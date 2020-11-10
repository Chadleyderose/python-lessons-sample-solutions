from smtplib import SMTP


server = SMTP("smtp.gmail.com", 587)

try:
    sender_email = "thapelo.tsotetsi504@gmail.com"
    receiver_email = "thapelo@lifechoices.co.za"
    password = str(input("Please enter your password: "))
    server.starttls()

    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, 'This is a test email.')
    print("the message has been successfully sent")
except Exception as err:
    print("Something went wrong...", err)
finally:
    server.close()

# Tkinter - Building Email Client
# Create a tkinter application to send emails.
# The application should have 3 entry boxes. One for "To Email", one for the subject
# and another for the actual message. The aaplication needs to have a button to send
# the email address. You can also add a clear button which will clear all the inputs.
