input_params = {
    "main_filters": {
        "sellerType": {
            "prompt": "Seller type [private, dealer, any]: ",
            "valid_inputs": ["private", "dealer", "any"],
            "singular": True,
        },
        "fuelType": {
            "prompt": "Fuel type [diesel, petrol, electric, hybrid, any]: ",
            "valid_inputs": ["diesel", "petrol", "electric", "hybrid", "any"],
            "singular": False,
        },
        "transmission": {
            "prompt": "Transmission [manual, automatic, any]: ",
            "valid_inputs": ["manual", "automatic", "any"],
            "singular": True,
        },
        "bodyType": {
            "prompt": "Body type [convertible, coupe, saloon, hatchback, estate, mpv, suv, van, pick up, any]: ",
            "valid_inputs": [
                "convertible",
                "coupe",
                "saloon",
                "hatchback",
                "estate",
                "mpv",
                "suv",
                "van",
                "pick up",
                "any",
            ],
            "singular": False,
        },
        "numDoors": {
            "prompt": "Number of doors [2, 3, 4, 5, 6, any]: ",
            "valid_inputs": [str(num) for num in range(2, 7)] + ["any"],
            "singular": False,
        },
        "colour": {
            "prompt": "Colour [grey, black, blue, white, red, green, orange, brown, yellow, purple, silver, beige, gold, other, any]: ",
            "valid_inputs": [
                "grey",
                "black",
                "blue",
                "white",
                "red",
                "green",
                "orange",
                "brown",
                "yellow",
                "purple",
                "silver",
                "beige",
                "gold",
                "other",
                "any",
            ],
            "singular": False,
        },
        "country": {
            "prompt": "Current country of registration [ireland, uk, northern ireland, any]: ",
            "valid_inputs": ["ireland", "uk", "northern ireland", "any"],
            "singular": False,
        },
        "verifications": {
            "prompt": "Verifications [manufacturer approved, greenlight verified, trusted dealer, any]: ",
            "valid_inputs": [
                "manufacturer approved",
                "greenlight verified",
                "trusted dealer",
                "any",
            ],
            "singular": False,
        },
    },
    "make_model_filters": {
        "make": {
            "prompt": "Make of Vehicle: ",
            "valid_inputs": [
                "any",
                "ac",
                "aro",
                "abarth",
                "alfa romeo",
                "aston martin",
                "audi",
                "austin",
                "bmw",
                "byd",
                "bentley",
                "chevrolet",
                "chrysler",
                "citroen",
                "cupra",
                "dfsk",
                "ds automobiles",
                "dacia",
                "daihatsu",
                "daimler",
                "dodge",
                "ferrari",
                "fiat",
                "ford",
                "honda",
                "hummer",
                "hyundai",
                "infiniti",
                "isuzu",
                "jaguar",
                "jeep",
                "kia",
                "levc",
                "lamborghini",
                "lancia",
                "land rover",
                "lexus",
                "lotus",
                "maxus",
                "mg",
                "maserati",
                "mazda",
                "mercedes",
                "mercedes benz",
                "mercedes-benz",
                "mini",
                "mitsubishi",
                "morgan",
                "morris",
                "nissan",
                "nissan president",
                "opel",
                "ora",
                "perodua",
                "peugeot",
                "polestar",
                "porsche",
                "reliant",
                "renault",
                "rolls royce",
                "rover",
                "seat",
                "saab",
                "skoda",
                "smart",
                "ssangyong",
                "subaru",
                "suzuki",
                "tesla",
                "toyota",
                "triumph",
                "vauxhall",
                "volkswagen",
                "volvo",
                "other",
            ],
            "singular": True,
        },
        "model": {
            "prompt": "Model of Vehicle: ",
            "valid_inputs": ["any"],
            "singular": False,
        },
    },
    "range_filters": {
        "min_year": {
            "prompt": "Minimum year of manufacture [1980-2024]: ",
            "valid_inputs": [str(year) for year in range(1980, 2025)] + ["any"],
            "singular": True,
        },
        "max_year": {
            "prompt": "Maximum year of manufacture [1980-2024]: ",
            "valid_inputs": [str(year) for year in range(1980, 2025)] + ["any"],
            "singular": True,
        },
        "min_price": {
            "prompt": "Minimum price (€) [0-70000]: ",
            "valid_inputs": [str(price) for price in range(0, 71_000, 500)]
            + ["any", "100"],
            "singular": True,
        },
        "max_price": {
            "prompt": "Maximum price (€) [0-70000]: ",
            "valid_inputs": [str(price) for price in range(0, 71_000, 1_000)] + ["any"],
            "singular": True,
        },
        "min_mileage": {
            "prompt": "Minimum mileage (km) [0-400000]: ",
            "valid_inputs": [str(mileage) for mileage in range(0, 410_000, 1_000)]
            + ["any"],
            "singular": True,
        },
        "max_mileage": {
            "prompt": "Maximum mileage (km) [0-400000]: ",
            "valid_inputs": [str(mileage) for mileage in range(0, 410_000, 1_000)]
            + ["any"],
            "singular": True,
        },
        "min_engine": {
            "prompt": "Minimum engine size (cc) [1000-7000]: ",
            "valid_inputs": [str(size) for size in range(1_000, 7_500, 100)] + ["any"],
            "singular": True,
        },
        "max_engine": {
            "prompt": "Maximum engine size (cc) [1000-7000]: ",
            "valid_inputs": [str(size) for size in range(1_000, 7_500, 100)] + ["any"],
            "singular": True,
        },
        "min_enginePower": {
            "prompt": "Minimum engine power (hp) [50-500]: ",
            "valid_inputs": [str(power) for power in range(50, 550, 50)] + ["any"],
            "singular": True,
        },
        "max_enginePower": {
            "prompt": "Maximum engine power (hp) [50-500]: ",
            "valid_inputs": [str(power) for power in range(50, 550, 50)] + ["any"],
            "singular": True,
        },
        "min_batteryRange": {
            "prompt": "Minimum battery range (km) [100-500]: ",
            "valid_inputs": [str(range) for range in range(100, 501, 100)] + ["any"],
            "singular": True,
        },
        "min_seats": {
            "prompt": "Minimum number of seats [2-8]: ",
            "valid_inputs": [str(seats) for seats in range(2, 9)] + ["any"],
            "singular": True,
        },
        "max_seats": {
            "prompt": "Maximum number of seats [2-8]: ",
            "valid_inputs": [str(seats) for seats in range(2, 9)] + ["any"],
            "singular": True,
        },
        "max_roadTax": {
            "prompt": "Maximum road tax (€) [150-1000]: ",
            "valid_inputs": [
                "150",
                "200",
                "300",
                "400",
                "500",
                "1000",
                "1000+",
                "any",
            ],
            "singular": True,
        },
        "min_NCTExpiry": {
            "prompt": "Minimum valid NCT (months) [3, 6, 9, 12, 18]: ",
            "valid_inputs": ["3", "6", "9", "12", "18", "any"],
            "singular": True,
        },
        "max_owners": {
            "prompt": "Maximum previous owners [0-5]: ",
            "valid_inputs": [str(num) for num in range(0, 6)] + ["any"],
            "singular": True,
        },
        "min_warrantyDuration": {
            "prompt": "Minimum warranty duration (months) [3, 6, 9, 12, 24, 36, 48, 60, 72, 84, 96, any]: ",
            "valid_inputs": [
                "3",
                "6",
                "9",
                "12",
                "24",
                "36",
                "48",
                "60",
                "72",
                "84",
                "96",
                "any",
            ],
            "singular": True,
        },
    },
}
