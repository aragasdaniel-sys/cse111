def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # REVERSE LIST
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")

        # APPEND ORANGE
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")

        # INSERT CHERRY
        apple_index = fruit_list.index("apple")
        fruit_list.insert(apple_index, "cherry")
        print(f"insert cherry: {fruit_list}")

        # REMOVE BANANA
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        # POP ORANGE
        last = fruit_list.pop()
        print(f"pop {last}: {fruit_list}")

        # SORTED
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        # CLEARED
        fruit_list.clear()
        print(f"cleared: {fruit_list}")
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

if __name__ == "__main__":
    main()