from tkinter.ttk import Button

#one of the biggest parts of the project
def setup_dashboard_page(window, main_frame, frames, show_frame, app_data, details_entries):

    from multiprocessing import process
    from pathlib import Path
    import common


    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Akshaj Homework\ICS4U - Major Project 1\ICS4U - Major Project 1\build\assetsDashboard\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #dashboard frame
    dashboard_frame = frames["dashboard"]

    # profile_label = Label(dashboard_frame, bg="#F9E699")
    # profile_label.place(x=300, y=50, width=90, height=90)

    #to load the info at runtime
    def load_dashboard():
        #nonlocal dashboard_frame, profile_label
        user = app_data["current_user"]
        data = app_data["users"].get(user, {})

        for key in dashboard_entries:
            
            dashboard_entries[key].config(state="normal")

            dashboard_entries[key].delete(0, "end")
            dashboard_entries[key].insert(0, data.get(key, ""))

            dashboard_entries[key].config(state="readonly")
            dashboard_entries[key].config(readonlybackground="#F9FFA9")

    #helper functions
    def edit_entry(entry):
        entry.config(state="normal")
        entry.focus_set()
        entry.selection_range(0, "end")  # highlights all text
    
    def on_focus_out(event, key, entry):
        entry.after(1, lambda: save_field(key, entry))


    def save_field(key, entry):

        if entry.cget("state") == "readonly":
            return
        
        # Save value        
        user = app_data["current_user"]
        value = entry.get().strip()

        if app_data["users"][user].get(key) == value:
            entry.config(state="readonly")
            return
        
        print("Saving:", value)

        app_data["users"][user][key] = value
        
        with open(Path(__file__).parent / "personalInfo.txt", "w") as f:

            for user, info in app_data["users"].items():
                line = user + " | " + " # ".join(str(v) for v in info.values()) + "\n"
                f.write(line)

        # Lock again
        entry.config(state="readonly")

    def show_matches():
        show_frame("matches")
        frames["matches"].load_matches()
        
        
    canvas = Canvas(
        dashboard_frame,
        bg = "#F9E699",
        height = 475,
        width = 714,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.bind("<Button-1>", lambda e: dashboard_frame.focus_set())

    canvas.create_text(
        210.0,
        79.0,
        anchor="nw",
        text="Your Dashboard",
        fill="#974646",
        font=("Inter Bold", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("heart_topLeft.png"))
    image_1 = canvas.create_image(
        78.0,
        84.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("heart_topRight.png"))
    image_2 = canvas.create_image(
        630.0,
        84.0,
        image=image_image_2
    )


    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    
    entry_image_1Blue = PhotoImage(
        file=relative_to_assets("entry_1Blue.png"))
    
    entry_bg_1 = canvas.create_image(
        147.0,
        216.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_1.place(
        x=61.0,
        y=184.0,
        width=182.0,
        height=58.0
    )


    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    
    entry_image_2Blue = PhotoImage(
        file=relative_to_assets("entry_2Blue.png"))
    
    entry_bg_2 = canvas.create_image(
        147.0,
        334.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_2.place(
        x=271.0,
        y=184.0,
        width=182.0,
        height=58.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    
    entry_image_3Blue = PhotoImage(
        file=relative_to_assets("entry_3Blue.png"))

    entry_bg_3 = canvas.create_image(
        567.0,
        216.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_3.place(
        x=481.0,
        y=184.0,
        width=182.0,
        height=58.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    
    entry_image_4Blue = PhotoImage(
        file=relative_to_assets("entry_4Blue.png"))
    
    entry_bg_4 = canvas.create_image(
        567.0,
        334.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_4.place(
        x=61.0,
        y=302.0,
        width=182.0,
        height=58.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    
    entry_image_5Blue = PhotoImage(
        file=relative_to_assets("entry_5Blue.png"))
    
    entry_bg_5 = canvas.create_image(
        357.0,
        216.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_5.place(
        x=271.0,
        y=302.0,
        width=182.0,
        height=58.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    
    entry_image_6Blue = PhotoImage(
        file=relative_to_assets("entry_6Blue.png"))
    
    entry_bg_6 = canvas.create_image(
        357.0,
        334.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        master=dashboard_frame,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_6.place(
        x=481.0,
        y=302.0,
        width=182.0,
        height=58.0
    )


    button_image_1 = PhotoImage(
        file=relative_to_assets("edit1.png"))
    
    button_1 = Button(
        master=dashboard_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_1),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("save1.png"))
    
    button_2 = Button(
        master=dashboard_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("firstname", entry_1),
        relief="flat"
    )
    button_2.place(
        x=164.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("edit2.png"))
    
    button_3 = Button(
        master=dashboard_frame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_2),
        relief="flat"
    )
    button_3.place(
        x=250.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("save2.png"))
    
    button_4 = Button(
        master=dashboard_frame,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("lastname", entry_2),
        relief="flat"
    )
    button_4.place(
        x=374.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("edit3.png"))
    
    button_5 = Button(
        master=dashboard_frame,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_3),
        relief="flat"
    )
    button_5.place(
        x=460.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("save3.png"))
    
    button_6 = Button(
        master=dashboard_frame,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("age", entry_3),
        relief="flat"
    )
    button_6.place(
        x=584.0,
        y=245.0,
        width=91.0,
        height=25.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("edit4.png"))
    
    button_7 = Button(
        master=dashboard_frame,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_4),
        relief="flat"
    )
    button_7.place(
        x=40.0,
        y=363.0,
        width=91.0,
        height=25.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("save4.png"))
    
    button_8 = Button(
        master=dashboard_frame,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("gender", entry_4),
        relief="flat"
    )
    button_8.place(
        x=164.0,
        y=363.0,
        width=91.0,
        height=25.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("edit5.png"))
    
    button_9 = Button(
        master=dashboard_frame,
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_5),
        relief="flat"
    )
    button_9.place(
        x=250.0,
        y=363.0,
        width=91.0,
        height=25.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("save5.png"))
    
    button_10 = Button(
        master=dashboard_frame,
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("personality_traits", entry_5),
        relief="flat"
    )
    button_10.place(
        x=374.0,
        y=363.0,
        width=91.0,
        height=25.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("edit6.png"))
    
    button_11 = Button(
        master=dashboard_frame,
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: edit_entry(entry_6),
        relief="flat"
    )
    button_11.place(
        x=460.0,
        y=363.0,
        width=91.0,
        height=25.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("save6.png"))
    
    button_12 = Button(
        master=dashboard_frame,
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        font=("Inter", 5 * -1),
        command=lambda: save_field("hobbies", entry_6),
        relief="flat"
    )
    button_12.place(
        x=584.0,
        y=363.0,
        width=91.0,
        height=25.0
    )


    button_image_13 = PhotoImage(
        file=relative_to_assets("see_matches.png"))
    
    button_13 = Button(
        master=dashboard_frame,
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        bg="#F9E699",
        activebackground="#F9E699",
        command=lambda: show_matches(),
        relief="flat"
    )
    button_13.place(
        x=252.0,
        y=440.0,
        width=215.0,
        height=38.0
    )

    #avoiding garbage collection of images
    dashboard_frame.photo_images = [
        image_image_1,
        image_image_2,
        entry_image_1,
        entry_image_1Blue,
        entry_image_2,
        entry_image_2Blue,
        entry_image_3,
        entry_image_3Blue,
        entry_image_4,
        entry_image_4Blue,
        entry_image_5,
        entry_image_5Blue,
        entry_image_6,
        entry_image_6Blue,
        button_image_1,
        button_image_2,
        button_image_3,
        button_image_4,
        button_image_5,
        button_image_6,
        button_image_7,
        button_image_8,
        button_image_9,
        button_image_10,
        button_image_11,
        button_image_12,
        button_image_13
    ]
    
    dashboard_entries = {
        "firstname": entry_1,
        "lastname": entry_2,
        "age": entry_3,
        "gender": entry_4,
        "personality_traits": entry_5,
        "hobbies": entry_6
    }

    def bind_entry(key, entry):
        entry.bind("<FocusOut>", lambda e: on_focus_out(e, key, entry))


    for key, entry in dashboard_entries.items():
        bind_entry(key, entry)


    dashboard_frame.load_dashboard = load_dashboard