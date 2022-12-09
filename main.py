def get_text():
    with open("text.txt", "r") as f:
        a = f.readlines()
        for i1, i in enumerate(a):
            if "\n" in i:
                a[i1] = i[:-1]
        return a


def ans(text, a, b):
    status = False
    for i1, i in enumerate(text):
        text[i1] = i.split(" ")

    for i in range(len(text)):
        for k in range(len(text[i])):
            if text[i][k] == a:
                text[i][k] = b
                status = True

    if status:
        with open("text.txt", "w") as f:
            for i in text:
                for k in i:
                    f.write(k + " ")
                f.write("\n")
        print("зміни було виконано успішно")
    else:
        print("слово не було знайдено")


def ui():
    a = input("введіть слово яке потрібно замінити")
    b = input("введіть слово на яке потрібно замінити")
    ans(get_text(), a, b)




def main():
    ui()


main()
