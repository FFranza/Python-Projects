# Online Store Management
# Tasked with building a Online Store Management
# Objectives:
    # Product Class, Customer Class, Order Class, and Store Class.
# Dictionary variable for products
products_by_category =  {
    'electronics': [],
    'books': [],
    'clothing': [],
}
 
class Product:
    def __init__(self, product_id, product_name, product_price, product_quantity_in_stock, product_category):
        self.prid = product_id
        self.pname = product_name
        self.pprice = product_price
        self.pqis = product_quantity_in_stock
        self.pcty = product_category

        # Add to the product inine with category
        products_by_category[product_category].append(self)
    
    def get_product_info(self): # Allows calling for information from class abnd is used to keep currented updated information.
        return f"{self.prid} - {self.pname}, Price: ${self.pprice}, Stock: {self.pname}"

    def adding_qis(self, quantity):
        if quantity > 0: # Checks if value is applicable for adding products, disallows negative or non real numbers.
            self.qis += quantity
            print (f"Added {quantity} units to {self.pname} to the new stock. Current stock is: {self.pqis}")
        else:
            print ("Invalid amount, please recheck. Stock is not updated.")

    def sell(self, quantity):
        if 0 < quantity <= self.qis: # Checks if quantity can be sold if quantity is can be sold
            self.qis -= quantity
            print (f"Sold {quantity} units of {self.pname}. Current stock is {self.pqis}")
            return True
        elif quantity <= 0: # Checks if value can be reduced properply either by using proper values or stock is still present
            print ("Invalid quantity, stock has not been updated")
        else:
            print (f"Insufficient amount of quantity, {self.pname} has not be sold and stock has not been updated")

class Customer:
    def __init__(self, customer_id, customer_name, customer_join_date):
        self.cid = customer_id
        self.cname = customer_name
        self.cjd = customer_join_date
        self.history = []
    
    def add_to_purchase_history(self, item):
        self.history.append(item)

    def get_customer_info(self): # Return with customer information
        return f"Customer's name is: {self.cname} with the ID of: {self.cid}. Join date: {self.cjd}"