# Запрашиваем у пользователя информацию о наличии водительского удостоверения
has_driving_license = input("У вас есть водительское удостоверение? (да/нет): ").strip().lower()

# Проверяем условие и выводим соответствующее сообщение
if has_driving_license == 'да':
    print("Поздравляем! Вы можете арендовать машину.")
elif has_driving_license == 'нет':
    print("Извините, вам необходимо водительское удостоверение для аренды машины.")
else:
    print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")
