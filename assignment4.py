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
    def __init__(self, list1, list2, operator):
        self.input_1 = list1
        self.input_2 = list2
        self.operator = operator
        self.index = 0

        # Validation code for data types
        valid_operators = ["add", "sub", "div", "mul"]
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

        # Length validation
        if len(self.input_1) != len(self.input_2):
            raise ValueError(
                "Inconsistent length of lists, please re-enter lists with same length")

    def __iter__(self):
        return self

    def __next__(self):

        # Exit of our loop
        if self.index >= len(self.input_1):
            raise StopIteration

        # Addition (+)
        if self.operator == "add":
            index = self.index
            self.index += 1
            return self.input_1[index] + self.input_2[index]

        # Subtraction (-)
        if self.operator == "sub":
            index = self.index
            self.index += 1
            return self.input_1[index] - self.input_2[index]

        # Multiplication (*)
        if self.operator == "mul":
            index = self.index
            self.index += 1
            return self.input_1[index] * self.input_2[index]

        # Division (/)
        if self.operator == "div":
            index = self.index
            self.index += 1
            return round(self.input_1[index] / self.input_2[index], 2)

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
    def __init__(self, iterable):
        self.iterable = iterable

        # Validating data types of the input
        allowed_datatypes = [list, tuple]
        if type(self.iterable) not in allowed_datatypes:
            raise ValueError(
                "Inconsistent data type! Please re-enter data which either has the data type list or tuple.")

    # Handing + operator overloading
    def __add__(self, other):
        temp_list = []
        if type(other) in (list, tuple):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] + other[i])
            return (ListV2(temp_list))

        if type(other) == (ListV2):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] + other.iterable[i])
            return (ListV2(temp_list))

        if type(other) in (float, int):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] + other)
            return (ListV2(temp_list))

    # Handing - operator overloading
    def __sub__(self, other):
        temp_list = []
        if type(other) in (list, tuple):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] - other[i])
            return (ListV2(temp_list))

        if type(other) == (ListV2):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] - other.iterable[i])
            return (ListV2(temp_list))

        if type(other) in (float, int):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] - other)
            return (ListV2(temp_list))

    # Handing * operator overloading
    def __mul__(self, other):
        temp_list = []
        if type(other) in (list, tuple):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] * other[i])
            return (ListV2(temp_list))

        if type(other) == (ListV2):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] * other.iterable[i])
            return (ListV2(temp_list))

        if type(other) in (float, int):
            for i in range(len(self.iterable)):
                temp_list.append(self.iterable[i] * other)
            return (ListV2(temp_list))

    # Handing / operator overloading
    def __truediv__(self, other):
        temp_list = []
        if type(other) in (list, tuple):
            for i in range(len(self.iterable)):
                temp_list.append(round(self.iterable[i] / other[i], 2))
            return (ListV2(temp_list))

        if type(other) == (ListV2):
            for i in range(len(self.iterable)):
                temp_list.append(
                    round(self.iterable[i] / other.iterable[i], 2))
            return (ListV2(temp_list))

        if type(other) in (float, int):
            for i in range(len(self.iterable)):
                temp_list.append(round(self.iterable[i] / other, 2))
            return (ListV2(temp_list))

    def __repr__(self):
        return f"[{', '.join(map(str, self.iterable))}]"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            ans = self.iterable[self.index]
            self.index += 1
            return (ans)
        else:
            raise StopIteration

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
    def read_file(filename):
        with open(filename, 'r') as file:
            temp_list = []
            for line in file:
                if not line.strip():  # used for skipping empty lines!
                    continue
                temp_list.append(line.strip("\n"))
            return temp_list

    student_with_min_avg = min(read_file(filename), key=lambda list: sum(
        map(int, list.split(",")[1:])) / 5)

    return (lambda list: sum(map(int, list.split(",")[1:])) / 5, student_with_min_avg)

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

    with open(filename, 'r') as file:
        list_of_lines = []
        for line in file:
            if not line.strip():  # used for skipping empty lines!
                continue
            list_of_lines.append(line.strip("\n"))

    def avg_to_grade(string_student_names_marks):
        name = string_student_names_marks.split(",")[0]
        avg_marks = round(
            sum(map(int, string_student_names_marks.split(",")[1:])) / 5)

        if avg_marks >= 65 and avg_marks < 70:
            return name + ": D"
        if avg_marks >= 70 and avg_marks < 80:
            return name + ": C"
        if avg_marks >= 80 and avg_marks < 90:
            return name + ": B"
        if avg_marks >= 90:
            return name + ": A"

    final_answer = list(map(lambda string_student_names_marks: avg_to_grade(
        string_student_names_marks), list_of_lines))

    return (lambda string_student_names_marks: avg_to_grade(string_student_names_marks), final_answer)

    # END SOLUTION


def ex5(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file

    import json
    with open(filename) as infile:
        grades = json.load(infile)

    # BEGIN SOLUTION
    return (lambda dictionary: float(dictionary["test3"]), sorted(grades, key=lambda dictionary: float(dictionary["test3"])))

    # END SOLUTION
