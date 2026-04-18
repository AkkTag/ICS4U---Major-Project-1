#another very important page of the app
def setup_matches_page(window, main_frame, frames, show_frame, app_data):

    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
    import common

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Akshaj Homework\ICS4U - Major Project 1\ICS4U - Major Project 1\build\assetsMatches\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    
    def load_matches():
        user = app_data["current_user"]
        data = app_data["users"].get(user, {})

        print("User:", user)
        print("Data:", data)
        print("Test completed:", data["test_completed"])

        # for username, user_data in app_data["users"].items():
        #     if not user_data.get("personality_scores"):
        #         user_data["personality_scores"] = common.convert_scores(user_data["answers"])

        if data["test_completed"] == False:
            show_empty_state()

        else:
            show_results_state()
            matches = find_matches(app_data["current_user"], app_data)
            fill_matches(matches)

    def show_empty_state():
        results_state.place_forget()
        empty_state.place(x=0, y=0, width=714, height=475)
        empty_state.lift()

    def show_results_state():
        empty_state.place_forget()
        results_state.place(x=0, y=0, width=714, height=475)
        results_state.lift()
        
    #return to dashboard
    def db_return():
        show_frame("dashboard")
        frames["dashboard"].load_dashboard()

    def take_test():
        show_frame("questions")
        frames["questions"].load_question()
        
    def top_traits(scores_dict):
        n = 5
        sorted_traits = sorted(scores_dict.items(), key=lambda pair: pair[1], reverse=True)
        
        return [trait for trait, score in sorted_traits[:n]]
    


    def is_valid_match(user1, user2):

        if not(user1["gender"] == user2["gender"]) and abs(user1["age"] - user2["age"]) <= 4: #checking gender AND age difference as criteria for a valid match
            return True
        return False
    

    def compatibility_score(user1, user2):
        scores1 = user1["personality_scores"]
        scores2 = user2["personality_scores"]
    
        traits1 = top_traits(scores1)
        traits2 = top_traits(scores2)
        
        common_traits = [trait for trait in traits1 if trait in traits2]
        
        match_count = len(common_traits)
        
        total_score = 0
        for trait in common_traits:
            total_score += scores1.get(trait, 0) + scores2.get(trait, 0)
    
        return match_count, total_score

    #actual function called to find the user's matches
    def find_matches(current_username, app_data):
        scores = []
        current_atts = app_data["users"][current_username]
        
        for username, other_atts in app_data["users"].items():
            
            # Skip current user (self)
            if username == current_username:
                continue
            
            # Apply conditions
            if not is_valid_match(current_atts, other_atts):
                continue
            
            # Compute compatibility
            match_count, total_score = compatibility_score(current_atts, other_atts)
            
            if match_count > 0: #only consider users with at least one shared top trait as matches
                scores.append((username, match_count, total_score))
        

        scores.sort(key=lambda x: (x[1], x[2]), reverse=True) #sorting priority: by match count first, then by total score as a tiebreaker 
        
        #level of match assigned here
        matches = {
            "premium": scores[0] if len(scores) > 0 else None, #checking if at least one match exists before accessing the first element
            "star": scores[1] if len(scores) > 1 else None, #checking if at least two matches exist before accessing the second element
            "standard": scores[2] if len(scores) > 2 else None #checking if at least three matches exist before accessing the third element
        }
    
        return matches

    #to update the UI, filling in the fields with the match's information
    def fill_matches(user_data):

        user1 = user_data["premium"][0] if user_data["premium"] else None
        user2 = user_data["star"][0] if user_data["star"] else None
        user3 = user_data["standard"][0] if user_data["standard"] else None

        if user1:
            results_canvas.itemconfig(texts[0], text=app_data["users"][user1]["firstname"])
            results_canvas.itemconfig(texts[1], text=app_data["users"][user1]["lastname"])
            results_canvas.itemconfig(texts[2], text=str(app_data["users"][user1]["age"]))
            results_canvas.itemconfig(texts[3], text=app_data["users"][user1]["gender"])
            results_canvas.itemconfig(texts[4], text=app_data["users"][user1]["personality_traits"])
            results_canvas.itemconfig(texts[5], text=app_data["users"][user1]["hobbies"])

        if user2:
            results_canvas.itemconfig(texts[6], text=app_data["users"][user2]["firstname"])
            results_canvas.itemconfig(texts[7], text=app_data["users"][user2]["lastname"])
            results_canvas.itemconfig(texts[8], text=str(app_data["users"][user2]["age"]))
            results_canvas.itemconfig(texts[9], text=app_data["users"][user2]["gender"])
        
        if user3:
            results_canvas.itemconfig(texts[10], text=app_data["users"][user3]["firstname"])
            results_canvas.itemconfig(texts[11], text=app_data["users"][user3]["lastname"])
            results_canvas.itemconfig(texts[12], text=str(app_data["users"][user3]["age"]))
            results_canvas.itemconfig(texts[13], text=app_data["users"][user3]["gender"])

    #matches frame
    matches_frame = frames["matches"]
    
    #two different states within matches_frame
    empty_state = Frame(matches_frame, bg="#F9E699")
    results_state = Frame(matches_frame, bg="#F9E699")

    empty_canvas = Canvas(
        empty_state,
        bg = "#F9E699",
        height = 475,
        width = 714,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    empty_canvas.place(x = 0, y = 0)

    results_canvas = Canvas(
        results_state,
        bg = "#F9E699",
        height = 475,
        width = 714,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    results_canvas.place(x = 0, y = 0)

    noMatches_msg = Label(
        master=empty_state,
        text="No matches yet! Start the test to realize your profile and see who you’re compatible with!",
        wraplength=700,
        fg="#974646",
        bg="#F9E699",
        font=("Inter", 32 * -1),
    )
    
    noMatches_msg.place(
        x=10.0,
        y=125.0,
        width=700.0,
        height=150.0
    )
 

    button_image_1 = PhotoImage(
        file=relative_to_assets("back.png"))
    
    back_to_db = Button(
        master=empty_state,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: db_return(),
        relief="flat"
    )

    back_to_db.place(
        x=86.0,
        y=297.0,
        width=253.0,
        height=80.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("start_test.png"))
    
    start_test = Button(
        master=empty_state,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: take_test(),
        relief="flat"
    )
    
    start_test.place(
        x=369.0,
        y=297.0,
        width=253.0,
        height=80.0
    )

    

    empty_canvas.create_line(
        0,
        426.5,
        338.5,
        426.5,
        width=2,
        fill="#974646",
    )

    # circle at end
    r = 6 # radius
    x1 = 337
    y1 = 427

    empty_canvas.create_oval(
        x1 - r,
        y1 - r,
        x1 + r,
        y1 + r,
        fill="#974646",
        outline="",
    )

    empty_canvas.create_line(
        369.0,
        426.5,
        714.0,
        426.5,
        width=2,
        fill="#974646",
    )

    x2 = 367
    y2 = 427

    empty_canvas.create_oval(
        x2 - r,
        y2 - r,
        x2 + r,
        y2 + r,
        fill="#974646",
        outline="",
        #tags="empty"
    )
    
    results_canvas.create_text(
        227.0,
        57.0,
        anchor="nw",
        text="Your Matches",
        fill="#974646",
        font=("Inter Bold", 40 * -1, "bold"),
        tags="results"
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))

    entry_bg_1 = results_canvas.create_image(
        200.0,
        293.0,
        image=entry_image_1,
        tags="results"
    )
    
    entry_1 = Entry(
        master=results_state,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0
    )

    entry_1.place(
        x=62.0,
        y=157.0,
        width=276.0,
        height=270.0
    )

    entry_1.lower()

    results_canvas.create_rectangle(
        42.0,
        139.0,
        358.0,
        174.0,
        fill="#974646",
        outline="",
        tags="results"
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))

    entry_bg_2 = results_canvas.create_image(
        536.0,
        210.5,
        image=entry_image_2,
        tags="results"
    )

    entry_2 = Entry(
        master=results_state,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0
    )

    entry_2.place(
        x=417.0,
        y=156.0,
        width=238.0,
        height=107.0
    )

    entry_2.lower()

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))

    entry_bg_3 = results_canvas.create_image(
        536.0,
        374.5,
        image=entry_image_3,
        tags="results"
    )

    entry_3 = Entry(
        master=results_state,
        bd=0,
        bg="#F9FFA9",
        fg="#000716",
        highlightthickness=0
    )

    entry_3.place(
        x=417.0,
        y=320.0,
        width=238.0,
        height=107.0
    )

    entry_3.lower()

    results_canvas.create_text(
        134.0,
        144.0,
        anchor="nw",
        text="Premium Match",
        fill="#FFFFFF",
        font=("Inter Medium", 20 * -1),
        tags="results"
    )

    results_canvas.create_rectangle(
        397.0,
        139.0,
        675.0,
        172.0,
        fill="#974646",
        outline="",
        tags="results"
    )

    results_canvas.create_text(
        487.0,
        144.0,
        anchor="nw",
        text="Star Match",
        fill="#FFFFFF",
        font=("Inter Medium", 20 * -1),
        tags="results"
    )

    results_canvas.create_rectangle(
        397.0,
        303.0,
        675.0,
        336.0,
        fill="#974646",
        outline="",
        tags="results"
    )

    results_canvas.create_text(
        467.0,
        308.0,
        anchor="nw",
        text="Standard Match",
        fill="#FFFFFF",
        font=("Inter Medium", 20 * -1),
        tags="results"
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("back2.png"))

    back_to_db2 = Button(
        master=results_state,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: db_return(),
        relief="flat"
    )
    back_to_db2.place(
        x=198.0,
        y=446.0,
        width=102.80792236328125,
        height=32
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("retake_test.png"))

    retake_test = Button(
        master=results_state,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: take_test(),
        relief="flat"
    )
    retake_test.place(
        x=326.0,
        y=446.0,
        width=198.0,
        height=32
    )


    results_canvas.create_rectangle(
        55.0,
        191.0,
        190.0,
        247.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        55.0,
        271.0,
        190.0,
        327.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        209.0,
        271.0,
        344.0,
        327.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        55.0,
        352.0,
        190.0,
        408.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        209.0,
        352.0,
        344.0,
        408.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        209.0,
        191.0,
        344.0,
        247.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        411.0,
        183.0,
        529.0,
        211.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        543.0,
        183.0,
        661.0,
        211.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        411.0,
        223.0,
        529.0,
        251.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        543.0,
        223.0,
        661.0,
        251.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        411.0,
        347.0,
        529.0,
        375.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        543.0,
        347.0,
        661.0,
        375.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        411.0,
        387.0,
        529.0,
        415.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    results_canvas.create_rectangle(
        543.0,
        387.0,
        661.0,
        415.0,
        fill="#FFFFFF",
        outline="#974646",
        width=2,
        #tags="results"
    )

    premium_fn = results_canvas.create_text(
        63.0,
        203.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    premium_ln = results_canvas.create_text(
        217.0,
        203.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    premium_age = results_canvas.create_text(
        63.0,
        282.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    premium_gender = results_canvas.create_text(
        217.0,
        282.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    premium_pt = results_canvas.create_text(
        63.0,
        364.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    premium_hobbies = results_canvas.create_text(
        217.0,
        364.0,
        width=127.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    star_fn = results_canvas.create_text(
        418.0,
        186.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    star_ln = results_canvas.create_text(
        550.0,
        186.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    star_age = results_canvas.create_text(
        418.0,
        226.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    star_gender = results_canvas.create_text(
        550.0,
        226.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    standard_fn = results_canvas.create_text(
        419.0,
        350.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    standard_ln = results_canvas.create_text(
        550.0,
        350.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    standard_age = results_canvas.create_text(
        419.0,
        390.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    standard_gender = results_canvas.create_text(
        550.0,
        390.0,
        width=110.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 20 * -1),
        #tags="results"
    )

    texts = [premium_fn, premium_ln, premium_age, premium_gender, premium_pt, premium_hobbies,
             star_fn, star_ln, star_age, star_gender, standard_fn, standard_ln, standard_age, standard_gender]
    
    matches_frame.photo_images = [
        button_image_1,
        button_image_2,
        button_image_3,
        button_image_4
    ]

    


    matches_frame.load_matches = load_matches