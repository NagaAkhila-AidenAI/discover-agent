# Linear Search Algorithm

def linear_search(arr, target):
    """
    Performs a linear search to find a target value in a list.
    
    Args:
        arr: List of elements to search
        target: Element to search for
    
    Returns:
        Index of the target if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Finds all occurrences of a target value in a list.
    
    Args:
        arr: List of elements to search
        target: Element to search for
    
    Returns:
        List of indices where target is found, or empty list if not found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


def linear_search_object(arr, key, value):
    """
    Performs a linear search on a list of dictionaries.
    
    Args:
        arr: List of dictionaries
        key: Dictionary key to search
        value: Value to match
    
    Returns:
        Index of the matching dictionary, or -1 if not found
    """
    for i in range(len(arr)):
        if arr[i].get(key) == value:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    # Test with a simple list
    numbers = [45, 23, 67, 12, 89, 34, 56, 78]
    target = 34
    
    print(f"Array: {numbers}")
    print(f"Searching for: {target}")
    result = linear_search(numbers, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")
    
    # Test finding all occurrences
    print("\n--- Finding All Occurrences ---")
    numbers2 = [1, 2, 3, 2, 4, 2, 5]
    target2 = 2
    print(f"Array: {numbers2}")
    print(f"All indices of {target2}: {linear_search_all(numbers2, target2)}")
    
    # Test with list of dictionaries
    print("\n--- Search in Objects ---")
    students = [
        {'name': 'Alice', 'id': 101},
        {'name': 'Bob', 'id': 102},
        {'name': 'Charlie', 'id': 103},
        {'name': 'Diana', 'id': 104}
    ]
    
    idx = linear_search_object(students, 'name', 'Bob')
    if idx != -1:
        print(f"Found student at index {idx}: {students[idx]}")
    else:
        print("Student not found")
