'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with Mathematical 
Operators. Focus on the operations and find the problems with the Mathematical
Operators.

The number of errors are as follows:
calculations: 4 errors
-2 logical
-2 syntax
'''

'''
This function takes a list of numbers of FIVE numbers and calculates the:
sum (all the numbers added up)
average (add all the numbers up and divide by how many there are)
range (biggest number - smallest number) (the biggest number is always the
last item and the smallest number is the first item)

'''
def calculations(list):
    sum = list[0] + list[1] + list[2] + list[3] + list[4]
    print("The sum is: " + str(sum))
    
    average = sum / 5
    print("The average is: " + str(average))
    
    diff = list[4] - list[0]
    print("The range is: " + str(diff))
    
    return

#Leave the following lines alone.
list = [24, 35, 46, 67, 78]
calculations(list)