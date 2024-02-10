def main():
    print("Доброго дня. Почнемо введення даних.")
    data = get_user_input()
    mounth_true = validate_month(mounth=data[1])
    year_true = validate_year(year=data[2])
    if mounth_true and year_true:
        create_texst_file(data)
    else:
        print("Ви ввели невалідний рік народження або місяць.\nПерезапуск програми.\n.\n.\n.")
        reload_prog()


def reload_prog():
    main()


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
    mounth = input("введіть місяць в якому ви народилися> ").capitalize()
    year = int(input("введіть рік свого народження> "))
    return [name, mounth, year]


def create_texst_file(data):
    file = open("testFile.txt", 'w')
    file.write(f'{data[1]}\n{data[2]}\n{data[3]}')
    print("Гаррі нас розсекретили вшиваймося!")



if __name__ == '__main__':
    main()

