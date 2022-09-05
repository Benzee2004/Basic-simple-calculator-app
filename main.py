from ast import operator
# simple calculator python script
def calulator():
    try:
        # get the firstnumber from user
        first_number = int(input("Enter your first number\n"))
        # gets the basic arithemitic operating sign from users(-,+,*,/)
        operator = input("Enter your operator sign\n")
        # gets the secondnumber from users
        second_number = int(input("Enter your second number\n"))
    # function to do addition expression
        def add_num():
            if operator == "+":
                total = first_number + second_number
                print(f"Your sum is: {total}")
        add_num()
    # function to do substraction expression
        def sub_num():
            if operator == "-":
                total = first_number - second_number
                print(f"Your sub is:{total}")
        sub_num()
    # function to do multication expression
        def multiply():
            if operator == "*":
                total = first_number * second_number
                print(f"Your multiplication is: {total}")
        multiply()
    # function to do division expression
        def division():
            if operator == "/":
                total = int(first_number / second_number)
                print(f"Your division is:{total}")
        division()
    except:
        print("Enter a vaild number")

if __name__ == '__main__':
    calulator()
