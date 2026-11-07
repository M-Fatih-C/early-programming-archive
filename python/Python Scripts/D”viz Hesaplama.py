# -*- coding: utf-8 -*-

import tkinter as tk
import requests

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    api_key = "YOUR_API_KEY"  # Exchange rates API key
    base_url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}"

    response = requests.get(base_url)
    data = response.json()

    if to_currency in data['rates']:
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        label_result.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        label_result.config(text="Döviz kuru bulunamadı.")

root = tk.Tk()
root.title("Döviz Kuru Hesaplama")

label_amount = tk.Label(root, text="Miktar:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

label_from_currency = tk.Label(root, text="Dönüştürülecek Döviz:")
label_from_currency.pack()

combo_from_currency = tk.StringVar()
combo_from_currency.set("USD")  # Varsayılan olarak USD
dropdown_from_currency = tk.OptionMenu(root, combo_from_currency, "USD", "EUR", "GBP", "JPY")
dropdown_from_currency.pack()

label_to_currency = tk.Label(root, text="Dönüştürülen Döviz:")
label_to_currency.pack()

combo_to_currency = tk.StringVar()
combo_to_currency.set("EUR")  # Varsayılan olarak EUR
dropdown_to_currency = tk.OptionMenu(root, combo_to_currency, "USD", "EUR", "GBP", "JPY")
dropdown_to_currency.pack()

button_convert = tk.Button(root, text="Dönüştür", command=convert_currency)
button_convert.pack()

label_result = tk.Label(root, text="", font=("Helvetica", 14))
label_result.pack()

root.mainloop()
