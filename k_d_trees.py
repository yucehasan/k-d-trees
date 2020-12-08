'''
CS 461 - Artificial Intelligence - Fall 2020 - Homework 5
Professor: Varol Akman
Group Name: PROMINI
Group Members:
    -Hakkı Burak Okumuş
    -Göksu Ece Okur
    -Yüce Hasan Kılıç

Algorithm represents the decision tree using k-d procedure to find the nearest neighbour in 2 dimensions.
Program uses a static input space of points with color, width and height.
To find the nearest neighbour in 2 dimension, we need dimensions of unknown point,
a set of points to find the nearest neighbour among them and a direction to compare points.
Logic is taken from the psuedocode in Winston textbook page 408 .

Currently, algorithm works for 2 dimensions. 
However, if the direction info is used non-binary, it can represent more directions
and comparisons can be made according more directions.
To achive this, we also need to change our points from 3-tuples to k+1-tuples where first value is the color, next k
values represent values in k dimensions.
We can sort the points in the desired dimension and split the set into two according to that direction

Current implementation do not use an actual tree structure.
It behaves the same by splitting the input set by sorting and splitting it in specified direction at each iteration
which is the exact thing decision trees do.
It can also go back one step and check the nearest neighbour in unlikely set if the distance to nearest neighbour in the
likely set is not less than the distance to the closest possible point in the unlikely set (boundary).
This approach is permitted by instructor (see https://piazza.com/class/kf2f1wy4ywp1na?cid=41)
'''
import math

# Taken from Winston textbook page 400 Figure 19.2
input_set = [ ("Red", 2, 6), ("Yellow", 5, 6), 
              ("Orange", 2, 5), ("Purple", 6, 5), 
              ("Red", 1, 2), ("Violet", 2, 1), 
              ("Blue", 4, 2), ("Green", 6, 1)]

# True denotes vertical direction false denotes horizontal direction 
def nearest_neighbour(x, y, points_set, boundary=math.inf, turn=True, single_stepping=False):
    # To find the nearest neighbour using the K-D procedure
    # Determine whether there is only one element in the set under consideration

    if len(points_set) == 1:
        if single_stepping:
            print("There is a single element in the set of consideration. Reporting...")
        # If there is only one, report it.
        return points_set[0]

    # Otherwise, compare the unknown, in the axis of comparison,
    # against the current node's threshold. The result determines
    # the likely set.
    likely_result = None
    if not turn:
        points_set.sort(key = lambda tup: tup[1])
        length = len(points_set)
        threshold = (points_set[length // 2 - 1][1] + points_set[length // 2][1]) / 2

        if single_stepping:
            print("Comparing against width. Threshold is", threshold)

        if x > threshold:
            likely_set = points_set[length // 2:]
            unlikely_set = points_set[:length // 2]
            dist_to_unl_set = abs(unlikely_set[-1][1] - x)

            if single_stepping:
                print("Unknown is above the threshold. Going right. Distance to unlikely set is", dist_to_unl_set)

            # Find the nearest neighbor in the likely set using this procedure.
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn, single_stepping=single_stepping)
        else:
            likely_set = points_set[:length // 2]
            unlikely_set = points_set[length // 2:]
            dist_to_unl_set = abs(unlikely_set[0][1] - x)

            if single_stepping:
                print("Unknown is not above the threshold. Going left. Distance to unlikely set is", dist_to_unl_set)

            # Find the nearest neighbor in the likely set using this procedure.
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn, single_stepping=single_stepping)

    else:
        points_set.sort(key = lambda tup: tup[2])
        length = len(points_set)
        threshold = (points_set[length // 2 - 1][2] + points_set[length // 2][2]) / 2

        if single_stepping:
            print("Comparing against height. Threshold is", threshold)

        if y > threshold:
            likely_set = points_set[length // 2:]
            unlikely_set = points_set[:length // 2]
            dist_to_unl_set = abs(unlikely_set[-1][2] - y)

            if single_stepping:
                print("Unknown is above the threshold. Going right. Distance to unlikely set is", dist_to_unl_set)

            # Find the nearest neighbor in the likely set using this procedure.
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn, single_stepping=single_stepping)
        else:
            likely_set = points_set[:length // 2]
            unlikely_set = points_set[length // 2:]
            dist_to_unl_set = abs(unlikely_set[0][2] - y)
            
            if single_stepping:
                print("Unknown is not above the threshold. Going left. Distance to unlikely set is", dist_to_unl_set)

            # Find the nearest neighbor in the likely set using this procedure.
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn, single_stepping=single_stepping)

    # Determine whether the distance to the nearest neighbor in
    # the likely set is less than or equal to the distance to the 
    # other set's boundary in the axis of comparison:

    dist_to_likely_nearest = math.sqrt( (x - likely_result[1]) ** 2 + (y - likely_result[2]) ** 2 )
    
    if single_stepping:
        print("Nearest neighbour in the likely set is found. Euclidean distance to that neighbour is {:.2f}".format(dist_to_likely_nearest)) 
        
    if dist_to_likely_nearest <= boundary:
            
        if single_stepping:
            print("Euclidean distance ({:.2f}) is less than or equal to the boundary ({}). Reporting the neighbour in the likely set...".format(dist_to_likely_nearest, boundary))

        # If it is, then report the nearest neighbor in the likely set
        return likely_result

    else:
        # If it is not, check the unlikely set using this procedure;
        # return the nearer of the nearest neighbors in the likely set
        # and in the unlikely set.

        if single_stepping:
            print("Euclidean distance ({:.2f}) is not bigger than the boundary ({}). Checking the neighbour in the unlikely set".format(dist_to_likely_nearest, boundary))
        unlikely_result = nearest_neighbour(x, y, unlikely_set, turn=not turn, single_stepping=single_stepping)
        dist_to_unlikely_nearest = math.sqrt( (x - unlikely_result[1]) ** 2 + (y - unlikely_result[2]) ** 2 )
        
        if single_stepping:
            if dist_to_unlikely_nearest > dist_to_likely_nearest:
                print("Nearest neighbour in the unlikely set is closer. ({:.2f}-{:.2f}) Reporting the neighbour in the unlikely set...".format(dist_to_unlikely_nearest, dist_to_likely_nearest))
            else:
                print("Nearest neighbour in the unlikely set is not closer. ({:.2f}-{:.2f}) Reporting the neighbour in the likely set...".format(dist_to_unlikely_nearest, dist_to_likely_nearest))

        return likely_result if dist_to_unlikely_nearest > dist_to_likely_nearest else unlikely_result

def main():
    x, y = input("Enter x and y coordinates: \n").split(" ")
    choice = input("Do you want single stepping? (y/n):\n") in ["Y", "y", "yes", "Yes"]
    result = nearest_neighbour(int(x), int(y), input_set, single_stepping=choice)
    print("Predicted color is", result[0])

if __name__ == "__main__":
    main()