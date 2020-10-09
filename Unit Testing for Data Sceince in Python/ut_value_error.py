
# Question split_into_training_and_testing_sets() takes a NumPy array containing housing area and prices as argument. The function randomly splits the array row wise into training and testing arrays in the ratio 3:1, and returns the resulting arrays in a tuple.
  #If the argument array has only 1 row, the testing array will be empty. To avoid this situation, you want the function to not return anything, but raise a      ValueError with the message "Argument data_array must have at least 2 rows, it actually has just 1".
  
import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    exc_info.match(expected_error_msg)
