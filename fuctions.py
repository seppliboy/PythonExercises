#Task:
#Please complete the tutorial on QA Community for python functions

def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)

name = input("What is your name?: ")
homework_score = input("What is your homework score?: ")
assessment_score = input("What is your assessment score?: ")
exam_score = input("What is your exam score?: ")

def add_calc(homework_score, assessment_score, exam_score):
    answer = (homework_score + assessment_score + exam_score)
    return answer
print(answer/175*100)
