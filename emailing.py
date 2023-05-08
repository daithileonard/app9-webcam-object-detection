import smtplib
from email.message import EmailMessage
import imghdr
# import Pillow as pil

PASSWORD = "triptahziifbnxgn"
SENDER = "daithileonard@gmail.com"
RECEIVER = "daithileonard@gmail.com"


def send_email(image_path):
    print("send email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey we just saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email function finished")


if __name__ == "__main__":
    send_email(image_path="images/17_image.png")
