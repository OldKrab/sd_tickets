# Import the os module to create folders and files
import os

# Open the temp file and read its contents
with open("temp", "r", encoding="utf-8") as f:
    contents = f.read()

# Split the contents by empty lines
sections = contents.split("\n\n")

# Loop through the sections and create folders and files
for i, section in enumerate(sections):
    # Get the title of the section
    title = section.strip()

    # Create a folder name with leading zeros
    folder_name = f"{i+1:02d}"

    # Create a full path for the folder inside the tickets folder
    folder_path = os.path.join("tickets", folder_name)

    # Create the folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create a file name for the README.md file
    file_name = "README.md"

    # Create a full path for the file inside the folder
    file_path = os.path.join(folder_path, file_name)

    # Write the title to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(title)