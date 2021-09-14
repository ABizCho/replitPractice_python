#1부터 10까지 while로 모두더하기

i= 0
sum = 0


while i < 10 :
  print("i:",i,end=' | ')
  i= i+1
  sum = sum+i
  print("i++: ",i,"| sum: ",sum)


print("sum(1~10): ",sum)