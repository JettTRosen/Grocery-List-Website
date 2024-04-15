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

    # Adds a new item with specified parameters to list, updates dictionary with individual costs
    def push_back(self, name, price, quantity, customer_vec):
        item = self.item(name, price, quantity, customer_vec)
        self.items.append(item)
        itemTotal = (price * quantity * (1 + self.tax))
        self.total += itemTotal
        individual_cost = itemTotal / len(customer_vec)
        for customer in customer_vec:
            self.customer_dict[customer] += ceil(individual_cost * 100) / 100.0
    
    #Removes last item on list and takes away cost from customers
    def pop_back(self):
        item = self.items[-1]
        individual_cost = item.price / len(item.customer_vec)
        for customer in item.customer_vec:
            self.customer_dict[customer] -= ceil(individual_cost * 100) / 100.0
        self.items.pop()

    # Removes item on list at specified index, defaults to first term
    # Requires valid index for defined behavior
    def pop(self, index = 0):
        item = self.items[index]
        individual_cost = item.price / len(item.customer_vec)
        for customer in item.customer_vec:
            self.customer_dict[customer] -= ceil(individual_cost * 100) / 100.0
        self.items.pop(index)
        