import tkinter as tk
import requests
import schedule # type: ignore

def get_weather():
    city = entry_city.get()
    api_key = "YOUR_API_KEY"  # Buraya geçerli bir API anahtarı yerleştirin
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        # Yanıtın başarılı olup olmadığını kontrol et
        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            weather_label.config(text=f"Hava Durumu: {weather_description}\nSıcaklık: {temperature}°C")
        elif response.status_code == 401:
            weather_label.config(text="Hata: Geçersiz API anahtarı. Lütfen API anahtarınızı kontrol edin.")
        else:
            # API yanıtında başka bir hata varsa kullanıcıya hata mesajı göster
            error_message = data.get("message", "Hava durumu alınamadı.")
            weather_label.config(text=f"Hata: {error_message}")

    except requests.exceptions.RequestException as e:
        # İstek sırasında bir hata oluşursa kullanıcıya hata mesajı göster
        weather_label.config(text=f"İstek hatası: {str(e)}")

def update_weather():
    get_weather()
    schedule.every(30).minutes.do(get_weather)

def start_reminder():
    update_weather()
    schedule.run_all()
    root.after(1000, start_reminder)

root = tk.Tk()
root.title("Hava Durumu Hatırlatıcısı")

label_city = tk.Label(root, text="Şehir:")
label_city.pack()

entry_city = tk.Entry(root)
entry_city.pack()

button_get_weather = tk.Button(root, text="Hava Durumu Al", command=get_weather)
button_get_weather.pack()

weather_label = tk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack()

start_reminder()  # Hatırlatıcıyı başlat

root.mainloop()
