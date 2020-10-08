##### Syntax

```py
assert boolean_expression, "message"
```

* The message argument of the assert statement would execute only when there is a Assertion Error.
* **Handling float return values** - Python handles flaot values differnetly from how a human will calculate. Always use `pytest.approx()` to wrap expected floating return value. 
