class Customer:
    def __init__(self,customerid,name,address,email,phone,member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status
            

class Transaction:
    def __init__(self, date, item,cost,customerid):
        self.date = date
        self.item_name = item
        self.cost = cost
        self.customerid = customerid

    def calc_total(self):
        return self.cost