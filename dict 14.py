a={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
sorted_values = sorted(a.values())
sorted_dict = {}
for i in sorted_values:
    for k in a.keys():
        if a[k]==i:
            sorted_dict[k] - a[k]
            break
print(sorted_dict)


