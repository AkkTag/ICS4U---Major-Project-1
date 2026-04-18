def setup_loading_page(window, main_frame, frames, show_frame, details_entries, app_state, app_data):

    from multiprocessing import process
    from pathlib import Path
    # from tkinter import *
    # Explicit imports to satisfy Flake8

    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
    #from dashboard import load_dashboard

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Akshaj Homework\ICS4U - Major Project 1\build\assetsLoading\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

        #collecting user information
    def delete_details_entries():
        details_entries["firstname"].delete(0, "end")
        details_entries["lastname"].delete(0, "end")
        details_entries["age"].delete(0, "end")
        details_entries["gender"].delete(0, "end")
        details_entries["personality_traits"].delete(0, "end")
        details_entries["hobbies"].delete(0, "end")

    def log_out():
        show_frame("login")
        button_2.place_forget()
        delete_details_entries()
        frames["questions"].reset_questionsPage()
        

    loading_frame = frames["loading"]
    #dashboard_frame = frames["dashboard"]

    # Showing loading frame
    #show_frame("loading") #

    canvas = Canvas(
        loading_frame,
        bg = "#F9E699",
        height = 475,
        width = 714,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_text(
        175.0,
        116.0,
        anchor="nw",
        text="Successful!",
        fill="#974646",
        font=("Inter Bold", 68 * -1)
    )

    canvas.create_text(
        260.0,
        195.0,
        anchor="nw",
        text="Loading...",
        fill="#974646",
        font=("Inter", 43 * -1)
    )

    def show_logOut():

        button_2.place(
            x=266.0,
            y=0.0,
            width=178.0,
            height=38.0
        )
        #button_2.lift()


    button_image_2 = PhotoImage(
        file=relative_to_assets("log_out.png"))
    
    button_2 = Button(
        master=main_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: log_out(),
        relief="flat"
    )

    main_frame.photo_images = [
        button_image_2
    ]
    # button_2.place(
    #     x=456.0,
    #     y=440.0,
    #     width=178.0,
    #     height=38.0
    # )

    loading_heart1 = PhotoImage(
        file=relative_to_assets("loadingheart1.png"))
    loading1 = canvas.create_image(
        81.0,
        337.0,
        image=loading_heart1
    )

    loading_heart2 = PhotoImage(
        file=relative_to_assets("loadingheart2.png"))
    loading2 = canvas.create_image(
        218.0,
        337.0,
        image=loading_heart2
    )

    loading_heart3 = PhotoImage(
        file=relative_to_assets("loadingheart3.png"))
    loading3 = canvas.create_image(
        356.0,
        337.0,
        image=loading_heart3
    )

    loading_heart4 = PhotoImage(
        file=relative_to_assets("loadingheart4.png"))
    loading4 = canvas.create_image(
        493.0,
        337.0,
        image=loading_heart4
    )

    loading_heart5 = PhotoImage(
        file=relative_to_assets("loadingheart5.png"))
    loading5 = canvas.create_image(
        631.0,
        337.0,
        image=loading_heart5
    )

    loading_items = [loading1, loading2, loading3, loading4, loading5]
    for item in loading_items:
        canvas.itemconfig(item, state="hidden")

    #loading animation functions
    def show_loading_heart(index):
        if index == len(loading_items):
            if app_state["auth_mode"] == "login":
                canvas.after(750, lambda: show_frame("dashboard"))
                frames["dashboard"].load_dashboard()
            elif app_state["auth_mode"] == "signup":
                canvas.after(750, lambda: show_frame("details"))
                frames["details"].reset_profile_preview()
            canvas.after(850, show_logOut())
            return
        canvas.itemconfig(loading_items[index], state="normal")
        canvas.after(750, lambda index=index+1: show_loading_heart(index))

    def start_loading_animation():
        for item in loading_items:
            canvas.itemconfig(item, state="hidden")
        canvas.after(750, lambda: show_loading_heart(0))

    #**loading frame is where log out button is declared, not part of any specific frame, attached to main_frame
    loading_frame.start_loading_animation = start_loading_animation

    canvas.create_rectangle(
        0.0,
        226.0,
        228.0,
        226.0,
        fill="#974646",
        outline=""
    )

    canvas.create_rectangle(
        486.0,
        226.0,
        714.0,
        226.0,
        fill="#974646",
        outline=""
    )

    loading_frame.photo_images = [
        loading_heart1,
        loading_heart2,
        loading_heart3,
        loading_heart4,
        loading_heart5

    ]