inputMenu = eval(input("1.숫자\n2.문자\n입력유형을 선택하세요: "))

if inputMenu == 1 : 
  inputVar = input("숫자를 입력하세요: ")
  inputVar = eval(inputVar)
  print(inputVar)

elif inputMenu == 2:
  inputVar = input("문자를 입력하세요: ")
  print(inputVar)

else :
  print("잘못입력하셨습니다.")