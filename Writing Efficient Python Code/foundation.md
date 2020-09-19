# Task: looping over a list.
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Suppose you wanted to collect the names in the above list that have six letters or more.
# USE list comprehension
best_list = [name for name in names if len(name) >= 6]

# import this  - Zen of Python a journey towards a pythonic way of coding
# Buit-ins 
# range(Start, stop) excluding stop  
  eg.  range(0,11) or range(11)

# enumerate - Creates an index list of objects. The enumerate object can be converted into a list 
