import hashlib
import os


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:

            data = f.read(4096)

            if not data:
                break

            sha256.update(data)


    return sha256.hexdigest()



def scan_folder(folder):

    file_hashes = {}


    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            file_hashes[path] = calculate_hash(path)


    return file_hashes