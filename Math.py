import random
n = 1
Exam = []
Answer = []
Answer2 = []
T = 0
file = open("Math.txt","r",encoding='utf-8')
for i in file.readlines():
    a = i.split("=")
    Exam.append(a[0])
    Answer.append(a[1])
file.close
for i in Answer:
    j = i.replace("\n","")
    j = j.replace(" ","")
    Answer2.append(j)
while n <= 10:
    exam = random.randint(1,len(Exam)-1)
    print("題目",n,Exam[exam])
    answer = input("答案:")
    if answer == Answer2[exam]:
        T += 1
        print("正確")
    else:
        print("錯誤")
    n += 1
else:
    print("答對題數{}\n答錯題數{}".format(T,10-T))
    

    
