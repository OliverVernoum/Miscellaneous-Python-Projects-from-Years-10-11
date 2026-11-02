"""
PYTHON ARRAYS (LISTS) TEST SHEET
=================================
A comprehensive guide to testing your knowledge of Python lists/arrays.
Run this file and all test cases will execute with PASS/FAIL results.
"""

# ============================================================================
# SECTION 1: BASIC ARRAY CREATION AND ACCESS
# ============================================================================

print("=" * 60)
print("SECTION 1: BASIC ARRAY CREATION AND ACCESS")
print("=" * 60)

# Test 1.1: Create a list with 5 numbers
print("\nTest 1.1: Create a list with numbers [10, 20, 30, 40, 50]")
numbers = [10, 20, 30, 40, 50]
print(f"List created: {numbers}")
print(f"Expected: [10, 20, 30, 40, 50]")
print(f"PASS" if numbers == [10, 20, 30, 40, 50] else "FAIL")

# Test 1.2: Access first element (index 0)
print("\nTest 1.2: Access first element")
first = numbers[0]
print(f"First element: {first}")
print(f"Expected: 10")
print(f"PASS" if first == 10 else "FAIL")

# Test 1.3: Access last element (using -1)
print("\nTest 1.3: Access last element using negative index")
last = numbers[-1]
print(f"Last element: {last}")
print(f"Expected: 50")
print(f"PASS" if last == 50 else "FAIL")

# Test 1.4: Find length of list
print("\nTest 1.4: Find length of list")
length = len(numbers)
print(f"Length: {length}")
print(f"Expected: 5")
print(f"PASS" if length == 5 else "FAIL")


# ============================================================================
# SECTION 2: SLICING
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 2: SLICING")
print("=" * 60)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Test 2.1: Slice first 3 elements
print("\nTest 2.1: Slice first 3 elements [0:3]")
slice1 = fruits[0:3]
print(f"Result: {slice1}")
print(f"Expected: ['apple', 'banana', 'cherry']")
print(f"PASS" if slice1 == ['apple', 'banana', 'cherry'] else "FAIL")

# Test 2.2: Slice from index 2 to end
print("\nTest 2.2: Slice from index 2 to end [2:]")
slice2 = fruits[2:]
print(f"Result: {slice2}")
print(f"Expected: ['cherry', 'date', 'elderberry']")
print(f"PASS" if slice2 == ['cherry', 'date', 'elderberry'] else "FAIL")

# Test 2.3: Slice every other element
print("\nTest 2.3: Slice every other element [::2]")
slice3 = fruits[::2]
print(f"Result: {slice3}")
print(f"Expected: ['apple', 'cherry', 'elderberry']")
print(f"PASS" if slice3 == ['apple', 'cherry', 'elderberry'] else "FAIL")

# Test 2.4: Reverse list
print("\nTest 2.4: Reverse list [::-1]")
slice4 = fruits[::-1]
print(f"Result: {slice4}")
print(f"Expected: ['elderberry', 'date', 'cherry', 'banana', 'apple']")
print(f"PASS" if slice4 == ['elderberry', 'date', 'cherry', 'banana', 'apple'] else "FAIL")


# ============================================================================
# SECTION 3: MODIFYING LISTS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 3: MODIFYING LISTS")
print("=" * 60)

# Test 3.1: Add element with append()
print("\nTest 3.1: Add 'yellow' to the end using append()")
colors = ["red", "blue", "green"]
colors.append("yellow")
print(f"Result: {colors}")
print(f"Expected: ['red', 'blue', 'green', 'yellow']")
print(f"PASS" if colors == ['red', 'blue', 'green', 'yellow'] else "FAIL")

# Test 3.2: Insert element at specific index
print("\nTest 3.2: Insert 'orange' at index 1")
colors.insert(1, "orange")
print(f"Result: {colors}")
print(f"Expected: ['red', 'orange', 'blue', 'green', 'yellow']")
print(f"PASS" if colors == ['red', 'orange', 'blue', 'green', 'yellow'] else "FAIL")

# Test 3.3: Remove element by value
print("\nTest 3.3: Remove 'blue' from list")
colors.remove("blue")
print(f"Result: {colors}")
print(f"Expected: ['red', 'orange', 'green', 'yellow']")
print(f"PASS" if colors == ['red', 'orange', 'green', 'yellow'] else "FAIL")

