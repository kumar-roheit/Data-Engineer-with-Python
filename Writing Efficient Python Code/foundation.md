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
