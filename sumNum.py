def sumNum():
    sumList = []
    plusMinus = ""

    with open("number.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for line in lines:
        plusMinus = ""
        if line == "":
            continue
        if line[0] == "+" or line[0] == "-":
            plusMinus = line[0][0]
            line = line[1:]
        
        if line.replace(".", "", 1).isdigit():
            if plusMinus == "-":
                line = plusMinus + line
            sumList.append(float(line))
        
    return sum(sumList)

sumNum()



    