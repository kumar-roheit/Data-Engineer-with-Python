# Import pandas as pd
import pandas as pd


# Reading a CSV 
data = pd.read_csv('vt_tax_data_2016.csv')

read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', index_col=None, dtype=None, nrows=None, na_values=None, parse_dates=False,float_precision=None)
    Read a comma-separated values (csv) file into DataFrame.
    

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep='\t')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()



# Using only specific columns of the file 
cols = [ 'zipcode',  'agi_stub',  'mars1', 'MARS2', 'NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

#vt_data_first500 is already given
# Use nrows and skiprows to make a data frame, vt_data_next500, with the next 500 rows, also set the header argument so that pandas knows there is no header row.
# Lastly Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.
# Create data frame of next 500 rows with labeled columns

vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names= list(vt_data_first500))


# Specifying that agi_stub is "category" data and zipcode is string data. Reload the CSV and display the dtypes attribute
