# 숫자를 입력받습니다.
raw_input = input("inch 단위를 입력하세요: ")

# 입력된 데이터를 숫자 자료형으로 변환하고, CM 단위로 변환합니다.
inch = float(raw_input)
cm = inch * 2.54

# 변환된 결과를 출력합니다.
print(inch, "inch는", cm, "cm입니다.")
