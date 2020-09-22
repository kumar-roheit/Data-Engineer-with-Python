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

* The three elements of a context manager are : a function definition, a yield statement, and the `@contextlib.contextmanager` decorator.
* timer() is a context manager that does not return an explicit value, so yield is written by itself without specifying anything to return.

* every time you use with open_read_only() your files are safe from being accidentally overwritten. The function is an example of a context manager that does return a value, so we write yield read_only_file instead of just yield. Then the read_only_file object gets assigned to my_file in the with statement so that whoever is using your context can call its .read() method in the context block.

* Task:  connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.

```py
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open 'NVDA.txt' for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
```
