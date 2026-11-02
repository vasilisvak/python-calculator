epp = 1
while epp != 0:
    print("1 prostesh")
    print("2 afairesi")
    print("3 pollaplasiasmos")
    print("4 diairesi")
    print("0 Exodos")
    epp = int(input("ti praji tha kaneis? "))

    if epp >= 1 and epp <= 4:
        print("dwse duo arithmous")
        a = float(input("dwse ton arithmo a: "))
        b = float(input("dwse ton arithmo b: "))

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
    elif epp < 0 or epp > 4:
        print("dwthike latos epilogi")
