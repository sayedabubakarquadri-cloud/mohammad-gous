name=input("Enter the passenger name:")
if not name.isalpha():
    print("Invalid name only letter are allowed")
else:
    age=int(input("Enter the age:"))
    if age<=0:
        print("invalid Age:age must be positive number.")
    else:
        destination=input("Enter the Destination:")
        ticket=input("Enter th class(economy/bussiness/first):")
        if ticket.lower()=="economy"or ticket.lower()=="first":
            print("booking confirmed")
            print("name",{name})
            print("age",{age})
            print("destination",{destination})
            print("class:",{ticket.title()})
        else:("invalid class:please enter economy,bussiness,or first.")
        
            
    