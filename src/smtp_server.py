from src import email_parser, smtp_server, website, inbox_handler
from aiosmtpd.controller import Controller
import asyncore

class SMTPServer:
    async def handle_DATA(self, server, session, envelope):
        data = envelope.content
        try:
            parsed_email = email_parser.email_bytes_to_json(data)

            print("----")
            print("Received Email!")
            print(f"From: {parsed_email['From']}")
            print(f"To: {parsed_email['To']}")
            print(f"Subject: {parsed_email['Subject']}")
            print("----")

            inbox_handler.recv_email(parsed_email)
        except:
            pass

        return '250 Message accepted for delivery'

def run_smtp_server():
    server = SMTPServer()
    controller = Controller(server, hostname="0.0.0.0", port=25)
    controller.start()
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass