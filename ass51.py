"""
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to find maximum sum of non-adjacent numbers

"""

# Function to find the maximum sum
def rec(nums, idx):
	if idx >= len(nums):
		return 0
	return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))

def findMaxSum(arr, N):
	return rec(arr, 0)

# Driver Code
if __name__ == "__main__":
	# Creating the array
	arr = [2,3,4,55,33,4,55,343,66,77,88,99]
	N = len(arr)

	# Function call
	print(findMaxSum(arr, N))

