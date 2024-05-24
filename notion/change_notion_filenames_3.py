import os

# Save the last unique page identifiers in filenames in a new file so they're not lost (save all filenames)

def generate_unique_filename(target_path):
    """Returns a unique filename by appending a suffix if the target file already exists."""
    base, ext = os.path.splitext(target_path)
    counter = 1
    while os.path.exists(target_path):
        target_path = f"{base}_{counter}{ext}"
        counter += 1
    return target_path

def rename_files_and_folders(root):
    """
    Recursively renames all files and folders in the directory tree rooted at `root`
    by adding a 'b' at the end of their names and saves the old filenames in a file.
    """
    with open("old_filenames.txt", "a", encoding="utf-8") as file:
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isfile(path):
                dir_name, base_name = os.path.split(path)
                base_name, extension = os.path.splitext(base_name)
                
                # Split the base name into words
                words = base_name.split(' ')
                
                if len(words) > 1 and len(words[-1]) > 30:
                    new_base_name = " ".join(words[:-1]) + extension

                    new_path = generate_unique_filename(os.path.join(dir_name, new_base_name))
                    os.rename(path, new_path)
                    print(f'Renamed "{path}" to "{new_path}"')
                    print(f'Renamed file "{name}" to "{new_base_name}"')

                    file.write(f'Old name: {name}\\n')
            elif os.path.isdir(path):
                rename_files_and_folders(path)

                dir_name, base_name = os.path.split(path)
                base_name, extension = os.path.splitext(base_name)
                
                # Split the base name into words
                words = base_name.split(' ')
                
                if len(words) > 1 and len(words[-1]) > 30:
                    new_base_name = " ".join(words[:-1]) + extension

                    new_path = generate_unique_filename(os.path.join(dir_name, new_base_name))
                    os.rename(path, new_path)
                    print(f'Renamed "{path}" to "{new_path}"')
                    print(f'Renamed file "{name}" to "{new_base_name}"')

                    file.write(f'Old name: {name}\\n')

folder_names = ["expms", "techs", "notes", "apps", "eduarch", "ideas", "quizzes", "stage"]

for fn in folder_names:
    # Check if the folder exists
    if os.path.exists(f"C:\\Users\\mikel\\Downloads\\{fn}"):
        top_dir = f"C:\\Users\\mikel\\Downloads\\{fn}"
        rename_files_and_folders(top_dir)
