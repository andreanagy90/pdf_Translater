import os

def get_input():
    folder = input("Please enter the folder path \n(e.g. C:\\Users\\User\\Documents or Linux /home/user/Documents):\n")

    filename = input("Please enter your filename with extension (e.g. myfile.doc):\n")

    file_path = os.path.join(folder, filename)

    if os.path.exists(file_path):
        print(f"File found: {file_path}")
    else:
        print("File not found")
        exit()

    output = input("Please enter the output folder path\n")
    filename_2 = input("Please enter your new filename (e.g. myfile):\n")
    output_path = os.path.join(output, filename_2 + ".docx")

    if not os.path.exists(output):
        print("Output folder does not exist!")
        exit()

    return file_path, output_path
