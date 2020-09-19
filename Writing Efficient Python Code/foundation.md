#  looping over a list.
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
## - range(Start, stop) excluding stop  
  eg.  `range(0,11)` or `range(11)`

## - enumerate - Creates an index list of objects. The enumerate object can be converted into a list
  eg. ```py enumerate(list, start=starting_index_to_enumerate_from)```
 
