import tkinter as Tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import shutil
import os

def setup_window(bg_color="#F8E599", title="Online Romance", frame_names=["login", "loading", "details", "dashboard", "matches", "questions", "tested"]):
    window = Tk.Tk()
    window.geometry("714x475")
    window.configure(bg=bg_color)
    window.title(title)

    main_frame = Tk.Frame(window, bg=bg_color)
    main_frame.pack(fill="both", expand=True)

    frames = {}
    for name in frame_names:
        frames[name] = Tk.Frame(main_frame, bg=bg_color)

    def show_frame(name):
        for f in frames.values():
            f.pack_forget()
        frames[name].pack(fill="both", expand=True)

    return window, main_frame, frames, show_frame

def convert_scores(scores_str):
    scores = {}

    scores_str = scores_str.strip("{}")
    
    for item in scores_str.split(", "):
        if ": " in item:
            ptype, score = item.split(": ")
            scores[ptype] = int(score)
    return scores

from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import os
import shutil


def upload_profile_picture(user, size=90):

    file_path = filedialog.askopenfilename(
        title="Select Profile Picture",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp")]
    )

    if not file_path:
        return None, None

    os.makedirs("user_data/profile_pics", exist_ok=True)

    ext = os.path.splitext(file_path)[1]
    new_path = f"user_data/profile_pics/{user}{ext}"

    shutil.copy(file_path, new_path)

    # Create circle-masked image
    img = Image.open(new_path).convert("RGBA")
    img = img.resize((size, size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    img.putalpha(mask)

    photo = ImageTk.PhotoImage(img)

    return new_path, photo