# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания новой записи пользователя в системе
# содержат имя, телефон и адрес пользователя
user_body = get_user_body("Аа")
product_ids = {
    "ids": [1, 2, 3]
}
user_response = sender_stand_request.post_new_user(user_body)