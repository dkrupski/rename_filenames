import os
from datetime import datetime

directory = "files"

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    day = datetime.now().strftime("%Y-%m-%d")

    new_filename = f"{filename[:-4]}-{day}.txt"

    new_filepath = os.path.join(directory, new_filename)

    os.rename(filepath, new_filepath)

    print(f"Renamed {filename} to {new_filename}")
