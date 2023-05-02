class student_log:
    student_count = 0

    def __init__(self, first, last, year, class_in):
        self.first = first
        self.last = last
        self.year = year
        self.class_in = class_in
        self.student_email = first + '.' + last + str(year) + '@kippjax.org'

        student_log.student_count += 1



    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    

    
stud_1 = student_log('Javi', 'Villanueva', 2022, 'Bagui')

stu_str_1 = 'Savannah-Janda-2024-Bagui'
first,last,year,class_in = stu_str_1.split('-')
new_student_1 = student_log(first,last,year,class_in)

print(new_student_1.first)
print(student_log.full_name(new_student_1))
