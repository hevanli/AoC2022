file = open("day4input.txt", "r")
overlaps = 0
for line in file.read().splitlines():
    # Create two lists using split and map function in order to extract range values as integers
    first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
    if first_pair[0] != second_pair[0]:
        # Determine the inside range by the higher starting value
        if first_pair[0] > second_pair[0]:
            inside_range, outside_range = first_pair, second_pair
        else:
            inside_range, outside_range = second_pair, first_pair
    else:
        # If the starting value is the same, then determine the inside range by the smaller ending value
        if first_pair[1] < second_pair[1]:
            inside_range, outside_range = first_pair, second_pair
        else:
            inside_range, outside_range = second_pair, first_pair
    # Check if the inside range ends before or at the same place as the end of outside range
    if inside_range[1] <= outside_range[1]:
        print(first_pair + second_pair)
        overlaps += 1
print("Task 1 result: " + str(overlaps))
file.close()
