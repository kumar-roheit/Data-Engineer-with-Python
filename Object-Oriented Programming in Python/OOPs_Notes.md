

* Classes and objects both have attributes and methods, but the difference is that a class is an abstract template, while an object is a concrete representation of a class.

> **Attributes** encode the **state** of an object and are represented by **variables**.
  >> e.g. (Attributes) `self.name` = `new.name` (parameter of the function) 
> **Methods** encode **behavior** of an object and are represesnted by **functions**.

* Think of `self` as the stand in for the future object for any class.
  * We can use the attributes and call other methods from within the class definition even when no objects were created yet.
  * object-dot-method is equivalent to passing that object as an argument.
  
  > `cust.identify("Roy")` will be interpreted as `Customer.identify(cust, "Roy")`
  
* Encapsulation- bundling data with methods that operate on data.
