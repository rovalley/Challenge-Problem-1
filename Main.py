with open("Challenge1/MontanaCounties.csv", "r") as file:
    file.readline()
    lines = file.readlines()
    licensePlates = {}
    for line in lines:
        line = line.strip()
        data = line.split(",")
        prefix = data[2]
        county = data[0]
        countySeat = data[1]
        licensePlates[prefix] = {"county": county, "countySeat": countySeat}

while True:
    prefix = input("Enter the license plate prefix or enter 'q' to quit: ")
    if prefix == "q":
        break
    if prefix not in licensePlates:
        print("Invalid prefix")
    else:
        info = input("Do you need the county or county seat or both?")
        if info == "county":
            print(licensePlates[prefix]["county"])
        elif info == "county seat":
            print(licensePlates[prefix]["countySeat"])
        elif info == "both":
            print(licensePlates[prefix]["county"])
            print(licensePlates[prefix]["countySeat"])
        else:
            print("Invalid")








