# task 1, setup the class for the project
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget

# task 2, write getter and setters
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name
    def set_budget(self, new_budget):
        self.__budget = new_budget
        new_budget >= 0
    def get_budget(self):
        self.__budget = 1000
        return self.__budget
    
# task 3, Add budget functionality
    def add_budget(self, amount):
        self.budget = amount
        print(f"You spent ${amount}")
    
    # task 4, display budget
    def display_budget(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__budget}")
        print(f"Your remaining amount: {self.__budget - self.budget}")


food_category = BudgetCategory("Food", 1000)
food_category.add_budget(100)
food_category.display_budget()