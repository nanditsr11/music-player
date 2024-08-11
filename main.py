import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer for audio playback
mixer.init()

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x200")

# Global variable to hold the current music file path
current_music = None

# Function to load a music file
def load_music():
    global current_music
    current_music = filedialog.askopenfilename(initialdir="music", title="Select a Music File", filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")))
    if current_music:
        mixer.music.load(current_music)
        song_label.config(text=os.path.basename(current_music))

# Function to play the loaded music file
def play_music():
    if current_music:
        mixer.music.play()

# Function to pause the music
def pause_music():
    mixer.music.pause()

# Function to resume the music
def resume_music():
    mixer.music.unpause()

# Function to stop the music
def stop_music():
    mixer.music.stop()

# UI Components
load_button = tk.Button(root, text="Load Music", command=load_music)
play_button = tk.Button(root, text="Play", command=play_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
resume_button = tk.Button(root, text="Resume", command=resume_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)
song_label = tk.Label(root, text="No song loaded", relief="sunken", anchor="w")

# Arrange UI Components
load_button.pack(pady=10)
play_button.pack(pady=5)
pause_button.pack(pady=5)
resume_button.pack(pady=5)
stop_button.pack(pady=5)
song_label.pack(fill="x", padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
