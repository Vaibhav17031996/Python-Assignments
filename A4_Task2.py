'''
# Method 1 for entering the text in the file:
file = open("output.txt", "w")
writing_file = file.write("Hello, python!" + "\n")
print(writing_file)
file.close()
'''

# Method 2 for entering the text in the file:
# Take user input and write to output.txt
user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Append additional data
additional_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Read and display the final content
with open("output.txt", "r") as file:
    for line in file:
        print(line.rstrip())