**Pandas dtype VS dtypes**

In pd.DataFrame objects you only have dtypes, which is a series with the data type of each column.The good thing about this is that when you have a series you can treat it mostly uniformly as a NumPy array and use .dtype (which is a property present in every NumPy array) or as a data frame and use .dtypes (which is a property present in all Pandas objects). So in principle many functions for NumPy arrays or data frames already work with series out of the box.
