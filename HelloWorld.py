
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)

for index, course in enumerate(courses):
    print(index, course)

course_str =  ', '.join(courses)

course_newList = course_str.split(', ')
print(course_newList)
