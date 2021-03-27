# Used Google Takeout to get JSON files. Specifically "Location History" in archive

import glob


def readAndWrite():
    lines = []

    list_of_files = glob.glob('./*.json')
    for file_name in list_of_files:
        lines.append("\n==============" + file_name[2:6] + " " + file_name[7:10] + "==============\n")
        with open(file_name) as f:
            try:
                content = f.readlines()
            except UnicodeDecodeError:
                print("Could not read (Invalid character in file): " + file_name)

        content = [x.strip() for x in content]

        for line in content:
            if line[0:6] == '"name"' and line[8:-1] not in lines:
                lines.append(line[8:-1])

    output = open('places.txt', "w")
    for restaurant in lines:
        output.writelines(restaurant + "\n")


if __name__ == '__main__':
    readAndWrite()
