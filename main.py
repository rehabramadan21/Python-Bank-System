##BEFORE interacting with user
import json

# قراءة البيانات من الملف (إن وجدت) أو إنشاء ملف جديد بمستخدم واحد
try:
    with open("data.json", "r") as file:
        dbList = json.load(file)
except FileNotFoundError:
    dbList = []
    info = {
        "name": "rehab",
        "password": "2612",
        "phone number": "011",
        "gender": "female",
        "age": 20,
        "city": "cairo",
        "id": 1,
        "currentBalance": 100
    }
    dbList.append(info)
    with open("data.json", "w") as file:
        json.dump(dbList, file, indent=2)

#id range  علي حسب اكبر واحد موجود
if dbList:
    idRange = max(user["id"] for user in dbList)
else:
    idRange = 0

############################
print("Welcome to SIC bank")
print("-------------------")
enter = False
askRegister = False

while enter == False:
    # تحديث البيانات من الملف قبل أي عملية
    with open("data.json", "r") as file:
        dbList = json.load(file)

    print("[1] Login (If you already have an account)")
    print("[2] Register (If you don't have an account yet)")
    print("-------------------------------------------------")
    who = input()
## interacting with user
    if who == "1": ##login
        enter=True
        login=False
        while login==False:
            with open("data.json", "r") as file:
                dbList = json.load(file)  # تحديث البيانات عند تسجيل الدخول

            loginID = (input("enter your ID: "))
            if loginID.isdigit():
                loginID=int(loginID)
                loginPass = input("enter your Password: ")
                if (loginID > (len(dbList)) or loginID <= 0):
                    print("invalid id")
                    continue
                for i in dbList:
                    if loginID == i["id"]:
                        if loginPass == i["password"]:
                            print("---------------------------------------------------------")
                            print("********* Welcome Back " + i["name"] + " *********")
                            currentBalance = i["currentBalance"]
                            online = True
                            while online == True:
                                print("your current balance is: " + str(currentBalance)+" EGP")
                                print("---------------------------------------------------------")
                                print("[0] Depostie")
                                print("---------------------------------------------------------")
                                print("[1] Withdraw")
                                print("---------------------------------------------------------")
                                print("[2] Transfer")
                                print("---------------------------------------------------------")
                                print("[3] Check balance")
                                print("---------------------------------------------------------")
                                print("[4] Check personal info")
                                print("---------------------------------------------------------")
                                print("[5] Exit")
                                print("---------------------------------------------------------")

                                theOperation = input("Please, Choose the operation: ")
                                if theOperation.isdigit():
                                    theOperation = int(theOperation)
#############################################################      Deposit         ############################################################################################################
                                    if theOperation == 0:
                                        print("SIC Bank allows depositing the following currencies:")
                                        print("USD,SAR and EGP")
                                        print("Please, enter the amount you want to deposit and the currency as(20 USD)")
                                        print("---------------------------------------------------------")
                                        depositeAmount = input()
                                        depositeAmount = depositeAmount.split(" ")
                                        if (len(depositeAmount)) != 2:
                                            print("Invalid format. Please use the format: 20 USD")
                                            print("---------------------------------------------------------")
                                            continue
                                        value = depositeAmount[0]
                                        currency = depositeAmount[1].upper()
                                        if value.replace('.', '', 1).isdigit():
                                            value = float(value)
                                            if value > 0:
                                                if currency == "USD":
                                                    currentBalance += value * 50
                                                    i["currentBalance"]=currentBalance
                                                    print(str(value) + " USD was deposited successfully!! ")
                                                    print("Your current Balance is " + str(currentBalance) + " EGP")
                                                    print("=========================================================")

                                                elif currency == "SAR":
                                                    currentBalance += value * 13
                                                    i["currentBalance"] = currentBalance
                                                    print(str(value) + " SAR was deposited successfully!! ")
                                                    print("Your current Balance is " + str(currentBalance) + " EGP")
                                                    print("=========================================================")

                                                elif currency == "EGP":
                                                    currentBalance += value
                                                    i["currentBalance"] = currentBalance
                                                    print(str(value) + " EGP was deposited successfully!! ")
                                                    print("Your current Balance is " + str(currentBalance) + " EGP")
                                                    print("=========================================================")

                                                else:
                                                    print("this currency is not allowed [USD,SAR or EGP]")
                                                    print("---------------------------------------------------------")
                                            else:
                                                print("Deposit amount must be greater than 0")
                                                print("---------------------------------------------------------")

                                        else:
                                            print("not allowed value")
                                            print("---------------------------------------------------------")

                                        with open("data.json", "w") as file:
                                            json.dump(dbList, file, indent=2)
