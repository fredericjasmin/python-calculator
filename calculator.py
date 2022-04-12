# here the available languages are printed by console
print("""
What language do you speak?
1) English
2) Español""")
# in this input it will take the language you want to use
language = int(input("Select a language:\n"))
# here is the change of language to English
if (language==1):
    lang = 0
    print("You selected English")
# here is the change of language to Spanish
elif(language==2):
    lang = 1
    print("Usted seleccionó Español")
# here the menu is defined
def Menu():
# the calculator options menu will be printed here
    print(("""
Welcome to Frederic Jasmin calculator
1) Sum
2) Subtraction
3) Multiplication
4) Division
5) Exit""", """
Bienvenido a la calculadora de Frederic Jasmin
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")[lang])
# the calculator is defined here
def Calculator():
    # the menu starts here
    Menu()
    # in this input the number of the option selected will be taken
    option = int(input(("Select an option:\n", "Selecione una opcion:\n")[lang]))
    # if you select option 5 the following will happen
    while (option >0 and option <5):
        # in these inputs the numbers that will be operated will be taken
        x = float(input(("Enter a Number:\n", "Ingrese un Numero:\n")[lang]))
        y = float(input(("Enter Another Number:\n", "Ingrese Otro Numero:\n")[lang]))
        # sum
        if (option==1):
            print((f"The result of the sum is: {x+y}", f"El resultado de la Suma es: {x+y}")[lang])
            option = int(input(("Select another option:\n", "Selecione otra opcion:\n")[lang]))
        # subtraction
        elif(option==2):
            print((f"The result of the Subtraction is: {x-y}", f"El resultado de la Resta es: {x-y}")[lang])
            option = int(input(("Select another option:\n", "Selecione otra opcion:\n")[lang]))
        # multiplication
        elif(option==3):
            print((f"The result of the multiplication is: {x*y}", f"El resultado de la Multiplicacion es: {x*y}")[lang])
            option = int(input(("Select another option:\n", "Selecione otra opcion:\n")[lang]))
        # division
        elif(option==4):
            try:
                print((f"The result of the division is: {x/y}", f"El resultado de la Division es: {x/y}")[lang])
                option = int(input(("Select another option:\n", "Selecione otra opcion:\n")[lang]))
            # if a number is divided by zero it will say the following
            except ZeroDivisionError:
                print(("Division by 0 is not allowed", "No se permite la Division entre 0")[lang])
                option = int(input(("Select another option:\n", "Selecione otra opcion:\n")[lang]))
# here starts the calculator
Calculator()

# developed by Frederic Jasmin