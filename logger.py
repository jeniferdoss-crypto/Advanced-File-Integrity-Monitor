from datetime import datetime


def write_log(message):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open("logs.txt","a") as file:

        file.write(
            f"[{time}] {message}\n"
        )