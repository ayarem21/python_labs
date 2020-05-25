def main():
    input_file = open("5_10.txt", 'r')
    Cities = dict()
    Information = list()
    for line in input_file:
        if (line == "\n"):
            continue
        if (line.__contains__("Місто")):
            inf = line.split()
            for i in range(0, len(inf), 1):
                Information.append(inf[i])
            continue
        strs = line.split()
        key = strs[0]
        value = [i for i in strs[1:len(strs)]]
        Cities[key] = value
    input_file.close()
    print(str(Cities))
    Set_areas = set()
    for key, value in Cities.items():
        Set_areas.add(value[0])
    Area_square = dict()
    Area_density = dict()
    Area_hospital = dict()
    Area_university = dict()
    for area in Set_areas:
        Area_square[area] = list()
        Area_density[area] = list()
        Area_hospital[area] = list()
        Area_university[area] = list()
    for key, value in Cities.items():
        List = Area_square[value[0]]
        List.append([key, float(value[2])])
        Area_square[value[0]] = List
        List = Area_density[value[0]]
        List.append([key, float(value[1]) / float(value[2])])
        Area_density[value[0]] = List
        List = Area_hospital[value[0]]
        List.append([key, (1000 * float(value[3])) / float(value[1])])
        Area_hospital[value[0]] = List
        List = Area_university[value[0]]
        List.append([key, (1000 * float(value[4])) / float(value[1])])
        Area_university[value[0]] = List
    output_file = open("5_10_result.txt", 'w')
    print("Areas_square:")
    output_file.write("\nAreas_square:\n")
    print_areas(Area_square, output_file)
    print("Areas_density:")
    output_file.write("\nAreas_density:\n")
    print_areas(Area_density, output_file)
    print("Area_hospital:")
    output_file.write("\nArea_hospital:\n")
    print_areas(Area_hospital, output_file)
    print("Area_university:")
    output_file.write("\nArea_university:\n")
    print_areas(Area_university, output_file)
    output_file.close()

def print_areas(Areas, output_file):
    for key, value in Areas.items():
        print(str(key) + ":")
        output_file.write(str(key) + ":")
        for city in value:
            print(str(city))
            output_file.write(str(city))
main()