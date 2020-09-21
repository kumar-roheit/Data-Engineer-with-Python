# Docstrings

* ##### Google Doc String example 
```py
def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
```

* Tools like sphinx and pydoc that will automatically generate online documentation for you based off of your docstrings.
* When you need to set a mutable variable as a default argument, always use None and then set the value in the body of the function. This prevents unexpected behavior like adding multiple columns if you call the function more than once.
