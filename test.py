def drink():
    print('Please input age')
    age = int(input(">> "))
    if age >= 18 and age <= 49:
        print("Allowed to Party")
    elif age > 49:
        print('Go back to your Family \n This is not for you')
    else:
        print("Go back Home to your Daddy")

drink()
