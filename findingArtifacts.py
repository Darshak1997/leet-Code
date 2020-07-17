N = 4
artifacts = "1B 2C,2D 4D"
searched = "2B 2D 3D 4D 4A"
# N = 3
# artifacts = "1A 1B,2C 2C"
# searched = "1B"
dic = {}
def MakingArray():
    maps = [[0 for i in range(N)]for j in range(N)]
    print(maps)
    artifactsLists = (artifacts.split(","))
    count = 1
    print(artifactsLists)
    for artifact in artifactsLists:
        coordinates = artifact.split(" ") 
        print(coordinates)
        leftMost = coordinates[0]
        rightMost = coordinates[1]
        print(leftMost)
        if leftMost[1] != rightMost[1]:
            print(count)
            maps[int(leftMost[0]) - 1][ord(leftMost[1]) - ord('A')] = count
            maps[int(leftMost[0]) - 1][ord(rightMost[1]) - ord('A')] = count
            maps[int(rightMost[0]) - 1][ord(rightMost[1]) - ord('A')] = count
            maps[int(rightMost[0]) - 1][ord(leftMost[1]) - ord('A')] = count
            dic[count] = 4
        else:
            print(count)
            score = 0
            for i in range(int(leftMost[0])-1, int(rightMost[0])):
                maps[i][ord(leftMost[1]) - ord('A')] = count
                score += 1
            dic[count] = score

        print("------------")
        count += 1

    print(maps)
    
    def findingArtifacts():
        searchedCoordinates = searched.split(" ")
        print(searchedCoordinates)
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                spot = ""
                spot += str(i+1)
                spot += chr(65 + j)
                if spot in searchedCoordinates:
                    maps[i][j] = "X"
    
        print(maps)
    
    def comparingResults():
        artifactsLists = (artifacts.split(","))
        result = [0, 0]
        marked = 1
        print(artifactsLists)
        for artifact in artifactsLists:
            coordinates = artifact.split(" ") 
            print(coordinates)
            count = 0
            leftMost = coordinates[0]
            rightMost = coordinates[1]
            print(leftMost)
            if leftMost[1] != rightMost[1]:
                print(count)
                if maps[int(leftMost[0]) - 1][ord(leftMost[1]) - ord('A')] == "X":
                    maps[int(leftMost[0]) - 1][ord(leftMost[1]) - ord('A')] = "#"
                    count += 1
                if maps[int(leftMost[0]) - 1][ord(rightMost[1]) - ord('A')] == "X":
                    maps[int(leftMost[0]) - 1][ord(rightMost[1]) - ord('A')] = "#"
                    count += 1
                if maps[int(rightMost[0]) - 1][ord(rightMost[1]) - ord('A')] == "X":
                    maps[int(rightMost[0]) - 1][ord(rightMost[1]) - ord('A')] = "#"
                    count += 1
                if maps[int(rightMost[0]) - 1][ord(leftMost[1]) - ord('A')] == "X":
                    maps[int(rightMost[0]) - 1][ord(leftMost[1]) - ord('A')] = "#"
                    count += 1
                print("Count: ", count)
                if count == dic[marked]:
                    result[0] += 1
                else:
                    result[1] += count
                print("Result: ", result)
            else:
                print(count)
                for i in range(int(leftMost[0])-1, int(rightMost[0])):
                    if maps[i][ord(leftMost[1]) - ord('A')] == "X":
                        count += 1
                print("Count: ", count)
                if count == dic[marked]:
                    result[0] += 1
                else:
                    result[1] += count
            print("------------")
            marked += 1

        print(maps, result)


    findingArtifacts()
    comparingResults()




MakingArray()
