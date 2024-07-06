class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, level):
        if level in ['user', 'admin']:
            self._access_level = level
        else:
            raise ValueError("Invalid access level")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if self._access_level == 'admin':
            user_list.append(user)
        else:
            raise PermissionError("You do not have permission to add users")

    def remove_user(self, user_list, user_id):
        if self._access_level == 'admin':
            user_list[:] = [user for user in user_list if user.get_user_id() != user_id]
        else:
            raise PermissionError("You do not have permission to remove users")


# Пример использования:
users = []

# Создаем обычного пользователя
user1 = User(1, "Alice")
users.append(user1)

# Создаем администратора
admin1 = Admin(2, "Bob")

# Администратор добавляет нового пользователя
user2 = User(3, "Charlie")
admin1.add_user(users, user2)

# Выводим всех пользователей
for user in users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Администратор удаляет пользователя
admin1.remove_user(users, 1)

# Выводим всех пользователей после удаления
print("\nAfter removal:")
for user in users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")