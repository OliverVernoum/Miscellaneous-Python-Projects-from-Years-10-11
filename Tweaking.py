users = [
    ["Mike","Smith",24],
    ["John","Thompson",56],
    ["Mary","Field",19],
    ["Katie","Johnson",15],
    ["Olly","Vernoum",14],
    ["Max","Turner",14],
    ["Zach","Gartland",14],
    ["Ben","Gray",15],
    ["Bongani","Mudoti",14],
    ["Will","Coyle",14],
    ["Timmy","Carter",14],
    ["Olly","Johnson",15]
    ]


searchname = input("Please enter your first name: ")
for user in users:
    if user[1].lower() == searchname:

        foundat = users.index(user)
        print("Found at index: ",foundat)

        q = input ("Press (y) to delete this record: ")

        if q == "y":
            users.pop(foundat)
