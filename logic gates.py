def ander():
    a = int(input(" enter the input value of A (0/1) :-"))
    b = int(input(" enter the input value of B (0/1) :-"))
    if(a==0 or a== 1) and( b==0 or b==1):
        c = a * b
        if c > 1:
            c = 1
        return c;
    else:
        return 69;
def orrer():
    a = int(input(" enter the input value of A (0/1) :-"))
    b = int(input(" enter the input value of B (0/1) :-"))
    if (a == 0 or a == 1) and (b == 0 or b == 1):
        c = a + b
        if c > 1:
            c = 1
        return c;
    else:
        return 69;
def norrer():
    a = int(input(" enter the input value of A (0/1) :-"))
    b = int(input(" enter the input value of B (0/1) :-"))
    if (a == 0 or a == 1) and (b == 0 or b == 1):
        c = a + b
        if c > 1:
            c = 1
        if c==1 :
            c=0
        else:
            c=1
        return c
    else:
        return 69
def xorrer():
    a = int(input(" enter the input value of A (0/1) :-"))
    b = int(input(" enter the input value of B (0/1) :-"))
    if (a == 0 or a == 1) and (b == 0 or b == 1):
        if a == b:
          return 0;
        else:
            return 1;
    else:
        return 69;
def notter():
    a = int(input(" enter the input value of A (0/1) :-"))
    if (a == 0 or a == 1) :
        if a==1 :
            return 0;
        else:
            return 1;
    else:
        return 69;
# ---------------------------------------------------------------------------------------
print("         MENU            ")
print(" ")
print('     1.) And gate         ')
print('     2.) Or gate          ')
print('     3.) Nor gate         ')
print('     4.) Xor gate         ')
print('     5.) Not gate         ')
print('')
choi = int(input("  Please enter your choice (1-5) :- "))
ans = -1
if choi > 5 or choi < 1:
    print(" wrong choice entered . please retry ")
elif choi == 1:
    ans = ander()
elif choi == 2:
    ans = orrer()
elif choi == 3:
    ans = norrer()
elif choi == 4:
    ans = xorrer()
else:
    ans = notter()
if ans == 69 :
    print(" please enter the correct value of A and B ")
elif choi <=5 and choi >0:
    print(" the desired answer is :- " , ans)