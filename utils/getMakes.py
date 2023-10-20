import json
import re

import requests

url = "https://www.donedeal.ie/ddapi/legacy/search/api/v3/sections/filters/search/cars"


def get_makes():
    allMakes = []

    response = requests.get(url)
    response = response.json()

    for filter in response["searchFilters"]:
        if filter["name"] == "make":
            for make in filter["values"]:
                allMakes.append(
                    re.sub("[^0-9a-zA-Z]+", " ", make["displayName"].lower())
                )

    if "" not in allMakes:
        allMakes.append("")

    return allMakes


def save_makes_to_file(fileName):
    makes = get_makes()

    with open(fileName, "w") as file:
        json.dump(makes, file)


if __name__ == "__main__":
    makes = get_makes()
    for make in makes:
        print(make)
