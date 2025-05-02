import os
import sys

"""
def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

for value in my_generator(3):
    print(value)

squares_generator = (i*i for i in range(5))
for i in squares_generator:
    print(i)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x

def square(nums):
    for num in nums:
        yield num ** 2

print(sum(square(fibonacci_numbers(10))))
"""


def print_long_lines(filenames):
    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                if len(line.strip()) > 40:
                    print(line.strip())

def find_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def count_python_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                count += 1
    return count

def total_lines_in_python_files(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    total_lines += sum(1 for _ in f)
    return total_lines

def total_code_lines(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            total_lines += 1
    return total_lines

def main():
    while True:
        print("\n1. Print lines longer than 40 characters from files")
        print("2. List all files in directory recursively")
        print("3. Count Python files in directory")
        print("4. Count total lines in Python files")
        print("5. Count non-empty, non-comment lines in Python files")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            files = input("Enter file paths separated by spaces: ").split()
            print_long_lines(files)
        elif choice == '2':
            directory = input("Enter directory path: ")
            files = find_files(directory)
            for f in files:
                print(f)
        elif choice == '3':
            directory = input("Enter directory path: ")
            print(count_python_files(directory))
        elif choice == '4':
            directory = input("Enter directory path: ")
            print(total_lines_in_python_files(directory))
        elif choice == '5':
            directory = input("Enter directory path: ")
            print(total_code_lines(directory))
        elif choice == '6':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()