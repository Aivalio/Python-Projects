# ----------------------------------------------
# import os
# ----------------------------------------------
# The 'os' module lets Python interact with the operating system.
# We use it for:
#   - os.listdir()  → list files in a folder
#   - os.rename()   → rename or move files
#   - os.path.exists() → check if a folder exists
#   - os.mkdir()    → create new folders
# Without 'os', we cannot manipulate files or directories.
# ----------------------------------------------
import os


def arrange_files(files, ext):
    """
    This function takes a list of files and an extension (like '.jpg'),
    filters out only the files with that extension,
    prints them, creates an 'images' folder if not present,
    and moves/renames the files into that folder.
    """

    # Filter files that end with the given extension
    # Example: keep only ".jpg" files
    files_with_ext = [file for file in files if file.endswith(ext)]

    print("Files found with extension", ext, ":", files_with_ext)

    # Check if "images" folder exists; if not, create it
    if not os.path.exists("images"):
        os.mkdir("images")  # Creates a new folder called "images"
        print("Created 'images' directory.")

    # Enumerate gives us index (i) and file name
    # i starts from 0, so we use (i+1) to start numbering at 1.
    for i, file in enumerate(files_with_ext):
        new_name = f"images/Photo-{i+1}{ext}"  # New path + new name
        os.rename(file, new_name)             # Move + rename file
        print(f"Renamed '{file}' → '{new_name}'")


# ------------------------------------------------------
# Main program block
# This runs only when the file is executed directly.
# ------------------------------------------------------
if __name__ == "__main__":
    # Get all items in the current folder
    files = os.listdir()

    # Arrange only .jpg files
    arrange_files(files, ".jpg")
    print(arrange_files.__doc__)
