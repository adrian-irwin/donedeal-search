import json
import requests

from utils.inputParams import input_params

BASE_URL: str = "https://www.donedeal.ie/ddapi/v1/search"


def get_input(prompt: str, valid_inputs: dict) -> str:
    user_input = input(prompt)

    if valid_inputs == [] or valid_inputs == [""]:
        return ""
    elif user_input.lower() in valid_inputs:
        return user_input
    else:
        return get_input(prompt, valid_inputs)


def get_user_inputs() -> dict:
    user_inputs = {}

    print("Enter your search criteria below. Leave blank to ignore.")

    for input_param, value in input_params.items():
        user_input = get_input(value["prompt"], value["valid_inputs"])
        if user_input != "" and user_input != "any":
            user_inputs[input_param] = user_input

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