#############################################################      Withdraw         ############################################################################################################
                                    elif theOperation == 1:
                                        print("SIC Bank allows Withdrawing the following currencies:")
                                        print("USD,SAR and EGP")
                                        print("Please, enter the amount you want to Withdraw and the currency as(20 USD)")
                                        print("-------------------------------------------------------------------------")
                                        withdrawAmount = input()
                                        withdrawAmount = withdrawAmount.split(" ")
                                        if (len(withdrawAmount)) != 2:
                                            print("Invalid format. Please use the format: 20 USD")
                                            print("---------------------------------------------------------")
                                            continue
                                        value = withdrawAmount[0]
                                        currency = withdrawAmount[1].upper()
                                        if value.replace('.', '', 1).isdigit():
                                            value = float(value)
                                            if value > 0:
                                                if currency == "USD":
                                                    if currentBalance >= (value * 48.88):
                                                        currentBalance -= value * 48.88
                                                        i["currentBalance"] = currentBalance
                                                        print(str(value) + " USD was Withdrawed successfully!! ")
                                                        print("Your current Balance is " + str(currentBalance) + " EGP")
                                                        print("=========================================================")
                                                    else:
                                                        print("your current balance can't afford the withdraw amount")

                                                elif currency == "SAR":
                                                    if currentBalance >= (value * 12.91):
                                                        currentBalance -= value * 12.91
                                                        i["currentBalance"] = currentBalance
                                                        print(str(value) + " SAR was Withdrawed successfully!! ")
                                                        print("Your current Balance is " + str(currentBalance) + " EGP")
                                                        print("=========================================================")

                                                    else:
                                                        print("your current balance can't afford the withdraw amount")


                                                elif currency == "EGP":
                                                    if currentBalance >= value:
                                                        currentBalance -= value
                                                        i["currentBalance"] = currentBalance
                                                        print(str(value) + " EGP was Withdrawed successfully!! ")
                                                        print("Your current Balance is " + str(currentBalance) + " EGP")
                                                        print("=========================================================")
                                                    else:
                                                        print("your current balance can't afford the withdraw amount")

                                                else:
                                                    print("this currency is not allowed [USD,SAR or EGP]")
                                                    print("---------------------------------------------------------")

                                            else:
                                                print("Withdraw amount must be greater than 0")
                                                print("---------------------------------------------------------")
                                        else:
                                            print("not allowed value")
                                            print("=========================================================")
                                        with open("data.json", "w") as file:
                                            json.dump(dbList, file, indent=2)
#############################################################      Transfer         ############################################################################################################
                                    elif theOperation == 2:
                                        desIdStatue=False
                                        while desIdStatue ==False:
                                            destinationID = input("Enter the destination ID you want to transfer: ")
                                            if destinationID.isdigit():
                                                destinationID=int(destinationID)
                                                if destinationID <= 0 or not any(user["id"] == destinationID for user in dbList):  # تعديل هنا
                                                    print("invalid ID")
                                                else:
                                                    for j in dbList:
                                                        if destinationID == j["id"]:
                                                            if destinationID != i["id"]:
                                                                transferAmount = input("enter the amount you want to transfer to " + j["name"] + " only in EGP: ")
                                                                transferAmount = float(transferAmount)
                                                                if transferAmount <= i["currentBalance"]:
                                                                    i["currentBalance"] = i["currentBalance"] - transferAmount
                                                                    j["currentBalance"] = j["currentBalance"] + transferAmount
                                                                    currentBalance = i["currentBalance"]
                                                                    desIdStatue = True
                                                                    with open("data.json", "w") as file:
                                                                        json.dump(dbList, file, indent=2)
                                                                    print("you transfered " + str(transferAmount) + " EGP to " + j["name"] + " successfully!! ")
                                                                    print("And now " + i["name"] + " your current balance is " + str(i["currentBalance"]))
                                                                    print("=========================================================")

                                                                elif transferAmount > i["currentBalance"]:
                                                                    print("your current balance can't afford the transfer operation")
                                                                    print("---------------------------------------------------------")

                                                            else:
                                                                print("HAHAHA…Nice try, but you can’t transfer money to yourself, "+i["name"]+" !!!!!!!!!!!!")
                                                                print("---------------------------------------------------------")

                                            else:
                                                print("invalid id , please enter only integer numbers more than 0")
                                                print("---------------------------------------------------------")
