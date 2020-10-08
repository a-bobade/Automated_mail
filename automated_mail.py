# Import all functions
import datetime
import smtplib
import time

# To get the current date
now = datetime.datetime.now()

# Setting the time to send the mail, 7am in this case
print_time = datetime.datetime.combine(now.date(), datetime.time(7, 0, 0, 0))
time.sleep((print_time - now).total_seconds())

# Connecting to an SMTP server
mail = smtplib.SMTP("smtp.gmail.com", 587)
# Sending the SMTP "Hello" message
mail.ehlo()
# Starting TLS Encryption
mail.starttls()
# Logging in to the SMTP server
mail.login("username@gmail.com", "gmail_password")
# Sending the mail
mail.sendmail("username@gmail.com", "receiver@gmail.com",
              "Subject: Hello Programmer.\nDon't you think Python is the best language?")
# Disconnecting from the SMTP server
mail.quit()
print("email sent")
