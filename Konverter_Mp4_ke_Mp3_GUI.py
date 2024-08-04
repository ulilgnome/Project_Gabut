import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_video_to_mp3(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'mp3',
        output_file
    ]
    subprocess.run(command)

def select_file():
    input_file = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv")])
    if input_file:
        output_file = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                   filetypes=[("MP3 files", "*.mp3")])
        if output_file:
            try:
                convert_video_to_mp3(input_file, output_file)
                messagebox.showinfo("Sukses", "Konversi selesai!")
            except Exception as e:
                messagebox.showerror("Kesalahan", f"Gagal mengonversi: {str(e)}")

# Setup GUI
root = tk.Tk()
root.title("Konversi Video ke MP3")
root.geometry("300x150")

button = tk.Button(root, text="Pilih File Video", command=select_file)
button.pack(pady=20)

root.mainloop()