# Test 3.4: Pop (remove and return) last element
print("\nTest 3.4: Pop last element")
popped = colors.pop()
print(f"Popped: {popped}")
print(f"List after pop: {colors}")
print(f"Expected popped: 'yellow', List: ['red', 'orange', 'green']")
print(f"PASS" if popped == 'yellow' and colors == ['red', 'orange', 'green'] else "FAIL")

# Test 3.5: Change element at specific index
print("\nTest 3.5: Change element at index 0 to 'pink'")
colors[0] = "pink"
print(f"Result: {colors}")
print(f"Expected: ['pink', 'orange', 'green']")
print(f"PASS" if colors == ['pink', 'orange', 'green'] else "FAIL")


# ============================================================================
# SECTION 4: SEARCHING AND COUNTING
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 4: SEARCHING AND COUNTING")
print("=" * 60)

animals = ["cat", "dog", "cat", "bird", "cat", "fish"]

# Test 4.1: Find index of element
print("\nTest 4.1: Find index of 'dog'")
index = animals.index("dog")
print(f"Index: {index}")
print(f"Expected: 1")
print(f"PASS" if index == 1 else "FAIL")

# Test 4.2: Count occurrences of element
print("\nTest 4.2: Count how many times 'cat' appears")
count = animals.count("cat")
print(f"Count: {count}")
print(f"Expected: 3")
print(f"PASS" if count == 3 else "FAIL")

# Test 4.3: Check if element exists
print("\nTest 4.3: Check if 'bird' is in list")
exists = "bird" in animals
print(f"Result: {exists}")
print(f"Expected: True")
print(f"PASS" if exists == True else "FAIL")

# Test 4.4: Check if element does NOT exist
print("\nTest 4.4: Check if 'elephant' is NOT in list")
not_exists = "elephant" not in animals
print(f"Result: {not_exists}")
print(f"Expected: True")
print(f"PASS" if not_exists == True else "FAIL")


# ============================================================================
# SECTION 5: SORTING AND ORDERING
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 5: SORTING AND ORDERING")
print("=" * 60)

# Test 5.1: Sort numbers in ascending order
print("\nTest 5.1: Sort [5, 2, 8, 1, 9] in ascending order")
nums = [5, 2, 8, 1, 9]
nums.sort()
print(f"Result: {nums}")
print(f"Expected: [1, 2, 5, 8, 9]")
print(f"PASS" if nums == [1, 2, 5, 8, 9] else "FAIL")

# Test 5.2: Sort in descending order
print("\nTest 5.2: Sort [3, 7, 1, 9] in descending order")
nums2 = [3, 7, 1, 9]
nums2.sort(reverse=True)
print(f"Result: {nums2}")
print(f"Expected: [9, 7, 3, 1]")
print(f"PASS" if nums2 == [9, 7, 3, 1] else "FAIL")

# Test 5.3: Sort strings alphabetically
print("\nTest 5.3: Sort ['zebra', 'apple', 'mango'] alphabetically")
words = ["zebra", "apple", "mango"]
words.sort()
print(f"Result: {words}")
print(f"Expected: ['apple', 'mango', 'zebra']")
print(f"PASS" if words == ['apple', 'mango', 'zebra'] else "FAIL")

# Test 5.4: Get sorted list without modifying original
print("\nTest 5.4: Use sorted() to get new sorted list")
original = [5, 2, 8]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"Sorted: {sorted_list}")
print(f"Expected - Original unchanged: [5, 2, 8], Sorted: [2, 5, 8]")
print(f"PASS" if original == [5, 2, 8] and sorted_list == [2, 5, 8] else "FAIL")


# ============================================================================
# SECTION 6: LOOPING THROUGH LISTS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 6: LOOPING THROUGH LISTS")
print("=" * 60)

# Test 6.1: Simple for loop
print("\nTest 6.1: Loop through ['a', 'b', 'c'] and print each")
letters = ["a", "b", "c"]
print("Output:")
for letter in letters:
    print(f"  {letter}")
print("Expected: a, b, c (each on new line)")

# Test 6.2: Loop with index using enumerate()
print("\nTest 6.2: Loop with index using enumerate()")
print("Output:")
for i, letter in enumerate(letters):
    print(f"  Index {i}: {letter}")
print("Expected: Index 0: a, Index 1: b, Index 2: c")

# Test 6.3: Loop with range()
print("\nTest 6.3: Loop through indices using range()")
numbers = [10, 20, 30]
print("Output:")
for i in range(len(numbers)):
    print(f"  {numbers[i]}")
print("Expected: 10, 20, 30")


