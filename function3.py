'''def details(name , fathername , mothername,course,siblings):
    print(f'myself {name} my father name is {fathername} and my mothername is {mothername} with btech course {course} and i have 2 siblings {siblings}')
details(name="shivani", siblings="nikhitha and pranay",course="cse",fathername="pandurangam",mothername="dhanalaxmi")'''

'''def number(*num):
    sum=0
    for i in num:
        sum+=i
    return (sum)
print(number(1,2,3,4,5))'''

'''def number(*num):
    multiplication=1
    for i in num:
        multiplication*=i
    print(multiplication)
number(1,2,3,4)'''

def details(**urdetails):
    for i,j in urdetails.items():
        print(f'{i}:{j}')
            

details(name="shivani",age=23,address="kphb",fathername="pandurangam",mothername="dhanalaxmi",course="python")

def number(num=(1,2,3)):
    multiplication=1
    for i in num:
        multiplication*=i
    print(multiplication)
number((1,2,3,4))

