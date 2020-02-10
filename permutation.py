# Python3 code to demonstrate 
# to compute all possible permutations 
# using itertools.product() 
import itertools 

# initializing list of list of [14][3] 
all_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18],[19, 20, 21],[22, 23, 24],[25, 26, 27],[28, 29, 30],[31, 32, 33],[34, 35, 36],[37, 38, 39] ] 

# printing lists 
print ("The original lists are : " + str(all_list)) 

# using itertools.product() 
# to compute all possible permutations 
res = list(itertools.product(*all_list)) 

# printing result 
print ("All possible permutations are : " + str(res)) 
