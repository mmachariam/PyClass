# int
# bool
# list
# float
# tuple
# str
# dict
# DUCK TYPING

"""
A
multiline
comment
"""
#
# num: int =10
# name: str ="John Doe"
# avg: float =40.9
# names: list =["Mary","John"]
# cars: tuple = ("volvo","benz")
# marks: set = [1,2,3]
# is_passed =True
# is_adult = False
#
# print(num)
# print(f'Name {name} average{avg}')
# print(names)
#
# (names.append("Ruth"))
# print(names)
# names.pop(1)
# print (names)
# #names. clear()
# print("After Clearing",names)
#
# # x: int = 0
# # while x>2:
# #    print(name)
#
# def func()-> None:
#     print(90)
#     age = 20
#
#     print("Average")
#     for j in "names":
#         print(j)
#
#         if age >= 20:
#             print(age)
#
# func()


std: dict = {"name": "Alice", "Age" : 21}
print(std)

students: list = [
    {"student_name": "Alice", "Marks": [70,89,67]},
    {"student_Name": "Bob", "Marks": [99,90,56]},
    {"student_Name": "Charlie", "Marks": [99,91,85]},
    {"John": "Charlie", "Marks":[99,78,89]},
]

def average (marks: list[int]) -> float:
    return sum (marks) / len(marks)
