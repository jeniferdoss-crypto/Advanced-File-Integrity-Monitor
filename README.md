# Advanced File Integrity Monitor 🔐

A Python-based cybersecurity tool that monitors file integrity using **SHA256 hashing**.

This project detects file changes by comparing current files with a saved baseline. It identifies **modified, deleted, and newly created files**.

---

## Features

- SHA256 file hashing
- Create file baseline
- Detect modified files
- Detect deleted files
- Detect new files
- Generate scan reports
- Security event logging

---

## Project Structure


Advanced-File-Integrity-Monitor

├── main.py
├── scanner.py
├── monitor.py
├── logger.py
├── config.json
├── baseline.json
├── logs.txt
└── result.txt


---

## How It Works

1. Select the folder to monitor.
2. Create a baseline of the files.
3. The program stores file hashes.
4. Run a scan to compare changes.
5. The tool reports modified, deleted, and new files.

---

## Run Project:

python main.py

---

## Usage
Create Baseline

Choose:

1. Create Baseline

Enter the folder path.

Example:

C:\Users\ELCOT\Desktop\TestFolder
Scan Files

Choose:

2. Scan Files

The program detects:

Modified files
Deleted files
New files

---

## Example Output

--------------------------------
 File Integrity Report
--------------------------------

[ ! ] MODIFIED FILE :
C:\Users\ELCOT\Desktop\TestFolder\box.txt

[ - ] DELETED FILE :
C:\Users\ELCOT\Desktop\TestFolder\hiii.txt

[ + ] NEW FILE :
C:\Users\ELCOT\Desktop\TestFolder\hii.txt


--------------------------------
 Scan Completed
--------------------------------

---

## Technologies Used
Python
SHA256 Hashing
JSON
File System Monitoring
Logging
Security Concepts
File Integrity Monitoring (FIM)
Hash Verification
Change Detection
Security Logging

---

## License

This project is created for educational purposes and cybersecurity learning.
