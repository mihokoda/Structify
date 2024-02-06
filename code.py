def order_pairs(identifiers):
    """
    Initial sorting of identifiers. S1 follows that s1 < s2 < ... < sn, and that for each chord, si < ei. 
    S2 is the sequence with only the endpoints according to S1. 
    R1 = [s1, e1, s2, e2, ..., sn, en]
    R2 = [e1, e2, ..., en]

    Args:
        identifiers (list): List of identifiers in the format 's_x' or 'e_x'

    Returns:
        tuple: Contains four lists, S1 and S2 representing the , and R1 and R2 as reference sequences.
    """

    lst = []

    for ele in identifiers:
        lst.append(int(ele[2])) 

    pairs = {}
    for i in range(len(lst)):
        if lst[i] not in pairs.keys():
            pairs[lst[i]] = [i]
        else:
            pairs[lst[i]].append(i)
    
    sorted_items = sorted(pairs.items(), key=lambda item: item[1][0])
    sorted_dict = dict(sorted_items)

    S1 = [0] * len(lst)
    i = 1
    for k in sorted_dict.keys():
        S1[sorted_dict[k][0]] = i
        S1[sorted_dict[k][1]] = i
        i+=1
    
    occurrences = {}
    S2 = []
    for num in S1:
        occurrences[num] = occurrences.get(num, 0) + 1
        # Add the number to S2 if it's the second occurrence
        if occurrences[num] == 2:
            S2.append(num)


    R1 = []
    R2 = []
    for i in range(1, len(identifiers)//2+1):
        R1.append(i)
        R1.append(i)
        R2.append(i)

   
    return S1, S2, R1, R2
             






def merge_count_inversions(left, right, reference):
    """
    Merge two halves of a list while counting inversions with respect to a reference list.

    Args:
        left (list): The left half of the list.
        right (list): The right half of the list.
        reference (dict): Maps elements to their positions in the reference list.

    Returns:
        list: The merged list.
        int: The number of inversions.
    """

    merged = []
    inv_count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if reference[left[i]] <= reference[right[j]]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += (len(left) - i)  # All remaining elements in left are inversions
    
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count

def sort_count_inversions(arr, reference):
    """
    Sorts a list and counts the number of inversions with respect to a reference list using merge sort.

    Args:
        arr (list): The list to sort and count inversions.
        reference (dict): Maps elements to their positions in the reference list.

    Returns:
        list: The sorted list.
        int: The number of inversions.
    """
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = sort_count_inversions(arr[:mid], reference)
    right, right_inv = sort_count_inversions(arr[mid:], reference)
    merged, split_inv = merge_count_inversions(left, right, reference)

    total_inv = left_inv + right_inv + split_inv
    return merged, total_inv

def count_inversions(S, R):
    """
    Counts the number of inversions in S with respect to the order in R.
    
    Args:
        S (list): The list in which to count inversions.
        R (list): The reference list representing the correct order.
    
    Returns:
        int: The number of inversions in S with respect to R.
    """
    # Create a reference dictionary mapping elements of R to their positions
    reference = {elem: index for index, elem in enumerate(R)}

    # Sort S and count inversions with respect to the reference order in R
    _, inversions = sort_count_inversions(S, reference)
    
    return inversions


def count_intersection(radians, identifiers):
    S1, S2, R1, R2 = order_pairs(identifiers)
    inversions_S1_R1 = count_inversions(S1, R1)
    inversions_S2_R2 = count_inversions(S2, R2)
    return inversions_S1_R1 - 2*inversions_S2_R2


def run_tests(test_cases, test_function):
    """
    Runs a series of test cases through a specified test function and prints the results.

    Args:
        test_cases (dict): A dictionary where each key is a descriptive string for the test case,
                           and the value is a tuple containing input arguments and expected output.
        test_function (function): The function to tes

    """
    for description, (inputs, expected_output) in test_cases.items():
        print(f"Running: {description}")
        result = test_function(*inputs)
        assert result == expected_output, f"Test failed: Expected {expected_output}, got {result}"
        print("Test passed")

# Define test cases for the order_pairs function
test_cases = {
    "Test Case 1": (
        ([[0.78, 1.47, 1.77, 3.92], ['s_1', 's_2', 'e_1', 'e_2']], 1)
    ),  "Test Case 2": (
        ([[0.9, 1.3, 1.7, 2.92], ['s_1', 'e_1', 's_2', 'e_2']], 0)
    ),  "Test Case 3": (
        ([[0.1, 0.3], ['e_1', 's_1']], 0)
    ),  "Test Case 4": (
        ([[0.2, 0.4, 2.3, 2.9, 3.9, 3.93], ['s_2', 's_1', 'e_2', 'e_1', 's_3', 'e_3']], 1)
    ),  "Test Case 5": (
        ([[0.1, 0.33, 1.53, 1.69, 1.9, 2.11], ['s_1', 's_2', 'e_2', 's_3', 'e_1', 'e_3']], 1)
    ),  "Test Case 6": (
        ([[2.390762770335994, 4.496545111026571, 2.3265245799229475, 2.7901125426463507], ['s_1', 'e_2', 's_2', 'e_1']], 0)
    ),  "Test Case 7": (
        ([[2.390762770335994, 4.496545111026571, 2.3265245799229475, 2.7901125426463507], ['e_4', 's_3', 's_4', 'e_3', 'e_1', 's_2', 'e_2', 's_1']], 1)
    ),  "Test Case 8": (
        ([[2.390762770335994, 4.496545111026571, 2.3265245799229475, 2.7901125426463507], ['e_3', 'e_2', 's_1', 'e_4', 's_2', 's_4', 'e_1', 's_3']], 2)
    ),  "Test Case 9": (
        ([[2.390762770335994, 4.496545111026571, 2.3265245799229475, 2.7901125426463507], ['s_3', 'e_4', 'e_3', 'e_1', 's_2', 's_4', 'e_2', 's_1']], 3)
    ), 
    

}

run_tests(test_cases, count_intersection)
