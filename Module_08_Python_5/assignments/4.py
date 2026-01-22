import json

populations = {
    'Bankura':150_000,
    'Kolkata':700_000,
    'Darjeeling':145_000
}

with open("cities.json", "w") as f:
    json.dump(populations, f, indent=4)


