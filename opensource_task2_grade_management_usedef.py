# 조건: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 

#  키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성

#- 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수로 나누어 구현

#- 입력 형식

#    학번:

#    이름:

#     영어

#     C-언어:

#     파이썬:

#- 출력 형식

#                                 성적관리 프로그램         

#  =============================================================================

#   학번                    이름                 영어      C-언어      파이썬         총점       평균         학점          등수      

#  ==============================================================================

#  2023041001     홍길동                80            88             90           256         86           B+               1  

def input_scores():
    student_id = input("학번: ")
    name = input("이름: ")
    english_score = int(input("영어: "))
    c_score = int(input("C-언어: "))
    python_score = int(input("파이썬: "))
    return student_id, name, english_score, c_score, python_score

def calculate_total(student):
    return sum(student[2:])

def calculate_average(student):
    return round((sum(student[2:5]) / 3), 2)

def calculate_grade(student):
    average = calculate_average(student)
    if  average >= 95:
        return "A+"
    elif average >= 90:
        return "A"
    elif average >= 85:
        return "B+"
    elif average >= 80:
        return "B"
    elif average >= 75:
        return "C+"
    elif average >= 70:
        return "C"
    elif average >= 65:
        return "D+"
    elif average >= 60:
        return "D"
    else:
        return "F"

def calculate_rank(students):
    sorted_students = sorted(students, key=lambda x: x[4], reverse=True)
    for i, student in enumerate(sorted_students):
        student.append(i+1)

def print_scores(students):
    print("성적관리 프로그램")
    print("=" * 100)
    print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 100)
    for student in students:
        print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]}\t{student[7]}\t{student[8]}")

students = []
for _ in range(5):
    student = list(input_scores())
    student.append(calculate_total(student))
    student.append(calculate_average(student))
    student.append(calculate_grade(student))
    students.append(student)

calculate_rank(students)
print_scores(students)