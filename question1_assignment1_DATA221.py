#Question 1: controlled multiplication loop:

#variable names
threshold=int(input("give your threshold value:")) #threshold variable that the user will give
product=1 #product of whatever integer once it passes threshold
currentNumber=1 #current multiplier to keep track of

while product<=threshold: #while product is less than the threshold, it will continue in this while loop
    currentNumber=currentNumber+1 #adding to the current number so it can multiply into product with each run of while loop
    product=product*currentNumber #product will keep getting multiplied by current number until it passes threshold

print(f"final product is {product} and the integer that caused it to exceed the threshold is {currentNumber}") #using f string to print the final product and the integer that caused product to exceed the threshold