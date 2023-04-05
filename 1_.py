import json

# dictionary of 7 Indian states and their capitals
indian_states = {
     "uttar pardesh": "Lucknow",
     "punjab": "chandigarh",
     "Assam": "Dispur",
     "Bihar": "Patna",
     "Chhattisgarh": "Raipur",
     "Goa": "Panaji",
     "Haryana": "chandigarh"
}

# write the dictionary to a JSON file
with open("indian_states.json", "w") as file:
    file.write(json.dumps(indian_states, indent=5))
    print("file is created .... ")