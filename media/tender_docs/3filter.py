def lessthan(n):
    if n <0:
       return 1
        
    return 0
 
 
number_list = list(range(-5, 5))
 
print(number_list)
 
 
#less_than_zero = list(filter(lambda x: x < 0, number_list))
 
less_than_zero = list(filter(lessthan, number_list))
 
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

###################################
