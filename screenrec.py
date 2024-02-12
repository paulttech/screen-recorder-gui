import tkinter as tk
import cv2
import numpy as np
from PIL import ImageGrab
from threading import Thread

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Recorder")

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

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
        output = cv2.VideoWriter("output.avi", codec, 10, (1920, 1080))  # Adjust size as needed

        while self.recording:
            frame = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))  # Adjust size as needed
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output.write(frame)

        output.release()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenRecorder()
    app.run()
