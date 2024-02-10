def main():
    print("Доброго дня. Почнемо введення даних.")
    data = get_user_input()
    year_true = validate_month(mounth=data[1])


def validate_month(mounth):
    mounths = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
    if mounth in mounths:
        return True
    else:
        return False


def validate_year(year):
    if year < 1904 or year > 2019:
        return False
    else:
        return True


def get_user_input():
    name = input("введіть своє прізвище та ім'я> ")
    mounth = input("введіть місяць в якому ви народилися> ")
    year = input(int("введіть рік свого народження> "))
    return [name, mounth, year]


def create_test_file():
    pass

