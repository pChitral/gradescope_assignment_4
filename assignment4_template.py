class IteratorClass:
    # Complete this class! It takes in three inputs when initializing.
    # input#1 x -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#2 y -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#3 operator -- is a string that can either be 'add', 'sub', 'mul', 'div' -- If the specified operator
    # is not one of these, raise a ValueError.

    # Complete the class by writing functions that will turn it into an iterator class.
    # https://www.programiz.com/python-programming/methods/built-in/iter
    # The purpose of the class is to take two lists(x and y), apply the specified operator and return the output
    # as an iterator, meaning you can do "for ele in IteratorClass(x,y,'add')"
    # NOTE: For the / operator, round to two decimal places
    # Raise ValueError when the length is not the same for both inputs
    # Raise ValueError when the operator is not add, sub, mul, or div.

    # BEGIN SOLUTION
    def __init__(self, input_1, input_2, operator):

        # Assigning attributes to the class
        self.input_1 = input_1
        self.input_2 = input_2
        self.operator = operator
        self.limit = len(input_1)

        # Validation code for data types
        valid_operators = ["+", "-", "/", "*"]
        isValidList1 = True if (type(self.input_1) == list or type(
            self.input_1) == tuple) else False
        isValidList2 = True if (type(self.input_2) == list or type(
            self.input_2) == tuple) else False
        isValidOperator = True if (self.operator in valid_operators) else False

        if (isValidList1 and isValidList2 and isValidOperator):
            pass
        else:
            raise ValueError(
                "Inconsistent data types, please re-enter data in the valid data types")

        # Handling print() for the class

        def __str__(self):
            return f" First List/Tuple: [{', '.join(map(str, self.input_1))}] " + f" Second List/Tuple: [{', '.join(map(str, self.input_2))}]"

        # Iter
        def __iter__(self):
            self.value = 0
            return self

        def __next__(self):
            if self.value < self.limit:
                # Addition (+)
                if self.operator == "+":
                    output = self.input1[self.value] + self.input1[self.value]
                    self.value += 1
                    return output
                
                # Subtraction (-)
                if self.operator == "-":
                    output = self.input1[self.value] - self.input1[self.value]
                    self.value += 1
                    return output
                
                # Multiplication (*)
                if self.operator == "*":
                    output = self.input1[self.value] * self.input1[self.value]
                    self.value += 1
                    return output
                
                # Division (/)    
                if self.operator == "/":
                    output = round(
                        self.input1[self.value] / self.input1[self.value], 2)
                    self.value += 1
                    return output
            else:
                raise StopIteration

    # END SOLUTION


class ListV2:
    # Complete this class to fulfill the following requirement
    # 1) The class only takes one input argument which is a list or a tuple;
    #    Raise ValueError if the input is not a list or tuple
    # 2) The class overload loads +,-,*,/ and returns a ListV2 object as the result
    # 3) The class can handle +,-,*,/ for both list and int/float, meaning the thing to the right of the operator
    #    can be a sequence or a number;
    # 4) The class is an iterator
    # HINT: Study the assert statements in the test file to understand how this class is being used and reverse engineer it!
    # NOTE: For the / operator, round to two decimal places

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex3(filename):
    # Complete this function to read grades from `filename` and find the minimum
    # student test averages. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and use the min() function to find the student with the minimum
    # test average. The input to the min function should be
    # a list of lines. Ex. ['student1,33,34,35,36,45', 'student2,33,34,35,36,75']
    # input filename
    # output: (lambda_func, line_with_min_student) -- example (lambda_func, 'student1,33,34,35,36,45')

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex4(filename):
    # Complete this function to read grades from `filename` and map the test average to letter
    # grades using map and lambda. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and map() function.
    # The input to the map function should be
    # a list of lines. Ex. ['student1,73,74,75,76,75', ...]. Output is a list of strings in the format
    # studentname: Letter Grade -- 'student1: C'
    # input filename
    # output: (lambda_func, list_of_studentname_and_lettergrade) -- example (lambda_func, ['student1: C', ...])

    # Use this average to do the grade mapping. Round the average grade.
    # D = 65<=average<70
    # C = 70<=average<80
    # B = 80<=average<90
    # A = 90<=average
    # Define a function that takes in a number grade and returns the letter grade and use
    # it inside the lambda function.
    # HINT: create a function

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex5(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file

    import json
    with open(filename) as infile:
        grades = json.load(infile)

    # BEGIN SOLUTION
    pass
    # END SOLUTION
