import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender_email = sender_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get('1.0', 'end')
    recipient_emails = recipient_emails_entry.get().split(',')

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.ehlo()
        
        for recipient_email in recipient_emails:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email.strip()
            msg['Subject'] = subject

            body = message
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(sender_email, recipient_email.strip(), msg.as_string())
        server.quit()
        messagebox.showinfo("Success", "Email(s) sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Email Sender")

sender_label = tk.Label(root, text="Your Email:")
sender_label.grid(row=0, column=0)
sender_email_entry = tk.Entry(root)
sender_email_entry.grid(row=0, column=1)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=1, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=1, column=1)

recipient_label = tk.Label(root, text="Recipient Emails (comma-separated):")
recipient_label.grid(row=2, column=0)
recipient_emails_entry = tk.Entry(root)
recipient_emails_entry.grid(row=2, column=1)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=3, column=0)
message_text = tk.Text(root, height=5, width=30)
message_text.grid(row=3, column=1)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=4, columnspan=2)

root.mainloop()
