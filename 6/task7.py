import shelve

with shelve.open("mydata.db") as db:
    db["name"] = "Nguyen"
    db["age"] = 30
    db["email"] = "someone@gmail.com"

with shelve.open("mydata.db") as db:
    value = db["name"]
    print("Значение по ключу 'name':", value)
