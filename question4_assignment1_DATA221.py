from random import random #imports random function so now we can create numbers that are between 0-1

random_values_between_0_and_1= [random() for i in range(20)] #creates a list of 20 random numbers which are between 0-1
random_number_named_x=random() #generates one random number between 0-1 that can compare against the list

random_values_between_0_and_1.sort() #sorts list in from smallest-biggest

first_index_of_random_values=None #im setting a default value incase
index_counter=0 #starting an index counter at 0

for random_value in random_values_between_0_and_1: #loops through each number in sorted list
    if random_value>=random_number_named_x:
        first_index_of_random_values=index_counter
        break #first, checks if the current value is above or equal to x, then saves its index. and stops the loop as soon as we get one value that fits the condition with break
    index_counter=index_counter+1 #moving onto the next index

print("sorted list:", random_values_between_0_and_1)
print("x:",random_number_named_x)
print("First matching index:", first_index_of_random_values)