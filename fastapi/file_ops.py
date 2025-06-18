import os

# Step 1: Create and Write to a File
file_path = "sample.txt"
with open(file_path, "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("File created and written successfully.")

# Step 2: Read the File
with open(file_path, "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# Step 3: Append to the File
with open(file_path, "a") as file:
    file.write("This is an appended line.\n")

print("Line appended successfully.")

# Step 4: Update a Specific Line
# Let's say we want to update "second line" to "UPDATED second line"

# Read all lines
with open(file_path, "r") as file:
    lines = file.readlines()

# Modify desired line (e.g., line 2)
for i in range(len(lines)):
    if "second line" in lines[i]:
        lines[i] = "This is the UPDATED second line.\n"

# Write back the updated lines
with open(file_path, "w") as file:
    file.writelines(lines)

print("Line updated successfully.")

# Step 5: Read the Updated File
with open(file_path, "r") as file:
    updated_content = file.read()
    print("\n--- Updated File Content ---")
    print(updated_content)

# Step 6: Delete the File (Optional)
delete_choice = input("\nDo you want to delete the file? (yes/no): ").lower()
if delete_choice == "yes":
    os.remove(file_path)
    print("File deleted.")
else:
    print("File not deleted.")

 