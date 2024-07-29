import json

def read_inbox():
    with open("inbox.json", "r") as f:
        inbox = json.loads(f.read())
    return inbox

def write_inbox(data):
    with open("inbox.json", "w") as f:
        f.write(json.dumps(data))

def recv_email(email_json):
    inbox = read_inbox()
    if email_json['To'] not in inbox:
        inbox[email_json['To']] = [email_json]
    else:
        inbox[email_json['To']].append(email_json)
    write_inbox(inbox)