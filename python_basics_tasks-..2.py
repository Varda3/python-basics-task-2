"""Python basics practice: strings, lists, dictionaries, and sets."""


def strings_demo() -> None:
    print("=== Strings ===")

    full_name = "John" + " " + "Doe"  # string concatenation
    print(full_name)

    language = "Python"
    version = 3.9
    print(f"I am learning {language} version {version}.")  # string formatting

    text = " Hello python world "
    print(text.strip())  # remove leading and trailing whitespace
    print(text.upper())  # convert to uppercase
    print(text.lower())  # convert to lowercase


def lists_demo() -> None:
    print("\n=== Lists ===")

    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits: {fruits}")
    print(f"First fruit: {fruits[0]}")  # accessing an element
    print(f"Last fruit: {fruits[-1]}")  # accessing the last element
    print(f"Slice (first two): {fruits[0:2]}")  # slicing

    fruits[1] = "orange"  # modifying an element
    print(f"Modified fruits: {fruits}")

    fruits.append("grape")  # adding an element
    fruits.insert(1, "kiwi")  # inserting at a specific position
    print(f"Fruits after adding: {fruits}")

    fruits.remove("apple")  # removing an element by value
    popped_fruit = fruits.pop()  # removing the last element and storing it
    print(f"Fruits after removing: {fruits}. Popped fruit: {popped_fruit}")


def sets_demo() -> None:
    print("\n=== Sets ===")

    numbers = {1, 2, 3, 2, 4}
    print(f"Numbers set: {numbers}")  # duplicates are removed automatically

    numbers.add(5)  # adding an element
    print(f"Numbers after adding 5: {numbers}")

    numbers.remove(1)  # removing an element
    print(f"Numbers after removing 1: {numbers}")

    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    print(f"Union: {set_a.union(set_b)}")
    print(f"Intersection: {set_a.intersection(set_b)}")
    print(f"Difference (a - b): {set_a.difference(set_b)}")


def dictionaries_demo() -> None:
    print("\n=== Dictionaries ===")

    # Example 1: Sara
    student_sara = {"name": "Sara", "id": 123, "grade": 85}
    print(student_sara["name"])  # accessing values
    print(student_sara["id"])
    print(student_sara["grade"])

    student_sara["age"] = 21  # adding a new key-value pair
    student_sara["grade"] = 90  # modifying an existing value
    del student_sara["id"]  # deleting a key-value pair
    print(student_sara)

    # Example 2: Bob
    student_bob = {"name": "Bob", "age": 22, "major": "Computer Science"}
    print(f"Student info: {student_bob}")
    print(f"Student name: {student_bob['name']}")

    student_bob["age"] = 23  # modifying a value
    student_bob["gpa"] = 3.8  # adding a new key-value pair
    print(f"Updated student info: {student_bob}")

    for key, value in student_bob.items():  # looping over key-value pairs
        print(f"{key}: {value}")


def main() -> None:
    strings_demo()
    lists_demo()
    sets_demo()
    dictionaries_demo()


if __name__ == "__main__":
    main()
