import os

# save the last unique page identifiers in filenames in a new file so they're not lost (save all filenames)

def rename_files_and_folders(root):
    """
    Recursively renames all files and folders in the directory tree rooted at `root`
    by adding a 'b' at the end of their names and saves the old filenames in a file.
    """
    with open("old_filenames.txt", "a") as file:
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isfile(path):
                dir_name, base_name = os.path.split(path)
                base_name, extension = os.path.splitext(base_name)
                
                # Split the base name into words
                words = base_name.split(' ')
                
                if len(words) > 1 and len(words[-1]) > 30:
                    new_base_name = " ".join(words[:-1]) + extension

                    os.rename(path, os.path.join(dir_name, new_base_name))
                    print(f'Renamed file "{name}" to "{new_base_name}"')

                    file.write(f'Old name: {name}\n')
            elif os.path.isdir(path):
                rename_files_and_folders(path)

                dir_name, base_name = os.path.split(path)
                base_name, extension = os.path.splitext(base_name)
                
                # Split the base name into words
                words = base_name.split(' ')
                
                if len(words) > 1 and len(words[-1]) > 30:
                    new_base_name = " ".join(words[:-1]) + extension

                    os.rename(path, os.path.join(dir_name, new_base_name))
                    print(f'Renamed file "{name}" to "{new_base_name}"')

                    file.write(f'Old name: {name}\n')

folder_names = ["expms", "techs", "notes", "apps", "Source", "ideas"]

for fn in folder_names:
    # check if the folder exists
    if os.path.exists(f"C:\\Users\\mikel\\Downloads\\{fn}"):
        top_dir = f"C:\\Users\\mikel\\Downloads\\{fn}"
        rename_files_and_folders(top_dir)
