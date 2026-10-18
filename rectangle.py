def area(length, width):
    return length * width


def perimeter(length, width):
    return 2 * (length + width)


if __name__ == "__main__":
    length = float(input("Введите длину: "))
    width = float(input("Введите ширину: "))

    print("Площадь:", area(length, width))
    print("Периметр:", perimeter(length, width))