# class Car:

#     count = 0

#     def __init__(self, name=None, model=None):
#         print("not called ")

#     def __init__(self, name=None, model=None):
#         self.name = name
#         self.model = model
#         self.engine_started = False
#         Car.count += 1 

#     def start(self):
#         self.engine_started = True
#         print(f"The {self.name} {self.model} has started.")

#     def show_car(self):
#         print(f"Car Name: {self.name}")
#         print(f"Car Model: {self.model}")
#         print(f"Engine Status: {self.engine_started}")
#         print(f"Total Cars Created: {Car.count}")


# c1 = Car(name="feraria", model="v2")

# c1.start()

# print(c1.engine_started)

# c1.show_car()

# c2 = Car(name="BMW", model="3 Series")

# c2.show_car()

# print(getattr(c2, 'name'))
# setattr(c2, 'name', 'alto')
# print(getattr(c2, 'name'))
# print(hasattr(c2, 'model'))  
# # deletes the attribute age  
# delattr(c2, 'model')  
# print(getattr(c2, 'model'))



# 1	__dict__	It provides the dictionary containing the information about the class namespace.
# 2	__doc__	It contains a string which has the class documentation
# 3	__name__	It is used to access the class name.
# 4	__module__	It is used to access the module in which, this class is defined.
# 5	__bases__	It contains a tuple including all base classes.


class Account:

    total_accounts = 0

    def __init__(self, name=None, acc_no=None, amount=0):
        self.name = name
        self.acc_no = acc_no
        self.amount = amount
        Account.total_accounts += 1  # Increment the class variable, not the instance variable

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            print(f"Withdrawal of {amount} successful")

    def check_balance(self):
        print(f"Balance: {self.amount}")

    def display_account(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Balance: {self.amount}")

    @staticmethod
    def get_total_accounts():
        return Account.total_accounts


# Testing the Account class
a1 = Account(name="shrey", acc_no="123")
a1.display_account()
a1.deposit(5000)
a1.check_balance()
a1.withdraw(2000)
a1.check_balance()
a1.withdraw(4000)
a1.name = "sonu"
a1.display_account()

# Creating a second account
a2 = Account(name="shreya", acc_no="124")

# Getting the total number of accounts
total = Account.get_total_accounts()  # Access via class or instance
print(total)  # Output: 2



    