

a=["one","two","three","foure","five"]
b=[1,2,3,4,5]
d=dict()
n=b[0]
for i in a:
    d[i]=n
    n=n+1
print(d)