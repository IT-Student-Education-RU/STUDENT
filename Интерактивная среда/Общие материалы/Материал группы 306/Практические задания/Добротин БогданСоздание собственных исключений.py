class NameError(Exception):
    pass


class AgeError(Exception):
    pass


class Animal:
    def __init__(self, name, age):
        if any(char.isdigit() for char in name):
            raise NameError("Имя не должно содержать чисел")
        self.name = name

        if not age.isdigit() or int(age) <= 0:
            raise AgeError("Ошибка:возраст не должен быть отрицательным или равен нулю")
        self.age = int(age)


# Пример использования исключений

try:
    name = input("Введите имя животного: ")
    age = input("Введите возраст животного: ")

    animal = Animal(name, age)

    print(f"Животное с именем {animal.name} и возрастом {animal.age}")
except NameError as e:
    print(f"NameError: {e}")

except AgeError as e:
    print(f"Ошибка: {e}")

except Exception as e:
    print(f"Ошибка: {e}")
    
input()