def sort_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    sorted_lines = sorted(lines)

    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)
    

sort_lines("input.txt", "output.txt")
