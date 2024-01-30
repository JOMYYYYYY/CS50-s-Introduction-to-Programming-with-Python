class Resin:
    """
    the resin is used for water purification
    "name" is the specific type of the resin product
    "price" is the value or cost of money of the specific resin per liter
    "pollutant" is the type of source material that cause pollution
    "capacity" is the adsorption capacity of corresponding  pollutant per liter
    "strength" is the brief introduction of the advantage of the specific type of resin
    "case_projects" are successful projects implemented the specific type of resin

    temporarily there are only three types of resin available
    """

    def __init__(self, name, price=None, pollutant=None, capacity=None, strength=None, case_projects=None):
        self.name = name
        self.price = price
        self.pollutant = pollutant
        self.capacity = capacity
        self.strength = strength
        self.case_projects = case_projects

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_pollutant(self):
        return self.pollutant

    def get_ac(self):
        return self.capacity

    def get_strength(self):
        return self.strength

    def get_case_projects(self):
        return self.case_projects

    def set_name(self, name):
        # name_list = ["T-42", "CH-90", "A-62"]
        # if name not in name_list:
        #     raise ValueError("Invalid name of resin")
        self.name = name

    def set_parameters(self):
        if self.name == "T-42":
            self.price = 33
            self.pollutant = "ammonia nitrogen"
            self.capacity = 36
            self.strength = "Selective removal of ammonia nitrogen"
            self.case_projects = "T-42 case project 1"
        elif self.name == "CH-90":
            self.price = 125
            self.pollutant = "heavy metal"
            self.capacity = 150
            self.strength = "Selective removal of heavy metal"
            self.case_projects = "CH-90 case project 1"
        elif self.name == "A-62":
            self.price = 95
            self.pollutant = "nitrate"
            self.capacity = 12
            self.strength = "Selective removal of nitrate"
            self.case_projects = "A-62 case project 1"
        else:
            raise ValueError("Invalid name of resin")


def main():
    # let user input the name of the resin, if input content is not included, prompt again
    name_list = ["T-42", "CH-90", "A-62"]  # there are only three products available now.
    while True:
        try:
            resin_name = input("please input the name of the resin: ").strip()
            if resin_name in name_list:
                break
            else:
                print("this product has not been supported yet, please try another one.")
                print("here are what we support now:", *name_list)
                raise ValueError
        except ValueError:
            pass

    resin1 = Resin(resin_name)
    resin1.set_parameters()

    print(f"the {resin1.name} is used for dealing with the pollution of {resin1.pollutant}.")

    print("What is the flow rate of sewage that needs to be treated?")
    while True:  # make sure the user input a positive number, otherwise prompt again
        try:
            flow_rate = float(input("The unit is cubic meters per hour, please input the number here: "))
            if flow_rate > 0:
                break
            else:
                print("the flow rate must be a positive number, please input again!")
                raise ValueError
        except ValueError:
            pass

    print("what is the concentrations of the pollutants in the *incoming* polluted water?")
    while True:
        try:
            incoming_concentrations = float(input("The unit is milligrams per liter, please input the number here: "))
            if incoming_concentrations > 0:
                break
            else:
                print("the incoming concentrations of the pollutant must be a positive number, please input again!")
                raise ValueError
        except ValueError:
            pass

    print("what is the concentrations of the pollutants limit in the *outcome* of purified water?")
    while True:
        try:
            outcome_concentrations = float(input("The unit is milligrams per liter, please input the number here: "))
            if outcome_concentrations < 0:
                raise ValueError("smaller than zero")
            elif outcome_concentrations >= incoming_concentrations:
                raise ValueError("out is not less than in")
            else:
                break
        except ValueError as err:
            if str(err) == "smaller than zero":
                print("the outcome concentration number should be a positive number, please input again!")
            else:
                print("the limit should be smaller than the incoming concentration! please input again.")
            pass

    print("Do you want to have a view of the whole project? ")
    while True:
        try:
            flag = input('Press "a" for yes, "b" for No: ').strip().lower()
            if flag == "a" or flag == "b":
                break
            else:
                raise ValueError
        except ValueError:
            print('your input is not correct.')
            pass
    if flag == "a":
        print("_____here is what the whole project looks like:_____")
        print(f"the specific type of the resin is {resin1.name}")
        print(f"the pollutant that we are dealing with is {resin1.pollutant}")
        print(f"the capacity of {resin1.name} absorbing {resin1.pollutant} is {resin1.capacity} g/L")
        print(f"the price of the resin is ${resin1.price} per liter")
        print(f"by using {resin1.name} resin, we have make great cases like {resin1.case_projects}")
    else:
        pass

    print("based on the water flow rate, in and out condition, here are the cost and usage information:\n")

    usage_amount = count_usage_amount(incoming_concentrations, outcome_concentrations, flow_rate, resin1.capacity)
    print(f"the total amount of resin is {usage_amount:.2f}")

    price = count_price(resin1.price, usage_amount)
    print(f"the total price of resin is {price:.2f}")

    suggestion(price)


def count_usage_amount(incoming_concentrations, outcome_concentrations, flow_rate, capacity):
    delta_concentration = incoming_concentrations - outcome_concentrations
    return (delta_concentration * flow_rate * 1000) / capacity


def count_price(price, amount):
    return price * amount


def suggestion(cost):
    if cost <= 0:
        print("Invalid parameter")
        return None
    elif 0 < cost <= 10000:
        print("This is a C type project.")
        suggestion_text = "the suggestion content of C type project"
        print("the suggestion is: " + '"' + suggestion_text + '"')
        return "C"
    elif 100000 < cost <= 5000000:
        print("This is a B type project.")
        suggestion_text = "the suggestion content of B type project"
        print("the suggestion is: " + '"' + suggestion_text + '"')
        return "B"
    else:
        print("This is an A type project.")
        suggestion_text = "the suggestion content of A type project"
        print("the suggestion is: " + '"' + suggestion_text + '"')
        return "A"


if __name__ == "__main__":
    main()
