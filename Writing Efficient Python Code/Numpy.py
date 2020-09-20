# Numpy arrays are Homogeneous - they must contain elements of the same type 
# if we create the element with mixed types like int and float ... numpy will convert the numpy arrays to float.
---------------------------------------------------------------------------------------------------------------------------
# Numpy arrays broadcast 
nums = np.array([1,2])
nums ** 2
---------------------------------------------------------------------------------------------------------------------------
# Numpy array indexing and boolean indexing 
nums = [-2, -1, 0, 1, 2]
nums_np =  np.array(nums)

# boolean indexing
nums_np > 0
nums_np[nums_np > 0] #outputs array([1,2])
---------------------------------------------------------------------------------------------------------------------------
# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)
