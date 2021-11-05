def e_mail(a):
        if "." in a and "@" in a:
            print("This email adress is valid.")
        else:
            print("This email adress is invalid.")
e_mail(input("Please write an email adress \n"))


