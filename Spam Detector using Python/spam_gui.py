import tkinter as tk
from tkinter import messagebox
import joblib

model = joblib.load("logistic_model.pkl")
vectorizer = joblib.load("count_vectorizer.pkl")

def predict_spam():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showwarning("Warning", "Please enter a message.")
        return
    vectorized_input = vectorizer.transform([user_input])
    prediction = model.predict(vectorized_input)[0]
    
    if prediction == 1:
        result_label.config(text="🚫 Spam", fg="red")
    else:
        result_label.config(text="✅ Not Spam", fg="green")


root = tk.Tk()
root.title("Spam Detector for Turkish E-Mails")
root.geometry("420x220")

tk.Label(root, text="Enter your message:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 10))
entry.pack(pady=5)

tk.Button(root, text="Submit", command=predict_spam, font=("Arial", 10)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
