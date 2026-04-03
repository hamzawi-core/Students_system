Total=0
student_number=0

a=0
b=0
c=0
d=0
f=0

Largest=None
Lowest=None

while True:
    score=input("enter a score or done to finish : ")
    if (score == "done"):
        break
    try:
        score = float(score)
    except:
        print("invalid input")
        continue
    if score>100 or score<0 :
        print("invalid input")
        continue

    student_number+=1
    Total+=score

    if score>=90:
        a+=1
    elif score>=80:
        b+=1
    elif score>=70:
        c+=1
    elif score>=60:
        d+=1
    else:
        f+=1

    if Largest is None or score>Largest:
        Largest=score
    if Lowest is None or score<Lowest:
        Lowest=score

if student_number!=0:
    average=Total/student_number
    print("Largest score is :",Largest)
    print("Lowest score is :",Lowest)
    print("Average=",average)
    print("Total number of students:",student_number)
    print("A:",a)
    print("B:",b)
    print("C:",c)
    print("D:",d)
    print("F:",f)
else:
    print("there is no scores")