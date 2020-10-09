**Context Manager** - To test whether a function raises an exception we could use a context manager. 

```py
with ____:    print("This is part of the context")    # any code inside is the context
```

#### Unit testing exceptions
```py
def test_value error_on_one_dimensional_argument():    
  example_argument = np.array([2081, 314942, 1059, 186606, 1148, 206186])
  with pytest.raises(ValueError):
    split_into_training_and_testing_sets(example_argument)
```

* If function raises expected `ValueError`, test will pass.
* If function is buggy and does not raise `ValueError`, test will fail.
