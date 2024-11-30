class User:
    def __init__(self, first_name, last_name):
        self.user_first_name = first_name
        self.user_last_name = last_name

    def get_one_name(self):
        return self.user_first_name

    def get_two_name(self):
        return  self.user_last_name

    def info(self):
        return f'Имя: {self.user_first_name}, Фамилия: {self.user_last_name}'

get_info = User('Евгений', 'Геранин')

print(get_info.get_one_name())
print(get_info.get_two_name())
print(get_info.info())