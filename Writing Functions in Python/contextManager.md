### Context Manager 
* can be defined in two ways 
  * class-based
  * or decorating a cetain kind of fucntions

#### How to create a context manager
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
#### Scope 
Determines which variables can be accessed at different points in your code. 
  * Local - Interpretor will check inside the function.
  * Non-Local - In case of Nested function python will check the scope in the parent function before searching for the Global Scope
  * Global 
  * Built-In
* Python only gives you read access outside the current scope.
* What four values does this script print?
     ```py
     x = 50

     def one():
       x = 10

     def two():
       global x
       x = 30

     def three():
       x = 100
       print(x)

     for func in [one, two, three]:
       func()
       print(x)
     ```
* one() doesn't change the global x, so the first print() statement prints 50.
* two() does change the global x so the second print() statement prints 30.
* The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.
* But three() does not change the global x value so the last print() statement prints 30 again.

#### Closure
A closure in python is a tuple of variables that are no longer in scope, but that a function needed in order to run.
* Pythons way of attaching Non local variables to a returned fucntions.
* Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2), but only if they are used in the nested function. That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), then it would not be captured in new_func()'s closure.

```py
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None) #output: True
print(len(my_func.__closure__) == 2) #output: True

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17]) #output: True
```
### Decorator

Decorator Use: 
  Funcions as objects 
  Nested functions 
  Nonlocal scope
  Closures

* Decorator is a wrapper that you can place around a function that changes the fucntions behavior.
  * modify the inputs 
  * modify the outputs 
  * change the behaviour of the function itself.
  * ###### Note that @print_args before the definition of my_function is exactly equivalent to my_function = print_args(my_function). Remember, even though decorators are functions themselves, when you use decorator syntax with the @ symbol you do not include the parentheses after the decorator name.





