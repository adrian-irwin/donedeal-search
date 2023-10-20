import json
import sys

import requests

BASE_URL = "https://www.donedeal.ie/ddapi/v1/areas/"


def get_county_areas(county) -> dict:
    response = requests.get(BASE_URL + county)
    if response.ok is False:
        print(f"Error: {response.status_code}. {response.reason}")
        return
    response = response.json()
    return response


def save_county_areas_to_file(fileName):
    county_areas = get_county_areas()

    with open(fileName, "w") as file:
        json.dump(county_areas, file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        county = sys.argv[1]
    else:
        county = "dublin"

    county_areas = get_county_areas(county)
    for county_area in county_areas:
        print(county_area["displayName"])
