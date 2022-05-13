def phone_book(name,phonenumber):
    import re
    pattern = "[A-Za-z]{10}"
    pattern1="[0-9]{10}"
    name = str(input("User Name"))
    names=[]
    phonenumbers=[]
    phonenumber=str(input("Enter phone number"))
    #Forloop
    num=3
    if (re.search(pattern, name)):

        print(name)
    else:
        print("Please give full name")
        name = str(input("User Name"))

    if (re.search(pattern1,phonenumber)):
        print(phonenumber)

    else:
        print("please enter 10 digits number")




    for i in range(num):
        names.append(name)
        phonenumbers.append(phonenumber)



    for j in range(num):
        print(names[j],phonenumbers[j])


phone_book("NiravRajPandit","9161266177")