import os
import time

from src import email_parser, smtp_server, website, inbox_handler

if not os.path.isfile("inbox.json"):
    print("Creating Inbox Database..")
    with open("inbox.json", "w") as f:
        f.write("{}")

if __name__ == "__main__":
    import threading

    smtp_thread = threading.Thread(target=smtp_server.run_smtp_server)
    flask_thread = threading.Thread(target=website.run_flask_server)

    print("Starting PyMail SMTP Server and HTTP Server")

    smtp_thread.start()
    flask_thread.start()

    time.sleep(1)

    print("HTTP Server Listening On Port 80.")
    print("SMTP Server Listening On Port 25")

    print("")

    print("PyMail Is Running! Visit: http://localhost To Use It.")

    smtp_thread.join()
    flask_thread.join()