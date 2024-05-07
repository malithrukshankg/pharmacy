class Customer:

    def __init__(self, id, name, reward):
        if not name.stip().isalpha():
            raise ValueError(
                "Name should only contain alphabetic characters please enter correct name")

        self.name = name
        self.id = id
        self.reward = reward

    def get_reward(self):
        pass

    def get_discount(self):
        pass

    def update_reward(self):
        pass

    def display_info(self):
        pass


class BasicCustomer(Customer):

    reward_rate = 100

    def __init__(self, id, name, reward):
        super().__init__(id, name, reward)

    def set_reward_rate(cls, new_rate):
        cls.reward_rate = new_rate

    def get_reward_rate(cls):
        return cls.reward_rate

    def get_reward(self, total_cost):
        return round(total_cost * BasicCustomer.reward_rate/100)

    def update_reward(self, value):
        self.reward += value

    def display_info(self):
        print(f"Customer ID: {self.ID}, Customer Name: {self.name}, Customer Reward Points: {
              self.reward}, Customer Reward Rate: {BasicCustomer.reward_rate}%")


class VIPCustomer(Customer):
    def __init__(self, ID, name, reward_rate=1.0, discount_rate=0.08):
        super().__init__(ID, name, 0)
        self.reward_rate = reward_rate
        self.discount_rate = discount_rate

    def get_discount(self, total_cost):
        return total_cost * self.discount_rate

    def get_reward(self, total_cost):
        discounted_cost = total_cost - self.get_discount(total_cost)
        return round(discounted_cost * self.reward_rate)

    def update_reward(self, value):
        self.reward += value

    def display_info(self):
        print("ID:", self.ID)
        print("Name:", self.name)
        print("Reward Rate:", self.reward_rate)
        print("Discount Rate:", self.discount_rate)

    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate

    @staticmethod
    def set_reward_rate(rate):
        VIPCustomer.reward_rate = rate


class Product:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def display_info(self):
        print("ID:", self.ID)
        print("Name:", self.name)
        print("Price:", self.price)


class Order:

    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def compute_cost(self):
        self.total_cost = self.quantity * self.product.price
        self.discount = self.customer.get_discount(self.total_cost)
        self.reward = self.customer.get_reward(self.total_cost)


class Records:
    list_customers = {}
    list_products = {}

    def read_customer():
        with open("customers.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            customer_data = line.split(',')
            if customer_data[0].startswith('V'):
                customer = BasicCustomer(customer_data[0].strip(), customer_data[1].strip(
                ), customer_data[3].strip())
            else:
                customer = VIPCustomer(customer_data[0].strip(), customer_data[1].strip(
                ), customer_data[3].strip(), customer_data[4].strip())

            Records.list_customers[customer.name] = customer

    def read_product():
        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product_data = line.split(',')

            product = Product(product_data[0].strip(), product_data[1].strip(
            ), product_data[2].strip(), product_data[3].strip())

            Records.list_products[product.name] = product

    def find_customer(id):
        customer = Records.list_customers[id]
        return customer

    def find_product(id):
        product = Records.list_products[id]
        return product

    def list_customers():
        for key, value in Records.list_customers:
            print("Customer id ", value[0])
            print("Customer name ", value[0])
            print("Customer id ", value[0])
            print("Customer id ", value[10])

    def list_products():
        for key, value in Records.list_products:
            print("Product id ", value[0])
            print("Customer name ", value[0])
            print("Customer id ", value[0])
            print("Customer id ", value[0])


class Operations:

    def __init__(self):
        self.records = Records()
        self.records.read_customer()
        self.records.read_product()

    def display_customers(self):
        self.records.list_customers()

    def display_products(self):
        self.records.list_products()

    def menu():
        print(" "*25, "Welcome to the RMIT pharmacy!")
        print(" "*20, "#"*40)
        print(" "*20, "You can choose from the following options:")
        print(" "*20, "1:   Make a purchase")
        print(" "*20, "2:   Add/update information of a product")
        print(" "*20, "3:   Display existing customers")
        print(" "*20, "4:   Display existing products")
        print(" "*20, "5:   Display order history")
        print(" "*20, "0:   Exit the program")
        print(" "*20, "#"*40)

        try:
            choosed_option = int(input(" "*21 + "Choose one option : "))
        except ValueError:
            print("Wrong value enterted please enter a correct value")

    def purchase():
        # Infinite while loop run until customer enter the correct name.
        while 1:
            customerName = input("Please enter name of the customer : ")

            # customer name validation.
            if not customerName.isalpha():
                print(" "*20, "Invalid name entered please re-enter the name")
                continue
            else:
                break

        while 1:
            product = input("Please enter the choosed product : ")

            product = product.strip()

            if product not in Records.list_products:
                print(" "*20, "Invalid product: ", product +
                      " entered please re-enter the product")
            else:
                break

        while 1:
            try:
                productQuantity = int(input(
                    "Please enter quantity of the product : "))

                if int(productQuantity) <= 0:
                    print(
                        " "*20, "Value can't be less than one. Please enter a valid value")
                else:
                    break

            except ValueError:
                print(" "*20, "Value must be a integer. Please enter valid value")
                continue

        product = Product(Records.list_products[product])

        unit_price = product.price
        productQuantity = productQuantity
        totalCost = productQuantity*unit_price

        # Reward point is calculated baased on total cost before the deduction
        current_order_rewardPoints = round(totalCost)

        # If customer already exists new reward point is added to the previous reward point
        if customerName in Records.list_customers:
            customer = Records.list_customers[customerName]
            customer.reward += current_order_rewardPoints
        else:
            # If a customer is new then a new record is created
            Records.list_customers[customerName] = current_order_rewardPoints

        # The bill is printed below
        print(" "*20, "-"*40)
        print(" "*20, " "*15 + "Recipt")
        print(" "*20, "-"*40+"\n")
        print(" "*20, "Name:" + " "*20, customerName, "\n")
        print(" "*20, "Product:" + " "*17, product.name)
        print(" "*20, "Unit Price:" + " "*14, product.price)
        print(" "*20, "Quantity:" + " "*16, productQuantity, "\n")
        print(" "*20, "-"*40)
        print(" "*20, "Total cost:" + " "*14, round(totalCost, 2))
        print(" "*20, "Earned reward:" + " "*11,
              current_order_rewardPoints, "\n")
