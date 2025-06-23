student_scores = [150,120,100,90,80,70,60,50,40,30,20,10]
# 1 option
#total_exam_score = sum(student_scores)
#sum = 0
#for score in student_scores:
 #   sum += score
#print(sum)
#print(max(student_scores))
# 2 option
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        print(max_score)