def perform_list_operations():
    """
    Performs a series of specified operations on a list and prints the results.
    """
    print("--- List Operations ---")

    # 1. Create an empty list called my_list.
    my_list = []
    print(f"1. Initial empty list: {my_list}")

    # 2. Append the following elements to my_list: 10, 20, 30, 40.
    my_list.extend([10, 20, 30, 40])
    print(f"2. After appending elements: {my_list}")

    # 3. Insert the value 15 at the second position in the list.
    # The second position corresponds to index 1.
    my_list.insert(1, 15)
    print(f"3. After inserting 15 at the second position: {my_list}")

    # 4. Extend my_list with another list: [50, 60, 70].
    my_list.extend([50, 60, 70])
    print(f"4. After extending with another list: {my_list}")

    # 5. Remove the last element from my_list.
    my_list.pop()
    print(f"5. After removing the last element: {my_list}")

    # 6. Sort my_list in ascending order.
    my_list.sort()
    print(f"6. After sorting in ascending order: {my_list}")

    # 7. Find and print the index of the value 30 in my_list.
    index_of_30 = my_list.index(30)
    print(f"\n7. The index of the value 30 is: {index_of_30}")


if __name__ == "__main__":
    perform_list_operations()