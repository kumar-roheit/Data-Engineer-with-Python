### Step 1
* **Create a file** (a.k.a Test Modules). File Name example-: `test_row_to_list.py`
  * `test_` indicate unit tests inside, this is the general naming convention.

### Step 2 
* **Imports** Import the package you  would use to perform unit testing. Example.-:` import pytest`

### Step 3
* **Unit Tests**  Define unit tests which follows a convetion just like the test module. Example-:  `def test_for_clean_row():`

### Step 4 
* **Assertion** `pytest` allows you to use the standard python `assert` for verifying expectations and values in Python tests.
ddddddd
### The end test file

```py
import pytest
import row_to_list

def test_for_clean_row():
 assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]
 
def test_for_missing_area():
 assert row_to_list("\t293,410\n") is None
 
 def test_for_missing_tab():
  assert row_to_list("1,46328,765\n") is None
  
```
### Guidelines 
* Do not use equality operator `=` to check if variable is `None` type.
* Spotting and fixing bugs
    > To find bugs in functions, you need to follow a four step procedure.
        Write unit tests.
        Run them.
        Read the test result report and spot the bugs.
        Fix the bugs.

