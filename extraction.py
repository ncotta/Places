import glob


lines = []
list_of_files = glob.glob('./*.json')
for file_name in list_of_files:
    with open(file_name) as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for line in content:
        if line[0:6] == '"name"' and line[8:-1] not in lines:
            lines.append(line[8:-1])


output = open('places.txt', "w")
for restaurant in lines:
    output.writelines(restaurant + "\n")
