names = ["Кирилушка", "Саня", "Никитушка"]
new_names = ["Алиса", "Катя"]

# Добавить новые имена в список
names.extend(new_names)

# Удалить последнее имя из списка
names.pop()

# Вывести финальный список на консоль
print("Выходной список:", names)
names = ["Никитушка", "Саня", "Банана"]
new_names = ["Алиса", "Кирилушка"]

# Добавить новые имена в список
names += new_names

# Удалить последнее имя из списка
names = names[:-1]

# Вывести финальный список на консоль
print("Выходной список:", names)

input()