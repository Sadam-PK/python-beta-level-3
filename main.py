# import unittest
# import pdb
#
#
# def join_name(fname, lname):
#     return ' '.join([fname.capitalize(), lname.capitalize()])
#
#
# return_data = join_name('sadam', 'khan')
# print(return_data)
#
#
# class TestStringMethods(unittest.TestCase):
#     def test_is_capitalized(self):
#         temp1, temp2 = return_data.split(' ')
#         self.assertTrue(temp1.istitle())
#         self.assertTrue(temp2.istitle())
#
#     def test_length(self):
#         self.assertTrue(len(return_data.split(' ')), 2)
#
#     def test_split(self):
#         self.assertEqual(type(return_data), str)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# ########### Debugging ########
#
# import pdb
#
#
# def sum_values(a, b):
#     return a + b
#
#
# def test_function():
#     pdb.set_trace()
#     print('This is the first line.')
#     print('This is the second line.')
#
#     value = sum_values(2, 3)
#     print('The code is done.')
#     print(value)
#
#
# test_function()


# ---------- Exercise 1 ------------
#
#
# class MathOperations:
#     # pdb.set_trace()
#
#     def add(self, n1, n2):
#         return n1 + n2
#
#     def sub(self, n1, n2):
#         return n2 - n1
#
#     def mul(self, n1, n2):
#         return n1 * n2
#
#     def div(self, n1, n2):
#         return n2 / n1
#
#     def menu(self):
#         print("\nSelect operation.")
#         print("1. Add, 2. Subtract, 3. Multiplication, 4. Division, 5. Exit")
#
#
# mo = MathOperations()
#
# if __name__ == '__main__':
#
#     pdb.set_trace()
#
#     while True:
#         mo.menu()
#         choice = input('Enter: ')
#
#         if choice == '1':
#             sumNo = mo.add(20, 30)
#             print(f'Addition = {sumNo}')
#
#         elif choice == '2':
#             subNo = mo.sub(50, 100)
#             print(f'Subtraction = {subNo}')
#
#         elif choice == '3':
#             mulNo = mo.mul(10, 20)
#             print(f'Multiplication = {mulNo}')
#
#         elif choice == '4':
#             divNo = mo.div(10, 20)
#             print(f'Division = {divNo}')
#
#         else:
#             exit(0)

# ----------- Decorators --------------
#
# def div(a, b):
#     print(a / b)
#
#
# def smart_div(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#             return func(a, b)
#
#     return inner
#
#
# div = smart_div(div)
# div(2, 4)

# def inc(x):
#     return x + 1
#
#
# def operate(func, x):
#     result = func(x)
#     print(result)
#
#
# operate(inc, 2)


# def display(message):
#     greet = 'Hi,'
#
#     def printer():
#         print(greet, message)
#     return printer
#
#
# func = display('Python is awesome.')
#
# func()

# ------------- Closure -------------
# numbers = []
#
#
# def enter_num(x):
#     numbers.append(x)
#     print(numbers)
#
#
# enter_num(10)
# enter_num(20)
# enter_num(30)

# ----- applying closure ----------
# def outer_number():
#     numbers = []
#
#     def inner_number(x):
#         numbers.append(x)
#         print(numbers)
#
#     return inner_number
#
#
# num = outer_number()
# num(10)
# num(20)
# num(30)

# ---------- Closure with classes ------------
# class OuterNum:
#     numbers = []
#
#     def inner_num(self, x):
#         self.numbers.append(x)
#         print(self.numbers)
#
#
# num = OuterNum()
# num.inner_num(10)
# num.inner_num(20)
# num.inner_num(30)
