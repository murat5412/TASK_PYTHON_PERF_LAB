with open("circle", 'r', encoding="utf-8") as rf:
    centr_circle_X, centr_circle_Y = map(float, rf.readline().strip().split(' '))
    radius_circle = float(rf.readline())

with open("points", 'r', encoding="utf-8") as rf:
    coordinates_point_X = []
    coordinates_point_Y = []
    for line in rf:
        coordinates_point_X.append(float(line.split()[0])) 
        coordinates_point_Y.append(float(line.split()[1]))
    
def main():
    wf = open("answers", "w")

    for i in range(len(coordinates_point_X)):
        if (pow(coordinates_point_X[i] - centr_circle_X, 2.0) + pow(coordinates_point_Y[i] - centr_circle_Y, 2.0) == pow(radius_circle,2.0)):
            wf.write('0'+'\n')
        elif (pow(coordinates_point_X[i] - centr_circle_X, 2.0) + pow(coordinates_point_Y[i] - centr_circle_Y, 2.0) < pow(radius_circle, 2.0)):
            wf.write('1'+'\n')
        else:
            wf.write('2'+'\n')
    
    wf.close()

main()