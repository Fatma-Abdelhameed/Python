from cmath import sqrt
import math
def get_distance(x1, x2, y1, y2):
     distance = math.sqrt(math.pow(x2-x1, 1) + math.pow(y2-y1, 2))
     return distance
print(get_distance(3,6,2,4)) #output=>2.6457513110645907
