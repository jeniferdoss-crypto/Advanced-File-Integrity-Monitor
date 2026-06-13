import json
from scanner import scan_folder
from monitor import check_files


print("""
1. Create Baseline
2. Scan Files
""")


choice=input("Choice: ")



if choice=="1":


    folder=input("Folder path: ")


    data=scan_folder(folder)


    with open("baseline.json","w") as file:

        json.dump(data,file,indent=4)



    print("Baseline created")



elif choice=="2":


    folder=input("Folder path: ")

    check_files(folder)

