import json

import requests

from utils.inputParams import input_params

BASE_URL: str = "https://www.donedeal.ie/ddapi/v1/search"


def get_input(inputName: str, info: dict) -> list:
    output = []
    user_input = input(f"{info['prompt']}")

    user_input = [input.strip().lower() for input in user_input.split(",")]

    if info["singular"] is True:
        user_input = user_input[:1]

    for value in user_input:
        if value == "" or value == "any":
            continue
        elif value in info["valid_inputs"]:
            if inputName == "sellerType" and value == "dealer":
                value = "pro"
            elif inputName == "verifications":
                value = " ".join(
                    value.split(" ")[0] + value.split(" ")[1].capitalize()
                ).replace(" ", "")
            elif value == "uk":
                value = value.upper()
            elif (
                value == "mercedes"
                or value == "mercedes benz"
                or value == "mercedes-benz"
            ):
                value = "Mercedes-Benz"
            else:
                value = value.capitalize()
            output.append(value)
        else:
            print(f"Invalid input: {value}, Try again.")
            output += get_input(inputName, info)

    return output


def get_user_inputs() -> dict:
    user_inputs = {"main_filters": {}, "make_model_filters": {}, "range_filters": {}}

    print(
        f"\nEnter your search criteria below.\nSome fields can take multiple values, to do this separate them by a comma.\nLeave blank to ignore."
    )

    for section in input_params.keys():
        temp = {}
        print(f"\n{section.upper()}\n")

        for param, paramInfo in input_params[section].items():
            if param == "model" and "make" not in temp:
                continue
            elif (
                param == "min_batteryRange"
                and "fuelType" in user_inputs["main_filters"]
                and "Electric" not in user_inputs["main_filters"]["fuelType"]
            ):
                continue

            user_input = get_input(param, paramInfo)

            if user_input == []:
                continue

            if param.startswith("max_") and param.replace("max_", "min_") in temp:
                while (
                    user_input != []
                    and user_input[0] < temp[param.replace("max_", "min_")][0]
                ):
                    print(
                        f"Invalid input: {user_input[0]} is less than {temp[param.replace('max_', 'min_')][0]}, Try again."
                    )
                    user_input = get_input(param, paramInfo)

            if user_input != []:
                temp[param] = user_input

        user_inputs[section] = temp

    return user_inputs


def parse_main_filters(main_filters: dict) -> list:
    parsed = []
    for main_filter, main_filter_value in main_filters.items():
        parsed.append({"name": main_filter, "values": main_filter_value})
    return parsed


def parse_make_model_filters(make_model_filters: dict) -> list:
    if "make" not in make_model_filters or make_model_filters["make"] == "":
        return []
    parsed = [{"make": make_model_filters["make"][0], "model": "", "trim": ""}]

    for make_model_filter, make_model_filter_value in make_model_filters.items():
        if make_model_filter != "make":
            for model in make_model_filter_value:
                if parsed[0]["model"] == "":
                    parsed[0]["model"] = model
                else:
                    parsed.append(
                        {
                            "make": parsed[0]["make"],
                            "model": model,
                            "trim": "",
                        }
                    )

    return parsed


def parse_range_filters(range_filters: dict) -> list:
    parsed = []
    for range_filter, range_filter_value in range_filters.items():
        trimmed_filter = range_filter.replace("min_", "").replace("max_", "")
        # check all current filters in ranges, if filter already exists, add value to it otherwise create new filter
        for filter in parsed:
            if filter["name"] == trimmed_filter:
                if range_filter.startswith("min_"):
                    filter["from"] = range_filter_value[0]
                elif range_filter.startswith("max_"):
                    filter["to"] = range_filter_value[0]
                break
        else:
            if range_filter.startswith("min_"):
                parsed.append(
                    {
                        "name": trimmed_filter,
                        "from": range_filter_value[0],
                    }
                )
            elif range_filter.startswith("max_"):
                parsed.append(
                    {
                        "name": trimmed_filter,
                        "to": range_filter_value[0],
                    }
                )

    return parsed


def get_body(user_inputs: dict) -> dict:
    body: dict = {
        "sections": ["cars"],
        "sort": "",
        "terms": "",
        "filters": [],
        "geoFilter": {},
        "makeModelFilters": [],
        "ranges": [
            {"name": "year", "from": "", "to": ""},
        ],
        "paging": {"from": 0, "pageSize": 30},
    }

    if "main_filters" in user_inputs:
        body["filters"] = parse_main_filters(user_inputs["main_filters"])

    if "make_model_filters" in user_inputs:
        body["makeModelFilters"] = parse_make_model_filters(
            user_inputs["make_model_filters"]
        )

    if "range_filters" in user_inputs:
        body["ranges"] = parse_range_filters(user_inputs["range_filters"])

    return body


def get_search_results(body: dict) -> dict:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(body))
    return response.json()


def get_all_ads(body: dict) -> list:
    all_ads = []
    print("Getting page 0, starting at 0")
    initial_results = get_search_results(body)
    all_ads += initial_results["ads"]
    total_pages = initial_results["paging"]["totalPages"]
    for page in range(1, total_pages):
        body["paging"]["from"] = page * 30
        print(f"Getting page {page}, starting at {body['paging']['from']}")
        all_ads += get_search_results(body)["ads"]
    print("Done!")
    print(f"Total ads: {len(all_ads)}")
    return all_ads


if __name__ == "__main__":
    user_inputs = get_user_inputs()

    body = get_body(user_inputs)

    ads = get_all_ads(body)
