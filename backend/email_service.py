import smtplib

sender_email = "girishdoddi055@gmail.com"
app_password = "pkjk fufi wpjz ptve"

def send_otp_to_mail(email, otp):
    subject = "OTP Verification"
    body = f"Here's the OTP for email-verification ->{otp}"
    message = f"Subject: {subject}\n\n{body}"
    receiver_email = email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Login to SMTP server with app-specific password
        server.login(sender_email, app_password)
        # Send email
        server.sendmail(sender_email, receiver_email, message)