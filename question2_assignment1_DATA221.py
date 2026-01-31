# Question2: Nested Dictionary from Strings
def list_of_strings_into_a_dictionary(string_list):
    dictionary_of_the_string_list={} #empty dictionary for where were putting the key and values

    for the_string_values in string_list:
        the_length_of_the_string_value=len(the_string_values) #loops through each string in the list and calculates its length

        if the_length_of_the_string_value%2==0: #determining if the remainder is 0 for length of strings
            parity_of_the_characters_in_the_string_value="even"
        else:
            parity_of_the_characters_in_the_string_value="odd"

        dictionary_of_the_string_list[the_string_values]={"length":the_length_of_the_string_value,"parity":parity_of_the_characters_in_the_string_value}
        #editing empty dictionary with the length of the string values as key, and the parity of the strings if they're even or odd

    return dictionary_of_the_string_list #returning dictionary into function

