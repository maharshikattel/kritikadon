#  Syntax error

# def fun():
#     print("Done")


# name = "Kritika"
# print(name)




def divide(a,b):
    try:
       return a/b; 
    except ZeroDivisionError:    
        raise ZeroDivisionError("You can't divide by zero sir")
    except TypeError as type_error_message:
        print(type_error_message)
    except :
        raise ("Unexpected error occured")

print(divide(4,4))