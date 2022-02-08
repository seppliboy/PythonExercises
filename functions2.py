#working

#name = input("What is your name?: ")

#def add_calc(score1, score2, score3):
    #answer = (score1 + score2 + score3) / 175 * 100
    #return answer

#score = add_calc(25,50,100)
#print("Your Name: ", name, "Score: ", score)





name = input("What is your name?: ")
homework_score = int(input("What is your homework score?: "))
assessment_score = int(input("What is your assessment score?: "))
exam_score = int(input("What is your exam score?: "))


def add_calc(homework_score, assessment_score, exam_score):
    answer = (homework_score + assessment_score + exam_score) / 175 * 100
    return answer

score = add_calc(homework_score, assessment_score, exam_score)
print("Your Name:", name, "\t", "Score (%):", score)