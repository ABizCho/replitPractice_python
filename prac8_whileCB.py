i = 0;

while i < 10 :
  print("i: ",i)
  i=i+1
  print("i=i+1 : ",i)
  print("\n")

  if i == 7 :
    print("i == 7 -> continue")
    print("\n")
    continue
  
  if i == 8 : 
    print("i == 8 -> break")
    print("\n")
    break