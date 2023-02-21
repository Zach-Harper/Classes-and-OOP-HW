import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the 
# transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
order_total = 0

customerid = 569    
name = 'Dannie Sellyar'
address = '97 Mitchell Way HewittTexas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
member_status = True

customer = fc.Customer(customerid,name,address,email,phone,member_status)

list = []
for k in dict.keys():
    if dict[k][3] == customerid:
        list.append(k)
total_cost = 0
for i in list:
    date = dict[i][0]
    item = dict[i][1]
    cost = dict[i][2]
    customerid = dict[i][3]
    transaction = fc.Transaction(date, item,cost,customerid)
    total_cost += transaction.calc_total()

print('Customer Name:',name)
print('Phone:',phone)
for i in list:
    print('Order item',dict[i][1], 'Price:',dict[i][2])
print('Total Cost:','$',total_cost)
if member_status is True:
    print('Member Discount',.2*total_cost)
    print('Total Cost After Discount:',.8*total_cost)
else:
    pass

