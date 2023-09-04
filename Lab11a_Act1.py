# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Gavin Lane Phillips
#               Ford Hideo Bennett
#               Noah Quinn Hillis
#               Josh Amgad Botros
#               Ian Robert Wiechers
# Section:      472/572
# Assignment:   Lab 11 Act 1
# Date:         11/15/2021
#


#opens the file for reading
#pointFile =open('Lab11a_input.txt')



#makes an array of the points from the file given
def readfile(file):
    xyArray = []
    pointArray = []
    pointFile =open(file)
    for i in pointFile:
        array = []
        data = i.split(',')
        array.append(data[0])
        array.append(data[1])
        xyArray.append(array)

    xyArray.pop(0)

    for j in range(len(xyArray)):
        for k in range(len(xyArray[0])):
            holder = xyArray[j][k].split('\n')
            xyArray[j][k] = holder[0]

    for t in range(len(xyArray)):
        for q in range(len(xyArray[t])):
            xyArray[t][q] = int(xyArray[t][q])

    return xyArray
def cross(point1,point2):
    return float(point1[0])*float(point2[1])-float(point1[1])*float(point2[0])

#showlace that determines the area of the polygon
def shoelace(points):
    import numpy as np
    points = np.array(points)
    points = points.reshape(-1, 2)

    x = points[:, 0]
    y = points[:, 1]

    S1 = np.sum(x * np.roll(y, -1))
    S2 = np.sum(y * np.roll(x, -1))

    area = .5 * np.absolute(S1 - S2)

    return area

#main function that takes a filename as an input
def main():
    file = input("Please enter the filename: ")
    #file = "'" + filestring + "'"
    readfile(file)
    print("The area of the polygon is {:.1f}".format(shoelace(readfile(file))))

#print(readfile(pointFile))
#print(cross(xyArray[0],xyArray[1]))
#print(shoelace(xyArray))

if __name__ == '__main__':
    main()