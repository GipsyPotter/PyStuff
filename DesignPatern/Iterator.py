# Cung cấp một cách để truy cập các phần tử của một đối tượng tổng hợp một cách công bằng mà không tiết lộ đại diện cơ bản của nó.
# Alot of way to travel in HCM city
def inBuilt_Iterator1():
    alphabets = [chr(i) for i in range(65, 91)]
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


def inBuilt_Iterator2():
    alphabets = [chr(i) for i in range(97, 123)]
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


if __name__ == "__main__":
    inBuilt_Iterator1()
    inBuilt_Iterator2()
