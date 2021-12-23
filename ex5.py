num_1 = int(input("Please enter first number:"))
num_2 = int(input("Please enter second number:"))
num_3 = int(input("Please enter third number:"))

def max_number(num_1,num_2,num_3):
    if (num_1 > num_2) and (num_1 > num_3):
        largest_number = num_1
    elif (num_2 > num_1) and (num_2 > num_3):
        largest_number = num_2
    else:
        largest_number = num_3
    
    print(f'Largest of the three numbers is {largest_number}')

max_number(num_1,num_2,num_3)
    
   
