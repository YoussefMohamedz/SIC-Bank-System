

import json
try:
    with open("users.json","r") as f:
        users = json.load(f)
except FileExistsError:
     users=[]
print("Hello welcome to Sic Bank <3 ")
while True:
    print("please select your choicee \n"
          "1. Register\n2. Login\n3. Exit")
    choice = input("enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        password = input("Enter password: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        gender = input("Enter gender: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        balance = 0
        user = {
            "name": name,
            "password": password,
            "phone": phone,
            "email": email,
            "gender": gender,
            "age": age,
            "city": city,
            "balance": balance
        }
        users.append(user)
        with open("users.json", "w") as f:
            json.dump(users, f)
        print(f"registration successful your id is {len(users)-1}")
    if choice == "3":
        print("closed")
        break
    elif choice == "2":
        try:
            uid = int(input("enter your id: "))
            password = input("enter your password: ")
            if uid < 0 or uid >= len(users):
                print("invalid id")
                continue
            if users[uid]["password"] != password:
                print("wrong password")
                continue
            print(f"welcome {users[uid]['name']} to sic bank ")


            while True:
                print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Check balance & info\n5. Exit")
                c = input("Enter choice: ")

                if c == "1": # deposit
                    try:
                        amount = float(input("enter amount to deposit: "))
                        currency = input("enter currency (USD, SAR, EGP): ").upper()
                        if currency == "USD":
                            egpamount = amount * 48.33 # 7awlha l egp bs3r el yom
                        elif currency == "SAR":
                            egpamount = amount * 12.88
                        elif currency == "EGP":
                            egpamount = amount
                        else:
                            print("invalid currency")
                            continue
                        users[uid]["balance"] += egpamount
                        with open("users.json", "w") as f:
                            json.dump(users, f)
                        print(f"deposited {egpamount} EGP successfully")
                    except:
                        print("invalid amount")
                elif c == "2":
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        currency = input("Enter currency (USD, SAR, EGP): ").upper()
                        if currency == "USD":
                            egpamount = amount * 48.33
                        elif currency == "SAR":
                            egpamount = amount * 12.88
                        elif currency == "EGP":
                            egpamount = amount
                        else:
                            print("Invalid currency")
                            continue
                        if egpamount > users[uid]["balance"]:
                            print("not enough balance")
                            continue
                        users[uid]["balance"] -= egpamount
                        with open("users.json", "w") as f:
                            json.dump(users, f)
                        print(f"withdrew {egpamount} EGP successfully.")
                    except:
                        print("invalid amount")
                elif c == "3":
                    try:
                        amount = float(input("enter amount to transfer:"))
                        tid = int(input("enter target account id:"))
                        if uid == tid :
                          print("u cant transfer to ur self")
                          continue
                        if tid < 0 or tid >= len(users):
                            print("target account does not exist")
                            continue
                        currency = input("enter currency (USD, SAR, EGP): ").upper()
                        if currency == "USD":
                             egpamount = amount * 48.33
                        elif currency == "SAR":
                            egpamount = amount * 12.88
                        elif currency == "EGP":
                            egpamount = amount
                        else:
                            print("Invalid currency")
                            continue
                        if egpamount > users[uid]["balance"]:
                            print("mot enough balance")
                            continue
                        users[uid]["balance"] -= egpamount
                        users[tid]["balance"] += egpamount
                        with open("users.json", "w") as f:
                            json.dump(users, f)
                        print(f"transferred {egpamount} EGP to account {users[tid]["name"]} successfully.")
                    except:
                        print("invalid input")

                elif c == "4":
                    print("personal info \n")
                    for k, d in users[uid].items():
                        if k != "password":
                            print(f"{k}: {d}")
                elif c == "5":
                    break
                else:
                    print("invalid choice")
        except:
            print("invalid input")
