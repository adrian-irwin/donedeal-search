import json

import requests

from utils.inputParams import input_params

BASE_URL: str = "https://www.donedeal.ie/ddapi/v1/search"


def get_input(info: dict) -> list[str]:
    output = []
    user_input = input(f"{info['prompt']}")

    user_input = [input.strip() for input in user_input.split(",")]

    if info["singular"] is True:
        user_input = user_input[:1]

    for value in user_input:
        if value == "" or value == "any":
            continue
        elif value in info["valid_inputs"]:
            output.append(value)
        else:
            print(f"Invalid input: {value}, Try again.")
            output += get_input(info)

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
            user_input = get_input(paramInfo)
            if user_input != []:
                temp[param] = user_input

        user_inputs[section] = temp

    return user_inputs


def get_body(user_inputs: dict) -> dict:
    body = {}
    return body


def get_search_results(body: dict) -> dict:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(body))
    return response.json()


if __name__ == "__main__":
    print(get_user_inputs())
