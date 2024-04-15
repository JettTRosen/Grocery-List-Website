from math import ceil

class groceryList:
    class item:
        #ctor
        def __init__(self, name_in, price_in, quantity_in, customer_vec_in):
            self.name = name_in
            self.price = price_in
            self.quantity = quantity_in
            self.customer_vec = customer_vec_in

        def toString(self):
            return ("Name: " + self.name + " Price: $" + str(self.price) + " Quantity: " + str(self.quantity) + " Customers: " + " ".join(self.customer_vec) )

    #ctor
    def __init__(self, valid_customer_vec, tax_in):
        self.tax = tax_in
        self.customer_dict = {key: 0.0 for key in valid_customer_vec}
        self.items = []
        self.total = 0

    #Requires: valid inputs
    #Modifies: internal grocery list
    #Effects: adds a new item with specified parameters to list, updates dictionary with individual
    def push_back(self, name, price, quantity, customer_vec):
        item = self.item(name, price, quantity, customer_vec)
        self.items.append(item)
        itemTotal = (price * quantity * (1 + self.tax))
        self.total += itemTotal
        individual_cost = itemTotal / len(customer_vec)
        for customer in customer_vec:
            self.customer_dict[customer] += ceil(individual_cost * 100) / 100.0
    
    #Requires: non empty list
    #Modifies: internal grocery list
    #Effects: removes last item on list
    def pop_back(self):
        self.items.pop()

    #Requires: non empty list
    #Modifies: internal grocery list
    #Effects: removes item on list at specified index, defaults to first term
    def pop(self, index = 0):
        self.items.pop(index)
