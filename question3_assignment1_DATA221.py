#Question3: Safe Function Application
def the_power_of_given_variables(x,y):
    return x**y #this function returns x to the power of y

given_pairs=[[5,2],[3,-1],[4,3],[2,0]] #list of pairs given
result_after_appending_given_pairs=[]

for x,y in given_pairs:
    if y>=0: #ensuring that we skip pairs where y is negative
        result_after_appending_given_pairs.append(the_power_of_given_variables(x,y))
        #appending final list to hold pairs where y>=0

print(result_after_appending_given_pairs)

