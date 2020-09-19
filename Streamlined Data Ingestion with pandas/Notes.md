1. **Pandas dtype VS dtypes**  - In pd.DataFrame objects you only have dtypes, which is a series with the data type of each column.The good thing about this is that when you have a series you can treat it mostly uniformly as a NumPy array and use .dtype (which is a property present in every NumPy array) or as a data frame and use .dtypes (which is a property present in all Pandas objects). So in principle many functions for NumPy arrays or data frames already work with series out of the box.
      
2. In pandas, read_excel() module **sheet position referncing starts from 0**

3. If an Excel file has some sheets that you want loaded with the same parameters, you can get them in one go by **passing a list of their names or indices to read_excel()'s sheet_name keyword. *To get them all*, pass **None**.

4. **Date-Time processing with pandas** - Datetime columns are loaded as objects (*strings*) by default. We could specify that columns have datetimes with the **parse_dates** argument (not dtype!)
      * parse_dates can accept:
            - a list of column names or numbers to parse
            - a list containing lists of columns to combine and parse
            - a dictionary where keys are new column names and values are lists of columns to parse together
5. To reduce the file size, whenever we are ingesting a JSON data, we need to be mindfull that it may have been split formatted. 
      ```py
      df = pd.read_json("foo.json",orient="split")
      ```

