# file_read_write.py

# 🔸 Write to a file
with open("sample.txt", "w") as file:
    file.write("Hello from Streamlit user!\n")
    file.write("This is the second line.\n")

print("File written successfully.")

# 🔸 Read from the file
with open("sample.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)
