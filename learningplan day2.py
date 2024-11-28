#1.	How do you use regular expressions in Python for pattern matching

#in this we have imported the re module and now we are fetching the first string same or not ny using match module 
"""import re

text = "Python calling"
match = re.match(r"calling", text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")"""
#now we r fetching the second word same or not by using search module

"""import re

text = "Python is future of programming"
search = re.search(r"is", text)

if search:
    print("Search found:", search.group())
else:
    print("No match found.")"""

#now we r fetching a random word in a sentence
"""import re

text = "Python is easy to understand."
matches = re.findall(r"is", text)

print("All matches found:", matches)"""

#now we r replacing the existing word in sentence with new word

"""import re

text = "The guy is very good in python"
new_text = re.sub(r"good", "bad", text)

print("Replaced text:", new_text)"""

#now r are performing split operation in string

"""import re

text = "python, pycharm; code verstiality"
fruits = re.split(r"[;, ]+", text)

print("Fruits list:", fruits)"""

###################################################################################################################################################

#2. What is a decorator, and provide an example of a decorator that times a function.

#firstly we have imported time module then we have created a decorator function and named it as timer_decorator which takes (func) as an argument
#then we have created a nested function in it which named as wrapper this function will wrap the original function
#the start_time is recorded before calling the original function and the end_time is recorded after the function call
#the execution_time variable stores the calculation of end_time and start_time
#the decorator returns the wrapper function which is then assigned to the original function

"""import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # record the start time
        result = func(*args, **kwargs)  # call the original function
        end_time = time.time()  # record the end time
        execution_time = end_time - start_time  # calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # return the result of the original function
    return wrapper

# Using the decorator

# using @ before the deorator name is the syntax 
# when example_function is defined it is automatically wrapped by the timer_decorator
#inside function we have initialised 0 to total
#then we have used the for loop which iterates from 1 to n for each integer i is in the range 
#then we call the decorated function

@timer_decorator
def example_function(n):
   
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Call the decorated function
result = example_function(1000000)
print("Result:", result)"""
################################################################################################################################################### 

#4. What is a lambda function, and provide an example of a lambda function that squares a

# data is a variable which stores a list of tuples also here all the tupels contains a name and a unique number 
"""data = [("java", 88), ("c++", 95), ("python", 82), ("javascript", 90)]

#here we have made a variable name as sorted_data 
#lambda function lambda x: x[1] takes a argument as x which is representing each tuple in the list  as it is returning x[1] which is the score 
#on the basis of this value only the sorting takes place into the ascending order 

sorted_data = sorted(data, key=lambda x: x[1])

# Print the sorted list
print(sorted_data)"""

##########################################################################################################################################################

#5.	How do you create a class in Python and what is inheritance?

#firstly we have created an class and named it as code 
# def __init__(self,langauge,domain,project) this is a constructor method which intializes the instance of the class
#self is the refrence to the instance being created it helps to access the attributes and methods of the class in whole of the file 
#langauge,domain,project are the parameters that the constructor accepts while creating a new instance of the class
#self.langauge = langauge this assigns the value of langauge parameter to the instance object self.langauge
#and both of this self.domain and self.project works on same logic
#def logic it is also a function created in class which defines a method named logic. When called it will execute the code inside it
#def implement also works on same logic as def logic 
#my_work = code("python","data science","company sales data analysis") - here we have created a new instance of this code class and named it as my_work
#it passes this arguments to the constructor 1.python 2. data science 3. company sales data analysis
#python is assigned to self.langauge
#data science is assigned to self.domain
#company sales data analysis is assigned to self.project
#and at  last we have called our both functions 

"""class code:
    def __init__(self,langauge,domain,project):
        self.langauge = langauge
        self.domanin= domain
        self.project= project
        
    def logic(self):
        print("logic successfull")
        
    def implement(self):
        print("Implementation successfull")
        
my_work = code("python","data science","company sales data analysis")
my_work.logic()
my_work.implement()"""


##########################################################################################################################################

#9.	Write a Python expression using generator expressions that generates even numbers up to 100.

#so here we have created a variable and named it as even_numbers then inside it we r using a for loop to iterate the all even elements from 0 to 100 
#as the loop starts from x and goes to n+1 according to question we have to find upto 100 that's why we have taken 101 because our n will be 100
#we can convert the generator to a list using list(even_numbers) to see all the even numbers at once 

even_numbers = (x for x in range(101) if x % 2 == 0)
even_numbers_list = list(even_numbers)
print(even_numbers_list)

###########################################################################################################################################