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

            Records.list_customers[customer.id] = customer

    def read_product():
        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product_data = line.split(',')

            product = Product(product_data[0].strip(), product_data[1].strip(
            ), product_data[2].strip(), product_data[3].strip())

            Records.list_products[product.id] = product

    def find_customer(id):
        customer = Records.list_customers[id]
        return customer
    
    def find_product(id):
        product = Records.list_products[id]
        return product
    
    def list_customers():
        for key,value in Records.list_customers:
            print("Customer id ",value[0])
            print("Customer name ",value[0])
            print("Customer id ",value[0])
            print("Customer id ",value[10])

    def list_products():
        for key,value in Records.list_products:
            print("Product id ",value[0])
            print("Customer name ",value[0])
            print("Customer id ",value[0])
            print("Customer id ",value[0])



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

        # based on need_prescription variable priscription is requested.
        need_prescription = False

        # Infinite while loop run until customer enter the correct products.
        while 1:
            customer_choosed_products = input(
                "Please enter the choosed products : ")
            customer_entered_products_array = customer_choosed_products.split(',')

            # based on correct_product_entered variable, while loop run until the valid products are entered.
            correct_product_entered = True

            for product in customer_entered_products_array:
                # Product validation is done below
                product = product.strip()
                if product not in products:
                    print(" "*20, "Invalid product: ", product +
                        " entered please re-enter the product")
                    correct_product_entered = False
                    # If a product is invalid product validation loop is breaked and customer is asked to re-enter the products
                    break

                # if a product is valid and product need a prescription, need_prescription variable is set to true
                if products[product][1] == 'Y':
                    need_prescription = True

            # if correct_product_entered is equal to False while loop is continued else breaked
            if not correct_product_entered:
                continue
            else:
                break

        # Based on the need_prescription variable prescription is requested from the customer
        if (need_prescription):

            # Until a valid input is provided while loop run
            while 1:
                # Customer input is validated below
                hasPrescription = input("Do you have doctor’s prescription : ")
                if hasPrescription == 'N':
                    print(" "*20, "Without a prescription this item cannot be purchased")
                    return
                if hasPrescription != 'Y':
                    print(
                        " "*20, "Value should be equal to Y or N. Please enter a valid value")
                    continue
                # if the input is valid then the while loop is breaked
                break

        while 1:
            # Based on valid_product_quantity_entered varible while loop is continued
            valid_product_quantity_entered = True
            try:
                productQuantities = input(
                    "Please enter quantity of the product : ")
                product_quantity_list = str(productQuantities).split(',')

                # Validated whether number of products match with number of quantites.
                if len(customer_entered_products_array) != len(product_quantity_list):
                    print(" "*20,
                        "Quantity count should be equal to products count. Please re enter quantites")
                    continue

                # Validated quantiy is int and greater than 0
                for product_quantity in product_quantity_list:
                    if int(product_quantity.strip()) <= 0:
                        print(
                            " "*20, "Value can't be less than one. Please enter a valid value")
                        # If a quantity is not greter than 0 validation loop is breaked.
                        valid_product_quantity_entered = False
                        break
                # if Invalid quantity is entered while loop is continued until customer enter vlid quantities
                if not valid_product_quantity_entered:
                    continue
            # if invalid value is entered the error is hanled and while loop is continued.
            except ValueError:
                print(" "*20, "Value must be a integer. Please enter valid value")
                continue
            # if all the quantities are valid while loop is breaked.
            break

        # Unit price and total cost is calculated in the below logic
        bil_details = {}
        n = 0
        totalCost = 0.0
        # for each product unit cost is calculated based on that total cost is calculated
        for product in customer_entered_products_array:
            unit_price = products[product.strip()][0]
            productQuantity = int(product_quantity_list[n])
            totalCost = totalCost + productQuantity*unit_price
            # calclated unit price and product details are stored in bil_details dictionary
            bil_details[product] = [unit_price, productQuantity]

            n += 1

        # Reward point is calculated baased on total cost before the deduction
        current_order_rewardPoints = round(totalCost)

        # If customer already exists new reward point is added to the previous reward point
        if customerName in customers:
            customers[customerName] += current_order_rewardPoints
        else:
            # If a customer is new then a new record is created
            customers[customerName] = current_order_rewardPoints

        # Total cost and discount points are calculated in the below logic
        # If the customer's reward point before the current order is greater than 100 then customer is eligible for discount
        if customers[customerName] - current_order_rewardPoints > 100:
            custReward = customers[customerName] - current_order_rewardPoints
            discountPoints = (custReward//100) * 100
            totalCost = totalCost - discountPoints/10
            customers[customerName] -= discountPoints

        # The bill is printed below
        print(" "*20, "-"*40)
        print(" "*20, " "*15 + "Recipt")
        print(" "*20, "-"*40+"\n")
        print(" "*20, "Name:" + " "*20, customerName, "\n")

        for key, value in bil_details.items():
            print(" "*20, "Product:" + " "*17, key)
            print(" "*20, "Unit Price:" + " "*14, value[0])
            print(" "*20, "Quantity:" + " "*16, value[1], "\n")
        print(" "*20, "-"*40)
        print(" "*20, "Total cost:" + " "*14, round(totalCost, 2))
        print(" "*20, "Earned reward:" + " "*11, customers[customerName], "\n")

        # Bill details are persited in the final_bill dictionary to use in print previous order functionality.

        # final bill has the following data structure.
        # final_bill ={"Customer_name":[{Product_1:Unit_price,Quantity},{Product_2:Unit_price,Quantity},{Details:total_cost,reward_poitns}],  --Order1
        #                              [{Product_1:Unit_price,Quantity},{Details:total_cost,reward_poitns}],                                  --Order2
        #                              [{Product_1:Unit_price,Quantity},{Product_2:Unit_price,Quantity},{Details:total_cost,reward_poitns}],} --Order3

        # If customer already exits in the list new order details are apended  if not new record is created.
        if customerName in final_bill:
            final_bill[customerName].append([
                bil_details, {"Details": [totalCost, customers[customerName]]}])
        else:
            final_bill[customerName] = [[bil_details, {
                "Details": [totalCost, customers[customerName]]}]]
         
        


    




    
