student = {'name' : "Jon", 'age' : 25, 'courses': ['Math, CompSci']}

student.update({'name' : 'Jane', 'age': 25, 'phone': '555-5555'})
student.pop('age')

for key, value in student.items():
    print(key, value)
