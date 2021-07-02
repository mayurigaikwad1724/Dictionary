a = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
b = "bug"
c = {}
for i in a:
  count = 0
  for j in i.split():
    if j == b:
      count = count+1
  c[count]=i
d = []
for s in sorted(c):
  d.append(c[s])
d.reverse()
print(d)






