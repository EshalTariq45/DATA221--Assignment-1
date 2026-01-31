#Question 1: controlled multiplication loop:

#variable names
the_threshold_value=int(input("give your threshold value:")) #threshold variable that the user will give
product_of_the_consecutive_integers_starting_from_one=1 #product of whatever integer once it passes threshold
currentNumber_of_the_multiplier=1 #current multiplier to keep track of

while product_of_the_consecutive_integers_starting_from_one<= the_threshold_value:
    currentNumber_of_the_multiplier=currentNumber_of_the_multiplier+1
    product_of_the_consecutive_integers_starting_from_one=product_of_the_consecutive_integers_starting_from_one*currentNumber_of_the_multiplier #product will keep getting multiplied by current number until it passes threshold

print(f"final product is {product_of_the_consecutive_integers_starting_from_one} and the integer that caused it to exceed the threshold is {currentNumber_of_the_multiplier}") #using f string to print the final product and the integer that caused product to exceed the threshold