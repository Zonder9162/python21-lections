# # class Salary:
# #     percent = 8

# #     def __init__(self, salary, experience):
# #         self.salary = salary
# #         self.experience = experience
    
# #     def count_percent(self):
# #         result = (self.salary * self.experience * self.percent) / 100
# #         return result

# # obj = Salary(10000, 10)
# # print(obj.count_percent()) 

# # class Password:
# #     def __init__(self, password):
# #         self.password = password

# #     def validate(self):
# #         if len(self.password) > 8 and len(self.password) < 15:
# #             if self.password.isnumeric:
# #                 if any(map(lambda x: x.isalpha(), self.password)) == True:
# #                     if bool('@#&$%!~*'.find(self.password)):
# #                         return ('Ваш пароль сохранен.')
# #                     else:
# #                         raise Exception('Your password should have some symbols')
# #                 else:
# #                     raise Exception('Password should contain letters as well')        
# #             else:
# #                 raise Exception('Password should contain numbers too') 
# #         else:
# #             raise Exception('Password should be longer than 8, and less than 15')
    
# #     def __str__(self):
# #         return len(self.password)*'*'

# # password = Password('short')
# # print(password.validate())
# # print(password)

# import math

# class Math:
#     def __init__(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         return math.factorial(self.value)
    
#     def get_sum(self):
#         return sum(list(map(int, str(self.value))))
    
#     def get_mul_table(self):
#         result = ''
#         for i in list(range(1,11)):
#             result += f'{self.value}x{i}={self.value * i}\n'
#         return result

# num = Math(11)

# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())


# Task 1

class Hogwatrs:
    
    faculties_qualities = {
        'courage': 'Gryffindor',
        'intelligence': 'Ravenclaw',
        'justice': 'Hufflepuff',
        'ambition': 'Slytherin'
    }

    def __init__(self, courage, intelligence, justice, ambition):
        self.courage = courage
        self.intelligence = intelligence
        self.justice = justice
        self.ambition = ambition
        self.qualities_dictionary = locals()

    def sorting_hat(self):
        dictionary = {v: k for k, v in self.qualities_dictionary.items() if type(v) == int()}
        maximum_point = max(dictionary.keys())
        maximum_quality = dictionary[maximum_point]
        self.faculty = Hogwatrs.faculties_qualities[maximum_quality]
        print(f'{self.faculty}!!!')

student = Hogwatrs(1,3,7,3)
student.sorting_hat()
