# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:00:55 2023

@author: Muhammet Fatih
"""

#from datetime import datetime

#current_time = datetime.now()
#formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
#print("Şu anki tarih ve saat:", formatted_time)

import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # 1000ms (1 saniye) sonra güncelleme yap

root = tk.Tk()
root.title("Saat ve Tarih Göstergesi")

time_label = tk.Label(root, text="", font=("Helvetica", 24))
time_label.pack(padx=20, pady=20)

update_time()  # Saat ve tarih güncellemesini başlat

root.mainloop()
