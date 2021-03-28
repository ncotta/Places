# Used Google Takeout to get JSON files. Specifically "Location History" in archive

import glob
import requests


# Filters out addresses from json files
def filterOut():
    lines = []

    # Grab specified files
    list_of_files = glob.glob('./*.json')
    for file_name in list_of_files:
        # Added for readability
        lines.append("\n==============" + file_name[2:6] + " " + file_name[7:10] + "==============\n")

        # Open each file. If file could not be read due to unreadable character, skip over
        with open(file_name) as f:
            try:
                content = f.readlines()
            except UnicodeDecodeError:
                print("Could not read (Invalid character in file): " + file_name)

        f.close()
        content = [x.strip() for x in content]

        # Add each address in file to list
        for line in content:
            if line[0:9] == '"address"' and line[13:-2] not in lines:
                lines.append(line[13:-2])

    # Write each address into file
    output = open("places.txt", "w")
    for address in lines:
        output.writelines(address + "\n")


# Get addresses from google maps
def getAddresses():
    places_list = []
    api_file = open("api-key.txt", "r")
    api_key = api_file.read()
    api_file.close()

    fp = open("places.txt", "r")
    for line in fp:
        if not line.startswith("\n") and not line.startswith("="):
            places_list.append(line)
    fp.close()

    # print(places_list)

    for query in places_list:
        query = query.replace(" ", "+")
        query = query.replace(",", "")
        # base url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        # get response
        r = requests.get(url + "&query=" + query + "&key=" + api_key)
        # print(r.content)
        # print output
        output = r.json()["results"]
        if len(output) > 0:
            print(output[0]["name"])


if __name__ == '__main__':
    # print("Testing time for readAndWrite")
    # s = time.time()
    filterOut()
    getAddresses()
    # print("Time taken:", time.time() - s)
