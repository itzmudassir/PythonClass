# Create and write to names.txt
with open('names.txt', 'w') as file:
    file.write("Alice\n")
    file.write("Bob\n")
    file.write("Charlie\n")
    file.write("Dave\n")
    file.write("Eve\n")

# Read names from names.txt
with open('names.txt', 'r') as file:
    names = file.readlines()

# Open file to write name lengths
with open('name_lengths.txt', 'w') as output_file:
    for name in names:
        name = name.strip()  # Remove any leading/trailing whitespace
        if len(name) > 3:
            output_file.write(f'{name} is longer than 3 characters\n')
        else:
            output_file.write(f'{name} is 3 characters or less\n')
