## Context Manager 
* can be defined in two ways 
  * class-based
  * or decorating a cetain kind of fucntions

### How to create a context manager
```py
def my_context():
  # Add any set up code you need
  yield
  # Add any teardown code you need
```
1. Define a function.
2. Add code blocks.
3. Use the yield keyword.
4. Add Teardown code.
