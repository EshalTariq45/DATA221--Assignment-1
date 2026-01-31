#question 5: circle area comparison with validation

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    #here, im checking if both radii are positive
    if radiusOfCircle1<= 0 or radiusOfCircle2 <=0:
        return "Radii must be positive numbers"

    #doing calculations of the area for both circle 1 and circle 2
    area_of_circle_1=math.pi*radiusOfCircle1*radiusOfCircle1
    area_of_circle_2=math.pi*radiusOfCircle2*radiusOfCircle2

#figuring out which area is smaller than the other:
    if area_of_circle_1< area_of_circle_2:
        smaller_area_of_both_circles=area_of_circle_1
        larger_area_of_both_circles=area_of_circle_2
    else:
        smaller_area_of_both_circles=area_of_circle_2
        larger_area_of_both_circles=area_of_circle_1

#calculating the percentage of the cirles larger area that can be covered by the smaller circle
    percentage_of_larger_circles_area_that_is_covered_by_smaller_circle=(smaller_area_of_both_circles/larger_area_of_both_circles)*100
#returning the percentage
    return percentage_of_larger_circles_area_that_is_covered_by_smaller_circle

#asking the users input of both to use for the function
usersCircle1=int(input("enter radius of circle 1: "))
usersCircle2=int(input("enter radius of circle 2: "))

#printing whatever calculation the function gives us with input
print(circleAreaCoverage(usersCircle1,usersCircle2))