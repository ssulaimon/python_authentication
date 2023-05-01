import json


class UserModel:
    def __init__(self, firstName, lastName, userName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.email = email

    def createAccount(self,):
        dataBase = open("./user_data.json", "a")
        data = {"userName": self.userName,
                "fullName": f"{self.firstName} {self.lastName}", "password": self.password, "email": self.email}
        # Convert dictionary to json
        jsonFIle = json.dumps(data, indent=1)

        dataBase.write(f"{jsonFIle}")
        dataBase.close()
        print('User Account Created')

    def logintoAccount(self,):
        dataBased = open("./user_data.json")
        data = json.load(dataBased)
        count = 0
        userName = input("Please enter your userName: ")
        password = input("Please enter your password: ")

        while not (userName == data["userName"] or password == data["password"]):
            count += 1
            if count < 3:
                left = 3 - count
                print(f"You have {left} left")
                userName = input("Please enter your userName: ")
                password = input("Please enter your password: ")

            else:
                print("You are out of try. Account locked")
                break
