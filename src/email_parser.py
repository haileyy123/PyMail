from datetime import datetime
from email.parser import BytesParser
import time

def format_time(timestamp):
    dt_object = datetime.utcfromtimestamp(timestamp)
    formatted_date = dt_object.strftime("%b %d at %H:%M:%S")
    return formatted_date

def extract_text_between_words(input_string, start_word, end_word):
    start_index = input_string.find(start_word)
    end_index = input_string.find(end_word)
    return input_string[start_index + len(start_word):end_index].strip()

def email_bytes_to_json(data):
    msg = BytesParser().parsebytes(data)
    to_field = msg["To"]
    if isinstance(to_field, list):
        to_field = to_field[0]
    elif isinstance(to_field, str):
        pass
    else:
        to_field = str(to_field)

    if " " in to_field and "<" in to_field and ">" in to_field:
        to_field = extract_text_between_words(to_field, "<", ">")

    from_field = msg["From"]
    if isinstance(to_field, list):
        from_field = to_field[0]
    elif isinstance(to_field, str):
        pass
    else:
        from_field = str(to_field)

    if " " in from_field and "<" in from_field and ">" in from_field:
        from_field = extract_text_between_words(from_field, "<", ">")

    email_dict = {
        "From": from_field,
        "To": to_field,
        "Subject": msg["Subject"],
        "Timestamp": int(time.time()),
        "Sent": format_time(int(time.time()))
    }
    for part in msg.walk():
        content_type = part.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            email_dict["Body"] = part.get_payload(decode=True).decode(part.get_content_charset())
            if content_type == "text/plain":
                email_dict["ContentType"] = "Text"
            if content_type == "text/html":
                email_dict["ContentType"] = "HTML"

    return email_dict