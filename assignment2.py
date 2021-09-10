from socket import socket, AF_INET, SOCK_STREAM

class Assignment2:
    def __init__(self, age: int):
        self.age = age
        
    def tellBirthYear(self, currentYear: int):
        birthYear = currentYear - self.age
        print("Your birth year is " + str(birthYear))

    def listAnniversaries(self, n: int):
        anniversaries = []
        year = n
        while year <= self.age:
            anniversaries.append(year)
            year += n
        return anniversaries

    def modifyAge(self, n: int):
        ret1 = str(self.age * n)
        ret2 = str(self.age)[0] * n
        ret3 = str(self.age ** n)[0::2]
        return ret1 + ret2 + ret3

    def checkGoodString(string: str):
        hasNum = False
        for char in string:
            if char.isnumeric():
                hasNum = True
                break
        return len(string) >= 8 and string[0].islower() and hasNum
    
    def connectTcp(host: str, port: int):
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect((host, port))
        except:
            return False
        s.close()
        return True
