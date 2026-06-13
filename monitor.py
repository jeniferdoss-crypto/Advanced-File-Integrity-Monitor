import json
from scanner import scan_folder
from logger import write_log


def check_files(folder):


    with open("baseline.json") as file:

        old_files = json.load(file)



    new_files = scan_folder(folder)



    print("""
================================
 File Integrity Report
================================
""")


    for file in old_files:


        if file not in new_files:


            msg = f"DELETED FILE : {file}"

            print("[ - ]", msg)

            write_log(msg)



        elif old_files[file] != new_files[file]:


            msg = f"MODIFIED FILE : {file}"

            print("[ ! ]", msg)

            write_log(msg)



        else:

            print("[OK]", file)



    for file in new_files:


        if file not in old_files:


            msg = f"NEW FILE : {file}"

            print("[ + ]", msg)

            write_log(msg)



    print("""
================================
 Scan Completed
================================
""")