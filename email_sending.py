import smtplib

# Email configuration
sender_email = "girishdoddi055@gmail.com"
receiver_email = "girishdoddi0555@gmail.com"
app_password = "pkjk fufi wpjz ptve"

# Create a message
subject = "Test Email from Python"
body = "This is a test email sent from Python using an app-specific password."
message = f"Subject: {subject}\n\n{body}"

# Connect to Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Login to SMTP server with app-specific password
    server.login(sender_email, app_password)
    # Send email
    server.sendmail(sender_email, receiver_email, message)