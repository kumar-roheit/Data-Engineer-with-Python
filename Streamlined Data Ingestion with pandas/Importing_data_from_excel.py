The function in focus: read_excel()

#Task: Reading the spreadsheet
import pandas as pd 
pd.read_excel('foo.xlsx')


# Task: Skip the first two rows of the excel and get only the columns AD and the range AW through BA
foo_solution = pd.read_excel('foo.xlsx', skiprow=2,usecols="AD,AW:BA")


# Task: Create a data frame from the second workbook sheet , sheet position referncing starts from 0
# Created df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name=1)
