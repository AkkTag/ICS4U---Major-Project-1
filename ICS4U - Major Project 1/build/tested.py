def setup_tested_page(window, main_frame, frames, show_frame, app_data):

    from pathlib import Path

    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Akshaj Homework\ICS4U - Major Project 1\ICS4U - Major Project 1\build\assetsTested\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back_to_dashboard():
        show_frame("dashboard")
        frames["dashboard"].load_dashboard()

    tested_frame = frames["tested"]

    canvas = Canvas(
    tested_frame,
    bg = "#F9E699",
    height = 475,
    width = 714,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_text(
        208.0,
        84.0,
        anchor="nw",
        text="Test Complete!",
        fill="#974646",
        font=("Inter Bold", 40 * -1, "bold")
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("returnDashboard.png"))

    button_1 = Button(
        master=tested_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_dashboard(),
        relief="flat"
    )

    button_1.place(
        x=230.0,
        y=298.0,
        width=253.0,
        height=80.0
    )

    canvas.create_line(
        0.0,
        426.5,
        338.5,
        426.5,
        width=2,
        fill="#974646",
        #outline=""
    )

    # circle at end
    r = 6 # radius
    x1 = 337
    y1 = 427

    canvas.create_oval(
        x1 - r,
        y1 - r,
        x1 + r,
        y1 + r,
        fill="#974646",
        outline=""
    )

    canvas.create_line(
        369.0,
        426.5,
        714.0,
        426.5,
        width=2,
        fill="#974646",
    )

    x2 = 367
    y2 = 427

    canvas.create_oval(
        x2 - r,
        y2 - r,
        x2 + r,
        y2 + r,
        fill="#974646",
        outline=""
    )

    canvas.create_text(
        93.0,
        169.0,
        width=598.0,
        anchor="nw",
        justify="center",
        text="You may return to your Dashboard by clicking the button below.",
        fill="#974646",
        font=("Inter", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("heart1Left.png"))

    image_1 = canvas.create_image(
        96.0,
        318.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("heart2Right.png"))

    image_2 = canvas.create_image(
        616.0,
        318.0,
        image=image_image_2
    )

    tested_frame.photo_images = [
        button_image_1,
        image_image_1,
        image_image_2
    ]
