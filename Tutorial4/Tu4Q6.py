class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0.0
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price
    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: {self.price}")
mobile1 = Mobile()
mobile1.set_details("Apple", "iPhone 16", 1500000)
mobile1.display_details()
