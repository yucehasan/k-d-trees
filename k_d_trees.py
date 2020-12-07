'''
Psuedo-code for decision tree using k-d procedure
=================================================
To find the nearest neighbour using the K-D procedure
    * Determine whether there is only one element in the set 
    under consideration
        * If there is only one, report it.
        * Otherwise, compare the unknown, in the axis of comparison,
        against the current node's threshold. The result determines
        the likely set.
        * Find the nearest neighbor in the likely set using this
        procedure.
        * Determine whether the distance to the nearest neighbor in
        the likely set is less than or equal to the distance to the 
        other set's boundary in the axis of comparison:
            * If it is, then report the nearest neighbor in the likely
            set
            * If it is not, check the unlikely set using this procedure;
            return the nearer of the nearest neighbors in the likely set
            and in the unlikely set. 
'''
import math

# data.sort(key=lambda tup: tup[1])

input_set = [ ("Red", 2, 6), ("Yellow", 5, 6), 
              ("Orange", 2, 5), ("Purple", 6, 5), 
              ("Red", 1, 2), ("Violet", 2, 1), 
              ("Blue", 4, 2), ("Green", 6, 1)]

# print(vertical_set)

# True denotes horizontal
def nearest_neighbour(x, y, points_set, boundary=math.inf ,turn=True):
    if len(points_set) == 1:
        return points_set[0]

    likely_result = None
    if turn:
        points_set.sort(key = lambda tup: tup[1])
        length = len(points_set)
        threshold = (points_set[length // 2 - 1][1] + points_set[length // 2][1]) / 2
        if x > threshold:
            likely_set = points_set[length // 2:]
            unlikely_set = points_set[:length // 2]
            dist_to_unl_set = abs(unlikely_set[-1][1] - x)
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn)
        else:
            likely_set = points_set[:length // 2]
            unlikely_set = points_set[length // 2:]
            dist_to_unl_set = abs(unlikely_set[0][1] - x)
            likely_result = nearest_neighbour(x, y, likely_set, not turn)

    else:
        points_set.sort(key = lambda tup: tup[2])
        length = len(points_set)
        threshold = (points_set[length // 2 - 1][1] + points_set[length // 2][1]) / 2
        if x > threshold:
            likely_set = points_set[length // 2:]
            unlikely_set = points_set[:length // 2]
            dist_to_unl_set = abs(unlikely_set[-1][2] - y)
            likely_result = nearest_neighbour(x, y, likely_set, dist_to_unl_set, not turn)
        else:
            likely_set = points_set[:length // 2]
            unlikely_set = points_set[length // 2:]
            dist_to_unl_set = abs(unlikely_set[0][2] - y)
            likely_result = nearest_neighbour(x, y, likely_set, not turn)

    dist_to_likely_nearest = math.sqrt( (x - likely_result[1]) ** 2 + (y - likely_result[2]) ** 2 )
    if dist_to_likely_nearest <= boundary:
        return likely_result

    else:
        unlikely_result = nearest_neighbour(x, y, unlikely_set, not turn)
        dist_to_unlikely_nearest = math.sqrt( (x - unlikely_result[1]) ** 2 + (y - unlikely_result[2]) ** 2 )
        return likely_result if dist_to_unlikely_nearest > dist_to_likely_nearest else unlikely_result

def main():
    x, y = input("Enter x and y coordinates\n").split(" ")
    result = nearest_neighbour(int(x), int(y), input_set)
    print("Predicted color is", result[0])

if __name__ == "__main__":
    main()