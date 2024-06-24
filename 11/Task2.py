import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Недопустимый формат JSON.")

def shop_info(shop):
    for item in shop:
        for key, value in item.items():
            print(f"{key.capitalize()}: {value}")
        print("")

file_path = "script.json"
shop = load_json(file_path)
shop_info(shop.get("products", []))

