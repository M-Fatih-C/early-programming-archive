import smtplib
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Veri toplama
def collect_data():
    # Verileri bir Excel dosyasından okuyun
    data = pd.read_excel("data.xlsx")
    return data

# Veri analizi ve özetleme
def analyze_data(data):
    # Temel istatistiksel analiz
    summary_stats = data.describe()
    
    # Örnek bir grafik oluşturma
    plt.figure(figsize=(10, 6))
    data.plot(kind='line')
    plt.title('Data Trends')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.savefig('data_trends.png')
    plt.close()

    # Analiz özetini metin formatında oluşturma
    summary = "Data Analysis Summary:\n\n"
    summary += str(summary_stats)

    return summary

# E-posta gönderimi
def send_email(summary):
    # SMTP Sunucu Ayarları
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')
    recipient_email = 'recipient_email@gmail.com'

    # E-posta oluşturma
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Data Analysis Report'

    # E-posta metni
    body = summary
    msg.attach(MIMEText(body, 'plain'))

    # Ek olarak grafik dosyasını gönderme
    filename = 'data_trends.png'
    attachment = open(filename, 'rb')
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    # E-posta gönderme
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Ana program
if __name__ == "__main__":
    # Verileri toplayın
    data = collect_data()

    # Verileri analiz edin
    summary = analyze_data(data)

    # E-postayı gönderin
    send_email(summary)
