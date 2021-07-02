 #Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 23)
print(marks)

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))

