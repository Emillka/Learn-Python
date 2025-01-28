import os

def change_names_of_pictures(catalog_path):
    if not os.path.exists(catalog_path):
        print("The specified directory path does not exist.")
        return

    file_list = os.listdir(catalog_path)
    file_list.sort()
    
    numbering = 1
    for old_name in file_list:
        if not old_name.lower().endswith('.jpg'):
            continue  # Skip non-JPG files
        
        new_name = f"{numbering}.jpg"
        old_path = os.path.join(catalog_path, old_name)
        new_path = os.path.join(catalog_path, new_name)

        os.rename(old_path, new_path)
        numbering += 1

    print("File names changed.")

catalog_path = "enter the path to the directory here"
change_names_of_pictures(catalog_path)
