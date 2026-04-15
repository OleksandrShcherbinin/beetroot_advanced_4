def linear_search(sequences: list[int], target: int) -> int:
    for index, element in enumerate(sequences):
        if element == target:
            return index

    return None


numbers = [4, 2, 3, 1, 5, 6, 8, 9, 10]
result = linear_search(numbers, 10)
# print(result)


# O(log n)
def binary_search(sequences: list[int], target: int) -> int:
    low = 0
    high = len(sequences) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = sequences[mid]
        if guess == target:
            print(f"Found {target} in {steps} steps")
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    print(f"{target} not found in {steps} steps")
    return None

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(sorted_list, 1)

# O(1)
# print(len(sorted_list))
# print(len(list(range(100_000_000_000))))

# O(1)
# print(sorted_list[3])

my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
}
# O(1)
# print(my_dict['four'])

# for i in sorted_list: ... # O(n)
#
# for i in range(100_000_000_000): ... # O(n)


# O(1)
# O(log n)
# O(n)
# O(n^2)

# O(n^2)
def find_common(list_1, list_2):
    result = []
    for element in list_1:
        if element in list_2:
            result.append(element)

    return result

# O(n)
def find_common_effective(list_1, set_2):
    result = []
    for element in list_1:
        if element in set_2:
            result.append(element)

    return result


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
second_set = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# print(find_common(sorted_list, second_set))


# O(n^3)
def triple_iterations(number):
    for i in range(number):
        for j in range(i + 1, number):
            for k in range(j + 1, number):
                print(i, j, k)


# O(2^n)
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# O(n!)
# 1 * 2 * 3 * 4
def generate_permutations(input_list: list | str):
    if len(input_list) <= 0:
        return [input_list[:]]

    permutations = []
    for i in range(len(input_list)):
        current = input_list[i]
        rest = input_list[:i] + input_list[i + 1:]
        for perm in generate_permutations(rest):
            permutations.append([current] + perm)
    return permutations

# for p in generate_permutations(["a", "b", "c", 'd', 'e', 'f']):
#     print(p)


# O(n^2)
def find_common(list_1, list_2):
    result = []
    for element in list_1:
        if element in list_2:
            result.append(element)

    return result

# O(n)
def find_common_effective(list_1, set_2):
    result = []
    for element in list_1:
        if element in set_2:
            result.append(element)

    return result


from time import perf_counter
import matplotlib.pyplot as plt


def measure_time(func, *args):
    start = perf_counter()
    func(*args)
    end = perf_counter()
    return end - start


sizes = []
times_linear = []
times_quadratic = []

for n in range(1, 501):
    data_list = list(range(n))
    data_set = set(data_list)

    sizes.append(n)

    times_quadratic.append(measure_time(find_common, data_list, data_list))
    times_linear.append(measure_time(find_common_effective, data_list, data_set))

fig, ax = plt.subplots()
# ax.plot(sizes, times_linear, label="Linear")
ax.plot(sizes, times_quadratic, label="Quadratic")
ax.set_xlabel("Input Size (n)")
ax.set_ylabel("Time (seconds)")
ax.set_title("Linear and Quadratic Time")
ax.legend()
fig.savefig("complexity.png")
plt.show()