#----------------------------------------------------------------JSON----------------------------------------------------------------#
# JSON isn't a tabular format, so pandas makes assumptions about its orientation when loading data.

# Task: Load dhs_report_reformatted.json to a data frame with orient specified.
try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient="split")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
except ValueError:
    print("pandas could not parse the JSON.")

#Task: Get data from an API
# 1. use requests.get() to API. 
      #1. requests.get() needs a URL to get data from. 
      #2. certain API also needs search parameters and authorization headers passed to the params and headers keyword arguments, respectively.(like Yelp)
      #3. You'll need to extract the data from the response with its json() method, 
      #4. Pass it to pandas's DataFrame() function to make a data frame. Note that the necessary data is under the dictionary key "businesses".
# 1 URL
api_url = "https://api.yelp.com/v3/businesses/search"
#2. request.get() with Yelp API param and authorization header 
response = requests.get(api_url, 
                headers=headers, 
                params=params)

#3. Extract JSON data from the response
data = response.json()
#4. Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

#----------------------------------------------------------------JSON Nested----------------------------------------------------------------#
# Flatten Nested JSON
# Task: The Yelp API response data is nested. Your job is to flatten out the next level of data in the coodinates and location columns.
            # pandas (as pd) and requests have been imported. The results of the API call are stored as response.

# Load json_normalize()
from pandas.io.json import json_normalize
# Isolate the JSON data from the API response
data = response.json()
# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"], sep = "_")

#----------------------------------------------------------------Deeply Nested JSON----------------------------------------------------------------#
# Task: The categories attribute in the Yelp API response contains lists of objects. To flatten this data, you'll employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the data frame. You should also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions.
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates","longitude"]],
                    		meta_prefix="biz_")
# View the data
print(flat_cafes.head())
