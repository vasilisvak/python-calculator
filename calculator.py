
print("1 prostesh")
print("2 afairesi")
print("3 pollaplasiasi")
print("4 diairesi")
a = float(input("dwse ton arithmo a: "))
b = float(input("dwse ton arithmo b: "))
epp = int(input("ti praji tha kaneis?"))
if epp == 1:
    d = a + b
    print("to apotelesma einai", d)
elif epp == 2:
    d = a - b
    print("to apotelesma einai", d)
elif epp == 3:
    d = a * b
    print("to apotelesma einai", d)
elif epp == 4:
    if b == 0:
        print("den mporoume na kanoume diairesi me 0")
    else:
        d = a / b
        print("to apotelesma einai", d)
else:
    print("dwthike latos timh")