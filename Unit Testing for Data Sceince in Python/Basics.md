### Step 1
* **Create a file** (a.k.a Test Modules). File Name example-: `test_row_to_list.py`
  * `test_` indicate unit tests inside, this is the general naming convention.

### Step 2 
* **Imports** . Import the package you  would use to perform unit testing. example.-: 
                                      ```py 
                                      import pytest 
### Step 3
* Unit Tests -: 
               ```py
               def test_for_clean_row():
               ```

###

```
```py
import pytest
import row_to_list

def test_for_clean_row():
 assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]
 
def test_for_missing_area():
 assert row_to_list("\t293,410\n") is None
```
