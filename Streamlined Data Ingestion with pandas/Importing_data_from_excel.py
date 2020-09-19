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
# ALTERNATIVE one could just pass the actually wokrbook sheet's name to the attribute sheet name as shown below 
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name= '2017')

# Task: Load all sheets in the Excel file, list all 3 technique
all_survey_data = pd.read_excel("fcc_survey.xlsx",sheet_name=None) # Same as 
all_survey_data = pd.read_excel("fcc_survey.xlsx",sheet_name=['2016','2017']) # Same as
all_survey_data = pd.read_excel("fcc_survey.xlsx",sheet_name=[0,'2017']) 


# Working with multiple Spreadsheets
# Task: Survey file is set up with responses from different years in different sheets. Your task is to compile them in one data frame for analysis.

# Create an empty data frame
all_responses = pd.DataFrame()
# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)
# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

# Task: fcc_survey_subset.xlsx contains a string ID column and several True/False columns indicating financial stressors. You'll evaluate which non-ID columns have no NA values and therefore can be set as Boolean, then tell read_excel() to load them as such 

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={"HasDebt": bool})
# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())
