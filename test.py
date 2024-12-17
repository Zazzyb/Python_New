def drink():
    print('Please enter your Full Name')
    first_name = input('First Name : ')
    surname = input('Surname : ') 
    print('Please input age')
    age = int(input(">> "))
    if age >= 18 and age <= 49:
        print(surname + " " + first_name + ", You're allowed to Party")
    elif age > 49:
        print(surname + " " + first_name + ', Please go back to your Family \n This event is not for you')
    else:
        print(surname + " " + first_name + ", go back Home to your Daddy, Kid!!")

drink()
