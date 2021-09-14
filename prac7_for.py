i = 0
sum = 0

print("== range(1,11) ==")
for i in range(1,11) : # 1에서 11-1,즉 10까지의 숫자리스트를 i에 순서대로 대입하여 반복시킴
 sum = sum +i
 print("i : ",i," | ","sum : ",sum)


print("Final Sum:", sum)
print("\n\n")

i = 0
sum = 0

print("== range(11) ==")
for i in range(11) : #0부터 for문이 끝날때마다 i를 1씩 증가시키기를 11회반복하여 i가 10에 이르고 명령문을 수행하고 반복문을 종료시킴  
 sum = sum + i
 print("i: ",i," | ","sum : ",sum)
   