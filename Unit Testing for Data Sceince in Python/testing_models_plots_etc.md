* The built-in tmpdir fixture is very useful when dealing with files in setup and teardown. tmpdir combines seamlessly with user defined fixture via fixture chaining. 
  * `tmpdir` and fixture chaining -Setup-Assert-Teardown

>   Setup of `tmpdir()`→ Setup of the `fixture(function)` → `test` → teardown of `fixture(function)` → teardown of `tmpdir()`

#### Mocking
Def: **Testing functions independently of dependencies**
* Packages for mocking in `pytest`
  * pytest-mock
  * unittest.mock
  