#############################################################      Check balance         ############################################################################################################
                                    elif theOperation == 3:
                                        checkCurrencyType=True
                                        while checkCurrencyType==True:
                                            print("[1] EGP")
                                            print("[2] SAR")
                                            print("[3] USD")
                                            print("[4] Show all")
                                            currencyType = input("choose the cerrency you want to show your current balance")
                                            print("-------------------------------------------------------------------------")

                                            if currencyType == "1": ##EGP
                                                checkCurrencyType = False
                                                print("your current balance: "+str(i["currentBalance"])+" EGP")
                                                print("=========================================================")
                                            elif currencyType == "2": ##SAR
                                                checkCurrencyType = False
                                                print("your current balance: " + str((i["currentBalance"]/12)) + " SAR")
                                                print("===============================================================")
                                            elif currencyType == "3":##USD
                                                checkCurrencyType = False
                                                print("your current balance: " + str((i["currentBalance"])/50) + " USD")
                                                print("=================================================================")
                                            elif currencyType == "4":
                                                checkCurrencyType = False
                                                print("your current balance: " + str(i["currentBalance"]) + " EGP")
                                                print("your current balance: " + str((i["currentBalance"]/12)) + " SAR")
                                                print("your current balance: " + str((i["currentBalance"])/50) + " USD")
                                                print("=================================================================")
                                            else:
                                                print("not allowed choice")
#############################################################      Check personal info         ############################################################################################################
                                    elif theOperation == 4:
                                        print("Hello, "+ str(i["name"]))
                                        print("---------------------------")
                                        print("your password is: "+str(i["password"]))
                                        print("your ID is: "+str(i["id"]))
                                        print("your current balance is: "+str(i["currentBalance"]))
                                        print("your age is: "+str(i["age"]))
                                        print("your gender is: "+str(i["gender"]))
                                        print("you live in "+str(i["city"]))
                                        print("your phone number is: "+str(i["phone number"]))
                                        print("============================")
#############################################################      Exit         ############################################################################################################
                                    elif theOperation == 5:
                                        print("Thank you for using SIC Bank, "+ i["name"])
                                        print("=======================================")
                                        login = True
                                        enter = False
                                        break

                                    else:
                                        print("not allowed value, please choose only [0,1,2,3,4,5]")
                                        print("---------------------------------------------------------")

                                else:
                                    print("not allowed value, please choose only [0,1,2,3,4,5]")
                                    print("---------------------------------------------------------")

                        else:
                            print("wrong password")
                            print("---------------------------------------------------------")

            else:
                print("invalid id , please enter only integer numbers more than 0")
                print("---------------------------------------------------------")

#############################################################      register         ############################################################################################################
    elif who == "2":
        askRegister=False
        while askRegister==False:
            with open("data.json", "r") as file:
                dbList = json.load(file)

#                        ==============================================>> check name
            checkName=False
            while checkName == False:
                nameAsk=input("enter your name: ")
                print("---------------------------------------------------------")
                dashCount = 0
                validName = True
                for character in nameAsk:
                    if character.isalpha() or character==" " or character=="-":
                        if character == "-":
                            dashCount += 1
                            if dashCount > 1:
                                print("not allowed name")
                                validName=False
                                break
                    else:
                        print("this name is not valid")
                        validName=False
                        break
                if validName==True:
                    name = nameAsk
                    checkName = True

#                         ==============================================>> check password
            checkPass=False
            while checkPass==False:
                passAsk = input("enter your password: ")
                print("---------------------------------------------------------")
                if len(passAsk)>=4:
                    password=passAsk
                    checkPass=True
                else:
                    print("Weak password! It must be at least 4 characters long.")
                    print("---------------------------------------------------------")

