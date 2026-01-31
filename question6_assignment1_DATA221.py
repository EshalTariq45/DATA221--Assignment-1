#Question6: Distribution Analysis


def percentage_less_or_equal_comparison_gathered_from_list(numbers_in_list): #Defining a function that takes an input of a list of numbers
    the_dictionary_result_after_sorting_the_keys={} #creating an empty dictionary where the final results are going to be stored
    total=len(numbers_in_list) #calculating how many numbers are in the list
    unique_values_from_the_list=sorted(set(numbers_in_list)) #set removes the duplicates and sorted puts numbers in ascending order

    for unique_value in unique_values_from_the_list: #loops through each unique number in list
        count=0 #counter for the current unique value

        for num in numbers_in_list: #loops through every number in the list
            if num <= unique_value: #checking if current number is less or equal to the current unique value
                count+=1 #if condition is true increase the count by one

        percentage_of_elements_in_the_list= (count/total)*100 #turning the count into a precentage for the whole list

        the_dictionary_result_after_sorting_the_keys[unique_value]= percentage_of_elements_in_the_list #adds a new entry into the dictionary where key-> unique value

    return the_dictionary_result_after_sorting_the_keys #returning the completed dictionary


number_list=[3,1,2,3,4,2]
print(percentage_less_or_equal_comparison_gathered_from_list(number_list)) #printing list into function
