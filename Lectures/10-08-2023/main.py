def sort_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        sorted_lines = sorted(lines)

        with open(output_file, 'w') as file:
            file.writelines(sorted_lines)

    except FileNotFoundError:
        print("Input file not found.")

sort_lines("input.txt", "output.txt")

