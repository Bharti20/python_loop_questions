number1 = input('enter the first number.....')
number2 = input('enter the second number....')
try:
    num1= int(number1)
    num2 = int(number2)
    if num1 > num2 :
        i = 2
        hcf = 0
        while i < num1:
            if num1%i == 0 and num2%i ==0:
                hcf = i 
            i = i+1
        print(hcf)
    else:
        i = 2
        hcf = 0
        while i < num1:
            if num1%i == 0 and num2%i ==0:
                hcf = i 
            i = i+1
        print(hcf)
except Exception as e:
    print('Enter valid input')
