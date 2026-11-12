names = []
contacts = {}

while True:
    c = input("1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit: ")

    if c == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        contacts[name] = phone

    elif c == "2":
        name = input("Name: ")
        print(contacts.get(name, "Not found"))

    elif c == "3":
        name = input("Name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
        else:
            print("Not found")

    elif c == "4":
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
            names.remove(name)
        else:
            print("Not found")

    elif c == "5":
        for name in names:
            print(name, contacts[name])

    elif c == "6":
        break