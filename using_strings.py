import sys

RIGHT_COLUMN_WIDTH = 10

def main():
    my_list = [
        ('Paul', '37', 127.33),
        ('Ethan', '14', 1_732.48)
    ]
    print("BALANCE SHEET".center(50, '-'))
    for row in my_list:
        # print(row[0], row[1], row[2])
        print(f"{row[0]:<30}{row[1]:>5}{row[2]:>10}")
        # print("{0}|{1}|{2}".format(row[0], row[1], row[2]))
        # print("{name}%{age}%{bank_balance}".format(
        #     name=row[0],
        #     age=row[1],
        #     bank_balance=row[2]
        # ))
    print("-".center(50, '-'))
    print(f"{'Totals':<30}{51:>5}{1859.81:>10}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
