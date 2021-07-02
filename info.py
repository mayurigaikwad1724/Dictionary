match={"mayuri":{
  "contact":9487743,
  "salary":1232367
}
}
for id, info in match.items():
  print(id)
  for key in info:
      print(key + ':', info[key])