# ============================================================================
# SECTION 7: LIST OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 7: LIST OPERATIONS")
print("=" * 60)

# Test 7.1: Combine two lists
print("\nTest 7.1: Combine [1, 2] and [3, 4]")
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(f"Result: {combined}")
print(f"Expected: [1, 2, 3, 4]")
print(f"PASS" if combined == [1, 2, 3, 4] else "FAIL")

# Test 7.2: Repeat list
print("\nTest 7.2: Repeat [1, 2] three times")
repeated = [1, 2] * 3
print(f"Result: {repeated}")
print(f"Expected: [1, 2, 1, 2, 1, 2]")
print(f"PASS" if repeated == [1, 2, 1, 2, 1, 2] else "FAIL")

# Test 7.3: Clear list
print("\nTest 7.3: Clear a list")
temp_list = [1, 2, 3]
temp_list.clear()
print(f"Result: {temp_list}")
print(f"Expected: []")
print(f"PASS" if temp_list == [] else "FAIL")

# Test 7.4: Copy a list
print("\nTest 7.4: Create a copy of a list")
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print(f"Original: {original}")
print(f"Copy: {copy_list}")
print(f"Expected - Original: [1, 2, 3], Copy: [1, 2, 3, 4]")
print(f"PASS" if original == [1, 2, 3] and copy_list == [1, 2, 3, 4] else "FAIL")


# ============================================================================
# SECTION 8: LIST COMPREHENSION (Advanced)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 8: LIST COMPREHENSION (Advanced)")
print("=" * 60)

# Test 8.1: Create list of squares
print("\nTest 8.1: Create list of squares for numbers 1-5")
squares = [x**2 for x in range(1, 6)]
print(f"Result: {squares}")
print(f"Expected: [1, 4, 9, 16, 25]")
print(f"PASS" if squares == [1, 4, 9, 16, 25] else "FAIL")

# Test 8.2: Filter list
print("\nTest 8.2: Create list of even numbers from 1-10")
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Result: {evens}")
print(f"Expected: [2, 4, 6, 8, 10]")
print(f"PASS" if evens == [2, 4, 6, 8, 10] else "FAIL")

# Test 8.3: Transform strings
print("\nTest 8.3: Convert strings to uppercase")
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Result: {upper_words}")
print(f"Expected: ['HELLO', 'WORLD', 'PYTHON']")
print(f"PASS" if upper_words == ['HELLO', 'WORLD', 'PYTHON'] else "FAIL")


# ============================================================================
# CHALLENGE PROBLEMS
# ============================================================================

print("\n" + "=" * 60)
print("CHALLENGE PROBLEMS")
print("=" * 60)

# Challenge 1: Find maximum
print("\nChallenge 1: Find the maximum value in [5, 2, 9, 1, 7]")
max_val = max([5, 2, 9, 1, 7])
print(f"Result: {max_val}")
print(f"Expected: 9")
print(f"PASS" if max_val == 9 else "FAIL")

# Challenge 2: Find minimum
print("\nChallenge 2: Find the minimum value in [5, 2, 9, 1, 7]")
min_val = min([5, 2, 9, 1, 7])
print(f"Result: {min_val}")
print(f"Expected: 1")
print(f"PASS" if min_val == 1 else "FAIL")

# Challenge 3: Sum of all elements
print("\nChallenge 3: Find sum of [10, 20, 30, 40]")
total = sum([10, 20, 30, 40])
print(f"Result: {total}")
print(f"Expected: 100")
print(f"PASS" if total == 100 else "FAIL")

# Challenge 4: Find duplicates
print("\nChallenge 4: Find duplicates in [1, 2, 2, 3, 4, 4, 4, 5]")
nums = [1, 2, 2, 3, 4, 4, 4, 5]
duplicates = list(set([x for x in nums if nums.count(x) > 1]))
duplicates.sort()
print(f"Result: {duplicates}")
print(f"Expected: [2, 4]")
print(f"PASS" if duplicates == [2, 4] else "FAIL")

# Challenge 5: Flatten nested list
print("\nChallenge 5: Flatten [[1, 2], [3, 4], [5, 6]]")
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [x for sublist in nested for x in sublist]
print(f"Result: {flattened}")
print(f"Expected: [1, 2, 3, 4, 5, 6]")
print(f"PASS" if flattened == [1, 2, 3, 4, 5, 6] else "FAIL")

print("\n" + "=" * 60)
print("TEST SHEET COMPLETE!")
print("=" * 60)
