import os

if os.path.exists("identity_set.txt"): #Active Memory ,It Will Remind Your Previous Score!
    with open("identity_set.txt", "r") as file:
     saved_identities = file.read()
    print(f"Your Previous Saved Identities Are Stored IN .txt FIle!")
else:
    print("Welcome! No Previous Saved Identities found.")

class identity:
    def __init__(self, name, age, standard, hieght):
        self.name = name
        self.age = age
        self.standard = standard
        self.hieght = hieght

    def string(self):
        return f"\n==>{self.name} IDENTITY:\n\tName Is {self.name}\n\tAge Is {self.age}\n\tStandard Is {self.standard} Class Student\n\tHieght Is {self.hieght}"
    def info(self):
        print(self.string())


na = str(input("Enter Name:")).upper().strip()
ag = int(input("Enter Age:"))
st = str(input("Enter Standard:")).upper().strip()
hi = str(input("Enter Hieght (In-CM):")).upper().strip()
identity1 = identity(na ,ag ,st ,hi)

print("\nSaving the following details:")
identity1.info()

with open("identity_set.txt","a") as file:
 file.write(identity1.string())

 print("Successfully appended to identity_set.txt!")
