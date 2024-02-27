
# instead of utilizing a function main() change this into a class since you are housing variables that is a list of many user objects
# take a lot of the functionality in the main() function and add it to your Property class
class Property:
    def __init__(self, name, down_payment, investment):
        self.name = name
        self.down_payment = down_payment
        self.investment = investment
        self.expenses = 0
        self.income = 0

    def add_expense(self, tax, mortgage, insurance):
        expense = tax + mortgage + insurance
        self.expenses += expense

    def add_income(self, rent, laundry, parking, pet_fee):
        base_income = rent + laundry + parking + pet_fee
        self.income += base_income

    def calculate_roi(self):
        # ROI = (Net Profit / Total Investment) x 100
        total_monthly_cashflow = self.income - self.expenses
        net_profit = total_monthly_cashflow * 12
        return_on_investment = (net_profit / self.investment) * 100
        return return_on_investment

class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

#class 
def change_user(users, user_name):
    user = next((u for u in users if u.name == user_name), None)
    if user:
        return user
    else:
        print(f"User '{user_name}' not found.")
        return None

# Change to: class Main:
# add run methodls

def main():
    users = []
    control_loop = True
    user = None

    while control_loop:
        print("\nRental Property ROI Calculator")
        print("1. Add User")
        print("2. Add Property")
        print("3. Change User")
        print("4. Check ROI")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter user name: ")
            user = User(user_name)
            users.append(user)
            print(f"User '{user_name}' created.")

        elif choice == "2":
            if user:
                property_name = input("Enter property name: ")
                down_payment = float(input("Enter property down_payment: "))
                property_investment = float(input("Enter total investment in the property: "))
                property = Property(property_name, down_payment, property_investment)
                user.add_property(property)
                print(f"Property '{property_name}' added to '{user.name}'.")
                print("\n Now, add the expenses and income to this property: ")
                print("Expenses...")
                input_tax = float(input("Add tax: "))
                input_mortgage = float(input("Add mortgage: "))
                input_insurance = float(input("Add insurance: "))
                net_expenses = input_tax + input_mortgage + input_insurance
                print("\nIncome...")
                input_rent = float(input("Add rent: "))
                input_laundry = float(input("Add laundry: "))
                input_parking = float(input("Add parking: "))
                input_pet_fee = float(input("Add pet fee: "))
                net_income = input_rent + input_laundry + input_parking + input_pet_fee
                #adding expenses to proprtty
                property.add_expense(input_tax, input_mortgage, input_insurance)
                #adding income to property
                property.add_income(input_rent, input_laundry, input_parking, input_pet_fee)
            else:
                print("Create a user first.")

        elif choice == "3":
            user_name = input("Enter user name: ")
            user = change_user(users, user_name)

        elif choice == "4":
            if user:
                property_name = input("Enter property name to check its ROI: ")
                for property in user.properties:
                    if property.name == property_name:
                        roi = property.calculate_roi()
                        print(f"ROI for '{property_name}': {roi:.2f}%")
                        break
                else:
                    print(f"Property '{property_name}' not found in '{user.name}'.")

        elif choice == "5":
            print("Exiting the program.")
            control_loop = False


    main()