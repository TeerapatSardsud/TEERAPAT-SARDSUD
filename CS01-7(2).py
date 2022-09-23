a = int(input("คะเเนนเก็บ: "))
b = int(input("คะเเนนสอบกลางภาค: "))
c = int(input("คะเเนนสอบปลายภาค: "))
sumScore= a + b + c

if sumScore >= 80: print("A")
elif sumScore >= 75: print("B+");
elif sumScore >= 70: print("B");
elif sumScore >= 65: print("C+");
elif sumScore >= 60: print("C");
elif sumScore >= 55: print("D+");
elif sumScore >= 50: print("D");
eles: print("F") ;