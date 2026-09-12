# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем


def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """

    system_info = {
        "student_name": "Шустов Степан Михайлович",
        "academic_group": "ИВТИИбд-12",
        "github_link": "https://github.com/stepanshustov/ots_practice_2026"
    }
    return system_info


if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
