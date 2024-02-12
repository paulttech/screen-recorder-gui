import tkinter as tk
import cv2
import numpy as np
from PIL import ImageGrab
from threading import Thread

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kovai Screen Recorder")
        self.root.geometry("300x300")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=0, column=0, padx=20, pady=20)

        self.start_button = tk.Button(self.button_frame, text="Start Recording", command=self.start_recording, bg="black", fg="green", padx=10, pady=5)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED, bg="black", fg="red", padx=10, pady=5)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.label_text = tk.Label(self.root, text="Kovai Screen Recorder")
        self.label_text.grid(row=1, column=0, pady=10)
        self.label_text.config(font=("Helvetica", 12, "bold"))

        self.label_text1 = tk.Label(self.root, text="Credits - Pravin Kumar Softwares™")
        self.label_text1.grid(row=3, column=0, pady=10)
        self.label_text1.config(font=("Helvetica", 8))


        self.recording = False

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.record_thread = Thread(target=self.record)
        self.record_thread.start()

    def stop_recording(self):
        self.recording = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def record(self):
        codec = cv2.VideoWriter_fourcc(*"XVID")
        output = cv2.VideoWriter("output.avi", codec, 10, (1920, 1080))  

        while self.recording:
            frame = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080))) 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output.write(frame)

        output.release()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenRecorder()
    app.run()
