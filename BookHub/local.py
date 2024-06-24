import requests

api_url = 'http://127.0.0.1:5000/api/users'

new_user_data = {
    "login": "rasdavalka",
    "password": "123",
    "email": "new_user@example.com"
}

response = requests.post(api_url, json=new_user_data)

if response.status_code == 201:
    print("User added successfully!")
else:
    print("Failed to add user. Status code:", response.status_code)
