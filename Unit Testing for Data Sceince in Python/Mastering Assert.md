#### Assert statement general syntax

```py
assert boolean_expression, "message"
```

* The message argument of the assert statement would execute only when there is a Assertion Error.
* **Handling float return values** - Python handles flaot values differnetly from how a human will calculate. Always use `pytest.approx()` to wrap expected floating return value. 

#### Question Testing Float return values
get_data_as_numpy_array() takes two arguments: the path to a clean data file and the number of data columns in the file . An example file has been printed out in the IPython console. It contains three rows. *The function converts the data into a 3x2 NumPy array with dtype=float64. The expected return value has been stored in a variable called expected. Print it out to see it.* The housing areas are in the first column and the housing prices are in the second column. This array will be the features that will be fed to the linear regression model for learning.
The return value contains floats. write a test module to check the expected and actual return values are matching or not.
```py
import numpy as np
import pytest
from as_numpy import get_data_as_numpy_array

def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					   [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
  message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
  # Complete the assert statement
  assert actual == pytest.approx(expected), message
```
