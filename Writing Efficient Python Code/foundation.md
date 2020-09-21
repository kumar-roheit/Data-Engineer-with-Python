#  Looping over a list.
Suppose you wanted to collect the names in the above list that have six letters or more.
```names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']```
Use list comprehension
```py 
best_list = [name for name in names if len(name) >= 6]
```
---------------------------------------------------------------------------------------------------------------------------------------------

## Zen of Python - a journey towards a pythonic way of coding
``` py 
import this
``` 
---------------------------------------------------------------------------------------------------------------------------------------------


# Buit-ins 
## range(Start, stop) excluding stop 
To print a range from 0 to 10 we can do the following: `range(0,11)` or `range(11)`
### More examples
```py
# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Creates a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)
```


## enumerate(iterable, start) 
   * Creates an index list of objects. 
   * The enumerate object can be converted into a list
   * Python's built-in enumerate() function allows you to create an index for each item in the object you give it. 
   * You can use list comprehension, or even unpack the enumerate object directly into a list, to write a nice simple one-liner.
            
   ```py
  enumerate(list, start=starting_index_to_enumerate_from)
  
  --------------------------------------------------------------------
  # check the below loop 
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewriting the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpacking an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)
  ```


## map(function ~~()~~, iterables) 
   * To apply a function (func()) to each element of list(or other dtypes), you can use the command `map(func, names)`.  
      #### Note that the func argument should not contain closing parentheses.
   ```py
      # Use map to apply str.upper to each element in names
      names_map  = map(str.upper, names)

      # Print the type of the names_map
      print(type(names_map))

      # Unpack names_map into a list
      names_uppercase = [*map(str.upper,names)]

      # Print the list created above
      print(names_uppercase)
```


## Timing and profiling the code
* Consider using the literal syntaxes (like [] instead of list(), {} instead of dict(), or () instead of tuple()), where applicable, to gain some speed.
* One can use %timeit to gather runtime for a single line of code (line magic mode) and %%timeit to get the runtime for multiple lines of code. 

## Code Profiling for time
* To profile a function in our code if we'd like to see line-by-line runtimes
    * Use `%load_ext line_profiler` to load the line_profiler within your IPython session. 
    * Use `%lprun -f convert_units convert_units(heroes, hts, wts)` to get line-by-line runtimes.
    
## Sets 
* Membership testing is much faster when you use sets. Did you notice that using a set for member testing is faster than using a list regardless if the item you are checking is in the set?
* Using a set data type to collect unique values is much faster than using a for loop (like in the find_unique_items() function). Since a set is defined as a collection of distinct elements, it is an efficient way to collect unique items from an existing object. 

## Numpy
* eliminate loops using NumPy broadcasting and list comprehension wherever possible.

## Miscellaneous 
* use combinations, map, zip, Counter, set wherever applicable to optimize your code firther.

# Pandas Optimization

* `.iterrows()` returns each DataFrame row as a tuple of (index, pandas Series) pairs, you can either split this tuple and use the index and row-values separately (as you did with `for i,row in pit_df.iterrows())`, or you can keep the result of `.iterrows()` in the tuple form (as you did with for` row_tuple `in `pit_df.iterrows())`.
  * If using `i,row`, you can access things from the row using square brackets (i.e., `row['Team']`). If using `row_tuple`, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., `row_tuple[1]['Team']`).
* `.itertuples()` returns each DataFrame row as a special data type called a` namedtuple`. You can look up an attribute within a` namedtuple` with a special syntax. 
  * Remember, you need to use the dot syntax for referencing an attribute in a `namedtuple`.
  *  .itertuples() is just like using .iterrows() except it tends to be faster. 

* .apply() method let's you apply functions to all rows or columns of a DataFrame by specifying an axis.
  * One could have also used .apply() directly on a Series (or column) of the DataFrame. For example, you could use rays_df['Playoffs'].apply(text_playoffs) to convert the 'Playoffs' column to text.
* Using a DataFrame's underlying arrays to perform calculations can really speed up your code and yields some significant efficiency gains.
* .itertuples() approach beat the .apply() approach? Even though both these implementations can be useful, you should default to using a DataFrame's underlying arrays(NUMpy) to perform calculations.