#                         ==============================================>> check phone
            checkPhone=False
            while checkPhone == False:
                phoneAsk= input("enter your phone number: ")
                print("---------------------------------------------------------")
                if phoneAsk.isdigit():
                    if len(phoneAsk) == 11:
                        phoneNumber = phoneAsk
                        checkPhone = True
                    else:
                        print("This number is not complete!!! It must be 11 digits long")  # تعديل هنا
                        print("---------------------------------------------------------")
                else:
                    print("invalid phone number")
                    print("---------------------------------------------------------")

#                         ==============================================>> check gender
            checkGender=False
            while checkGender==False:
                genderAsk=input("enter your gender[male-female]: ")
                print("---------------------------------------------------------")
                genderAsk=genderAsk.lower()
                if (genderAsk == "male" or genderAsk == "female"):
                    gender=genderAsk
                    checkGender=True
                else:
                    print("HAHAHAAA ! This bank only supports humans, not aliens!")

 #                         ==============================================>> check age
            checkAge=False
            while checkAge == False:
                ageAsk=input("enter your age: ")
                print("---------------------------------------------------------")
                if ageAsk.isdigit():
                    ageAsk=int(ageAsk)
                    if ageAsk<20:
                        print("sorry,"+name+" You must be at least 20 years old to open a bank account")
                        print("-------------------------------------------------------------------------")
                    elif ageAsk >200:
                        print("what??? you Are "+str(ageAsk)+" years old !!!!!!!!!!!!!!!")
                        print("---------------------------------------------------------")
                    else:
                        age=ageAsk
                        checkAge=True
                else:
                    print("if you are not WEGZZZ , We m4 bettma4a Fy el Zaman ma7shy taka , we 3ndak Amal 3bkari ??")
                    print("You are only allowed to enter numbers in your age ya Fnaan ")
                    print("-----------------------------------------------------------")

#                         ==============================================>> check city
            checkCity=False
            while checkCity == False:
                cityAsk = input("enter your city: ")
                print("---------------------------------------------------------")
                if cityAsk.replace(" ","").isalpha():
                    city=cityAsk
                    checkCity=True
                else:
                    print("City names should only contain letters")
                    print("---------------------------------------------------------")

#                         ==============================================>> check balance
            checkBalance=False
            while checkBalance == False:
                askCurrentBalance = input("enter your Start balance[in egp]: ")
                print("---------------------------------------------------------")
                dotCount = 0
                validBalance=True
                for character in askCurrentBalance:
                    if (character.isdigit() or character=="."):
                        if character==".":
                            dotCount+=1
                            if dotCount>1:
                                print("not allowed balance")
                                print("---------------------------------------------------------")
                                validBalance=False
                                break
                    else:
                        validBalance=False
                        break
                if validBalance==True:
                    currentBalance = float(askCurrentBalance)
                    checkBalance=True

            userExists = False
            for user in dbList:
                if (user["name"] == name and user["age"] == age and user["city"] == city):
                    print("this user is already exist in the system")
                    print("---------------------------------------------------------")
                    askRegister = True
                    userExists = True
                    break

            if userExists==False:
                idRange = max([u["id"] for u in dbList], default=0) + 1
                id = idRange
                info = {
                    "name": name,
                    "password": password,
                    "phone number": phoneNumber,
                    "gender": gender,
                    "age": age,
                    "city": city,
                    "id": id,
                    "currentBalance": currentBalance
                }
                dbList.append(info)
                with open("data.json", "w") as file:
                    json.dump(dbList, file, indent=2)
                print("your register done successfully, your id is " + str(id))
                print("=================================================================")

                asking = False
                while asking == False:
                    ask = input("Do you want [1] Back to home page  [2] new register: ")
                    print("------------------------------------------------------------------")
                    if ask == "1":
                        askRegister = True
                        asking = True
                        break
                    elif ask == "2":
                        asking = True
                        break
                    else:
                        print("invalid choose only ([1] Back to home page  [2] new register ):")
                        print("----------------------------------------------------------------")
    else:
        print("invalid choose only ([1] login  [2] new register ): ")
        print("---------------------------------------------------------")
