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
            output.append(value)
        # TODO: there are more cases that need to be handled here
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
            user_input = get_input(param, paramInfo)
            if user_input != []:
                temp[param] = user_input

        user_inputs[section] = temp

    return user_inputs


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
    }

    main_filters = user_inputs["main_filters"]
    make_model_filters = user_inputs["make_model_filters"]
    range_filters = user_inputs["range_filters"]

    for main_filter, main_filter_value in main_filters.items():
        body["filters"].append({"name": main_filter, "values": main_filter_value})

    for make_model_filter, make_model_filter_value in make_model_filters.items():
        if make_model_filter == "make":
            body["makeModelFilters"].append(
                {"make": make_model_filter_value, "model": "", "trim": ""}
            )
        elif make_model_filter == "model":
            if body["makeModelFilters"][0]["model"] == "":
                body["makeModelFilters"][0]["model"] = make_model_filter_value
            else:
                body["makeModelFilters"].append(
                    {
                        "make": body["makeModelFilters"][0]["make"],
                        "model": make_model_filter_value,
                        "trim": "",
                    }
                )

    range_filter: str
    for range_filter, range_filter_value in range_filters.items():
        trimmed_filter = range_filter.replace("min_", "").replace("max_", "")
        # check all current filters in ranges, if filter already exists, add value to it otherwise create new filter
        for filter in body["ranges"]:
            if filter["name"] == trimmed_filter:
                if range_filter.startswith("min_"):
                    filter["from"] = range_filter_value[0]
                elif range_filter.startswith("max_"):
                    filter["to"] = range_filter_value[0]
                break
        else:
            if range_filter.startswith("min_"):
                body["ranges"].append(
                    {
                        "name": trimmed_filter,
                        "from": range_filter_value[0],
                    }
                )
            elif range_filter.startswith("max_"):
                body["ranges"].append(
                    {
                        "name": trimmed_filter,
                        "to": range_filter_value[0],
                    }
                )

    return body


def get_search_results(body: dict) -> dict:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(body))
    return response.json()


if __name__ == "__main__":
    # user_inputs = get_user_inputs()
    # print(user_inputs)

    test_user_inputs = {
        "main_filters": {
            "sellerType": ["pro"],
            "fuelType": ["petrol", "electric", "hybrid"],
            "transmission": ["manual"],
            "bodyType": [
                "convertible",
                "coupe",
                "saloon",
                "hatchback",
                "estate",
                "mpv",
                "suv",
                "van",
            ],
            "numDoors": ["3", "4", "5", "6"],
            "colour": ["black", "blue", "white", "red", "green", "orange"],
            "country": ["ireland", "uk"],
            "verifications": [
                "manufacturerApproved",
                "greenlightVerified",
                "trustedDealer",
            ],
        },
        "make_model_filters": {"make": ["hyundai"]},
        "range_filters": {
            "min_year": ["2020"],
            "max_year": ["2024"],
            "min_price": ["10000"],
            "max_price": ["70000"],
            "min_mileage": ["0"],
            "max_mileage": ["400000"],
            "min_engine": ["1000"],
            "max_engine": ["7000"],
            "min_enginePower": ["100"],
            "max_enginePower": ["500"],
            "min_batteryRange": ["100"],
            "min_seats": ["2"],
            "max_seats": ["8"],
            "max_roadTax": ["1000"],
            "min_NCTExpiry": ["3"],
            "max_owners": ["5"],
            "min_warrantyDuration": ["3"],
        },
    }

    body = get_body(test_user_inputs)
    print(body)
