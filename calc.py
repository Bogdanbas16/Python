while (True):

    num1 = float(input("\nПерше число: "))
    num2 = float(input("Друге число: "))

    fun = input("Дія (+ - * /)")

    if fun == '+':
        res = num1 + num2

    elif fun == '-':
        res = num1 - num2

    elif fun == '*':
        res = num1 * num2

    elif fun == '/':
        if num2 == 0:
            print("На нуль ділити не можнаю.")
            quit()
        res = num1 / num2

    print ("Резельтат: ", res, "\n")
