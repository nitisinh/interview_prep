"""
Quick list practice (5-minute exercise file).
Run this file and try different options.
"""

my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

def show_basics(data):
    print("\nHello World")
    print("Current list:", data)
    print("Iterate using index:")
    for i in range(len(data)):
        print(f"index {i} -> {data[i]}")
    print("Iterate directly:")
    for value in data:
        print(value)
    print("sum:", sum(data))
    print("max:", max(data))
    print("min:", min(data))
    print("length:", len(data))
    print("count of 1:", data.count(1))


def run_operation(choice, data):
    if choice == "1":
        value = int(input("Enter value to append: "))
        data.append(value)
    elif choice == "2":
        index = int(input("Enter index: "))
        value = int(input("Enter value: "))
        data.insert(index, value)
    elif choice == "3":
        value = int(input("Enter value to remove: "))
        data.remove(value)
    elif choice == "4":
        removed = data.pop()
        print("Popped value:", removed)
    elif choice == "5":
        data.sort()
    elif choice == "6":
        data.sort(reverse=True)
    elif choice == "7":
        data.reverse()
    elif choice == "8":
        n = int(input("Enter multiplier for each element: "))
        data[:] = [x * n for x in data]
    elif choice == "9":
        data[:] = [x for x in data if x % 2 == 0]
    elif choice == "10":
        start = int(input("Slice start index: "))
        end = int(input("Slice end index: "))
        print("Slice result:", data[start:end])
    else:
        print("Invalid choice")
        return
    print("Updated list:", data)


if __name__ == "__main__":
    show_basics(my_list)

    print("\nChoose one operation:")
    print("1. append")
    print("2. insert")
    print("3. remove")
    print("4. pop")
    print("5. sort ascending")
    print("6. sort descending")
    print("7. reverse")
    print("8. multiply all elements")
    print("9. keep only even numbers")
    print("10. slicing")

    selected = input("Enter choice (1-10): ").strip()
    run_operation(selected, my_list)
