{
    'sonu':85,
    'Kartik':90,
    'Deepak':96,
    'Aman':76,
    'Somesh':60,
    'Umesh':85,
    'Amarpal':70,
    'Roshan':57,
    'Riyaz':98,
    'Shabid':56
} 

a=1
student=[]
mak=[]
while a<=10:
    user=input("enter student name: ")
    student.append(user)
    mark=int(input("enter student marks: "))
    mak.append(mark)
    a+=1
d=dict()
n=mak[0]
for i in student:
    d[i]=n
    n+=1
print(d)


