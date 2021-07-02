name=["srushti","amisha","sagreeka","neha"]
age=[19,20,21,20]
class1=["1st","2nd","3rd","4th"]
i=0
a={}
b=[]
while i<len(name):
    dic={"name":name[i],"age":age[i],"class":class1[i]}
    a.update(dic)
    b.append(dic)
    i=i+1
print(b)        