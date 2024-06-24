import pickle

user_info = {
    "name": "Nguyen Tung Lam",
    "age": 25,
    "email": "someone@gmail.com"
}

with open("user_info.pickle", "wb") as file:
    pickle.dump(user_info, file)

with open("user_info.pickle", "rb") as file:
    loaded_user_info = pickle.load(file)
    print("Содержимое файла:\n", loaded_user_info)
