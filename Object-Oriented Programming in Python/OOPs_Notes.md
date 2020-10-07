

* Classes and objects both have attributes and methods, but the difference is that a class is an abstract template, while an object is a concrete representation of a class.

> **Attributes** encode the **state** of an object and are represented by **variables**.
  >> e.g. (Attributes) `self.name` = `new.name` (parameter of the function) 

> **Methods** encode **behavior** of an object and are represesnted by **functions**.

* Think of `self` as the stand in for the future object for any class.
  * We can use the attributes and call other methods from within the class definition even when no objects were created yet.
  * object-dot-method is equivalent to passing that object as an argument.
  
  > `cust.identify("Roy")` will be interpreted as `Customer.identify(cust, "Roy")`
  
* **Encapsulation**- bundling data with methods that operate on data.
* *Every time you refer to an attribute within a method, you should use the **self.attr** syntax.*

**Alternative constructors**

Python allows you to define class methods as well, using the `@classmethod` decorator and a special **first argument** `cls`. The main use of class methods is defining methods that return an instance of the class, but aren't using the same code as __init__().

For example, you are developing a time series package and want to define your own class for working with dates, *BetterDate*. The attributes of the class will be *year, month, and day*. You want to have a constructor that creates BetterDate *objects* given the *values* for year, month, and day, but you also want to be able to create *BetterDate objects* from strings like 2020-04-30.

You might find the following functions useful:

  `.split("-") method will split a string at"-" into an array, e.g. "2020-04-30".split("-") returns ["2020", "04", "30"],
    int() will convert a string into a number, e.g. int("2019") is 2019 .`

```py
# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod #class method decorator
    def from_str(cls, datestr): # special first argument cls
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dateobj):
      year, month, day = dateobj.year, dateobj.month, dateobj.day
      return cls(year, month, day) 


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)
```

###### Python always calls the child's __eq__() method when comparing a child object to a parent object.
