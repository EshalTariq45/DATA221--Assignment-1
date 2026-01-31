#Question 8: Pandas Dataframe with computed column
import pandas as pd

data_given={
    'A': [1,2,2,1],
    'B': [3.1,4.2,1.5,6.3],
    'C': [800,150,400,210]
}

#creating the dataframe
dataframe_from_the_data_given= pd.DataFrame(data_given)

#adding a new column derived from existing columns (like multiplying column A and column C
dataframe_from_the_data_given["A_multiply_into_C"]=(dataframe_from_the_data_given["A"]*dataframe_from_the_data_given["C"])

#printing the final dataframe
print(dataframe_from_the_data_given)