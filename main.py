import tkinter as tk
import RPi.GPIO as GPIO

button_pins = [5,6]
message_duration = 10000  # メッセージを表示する時間（ミリ秒）

GPIO.setmode(GPIO.BCM)
for button_pin in button_pins:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

root = tk.Tk()
root.title("ボタンチェック")
root.attributes("-fullscreen", True)
root.configure(bg='black')
root.config(cursor="none")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

message_label = tk.Label(frame, text="", font=("Arial", 150), bg='black', fg='white')
message_label.pack(expand=True)

def check_button_state(button_pin):
    if GPIO.input(button_pin) == GPIO.LOW:
        if button_pin == 6:
            message_label.config(text="表示メッセージ1")
            root.after(message_duration, clear_message)
        elif button_pin == 5:
            message_label.config(text="表示メッセージ2")
            root.after(message_duration, clear_message)

def clear_message():
    message_label.config(text="")

def update_button_state():
    for button_pin in button_pins:
        check_button_state(button_pin)
    root.after(100, update_button_state)

root.after(100, update_button_state)
root.mainloop()
