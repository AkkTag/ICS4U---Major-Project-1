def setup_questions_page(window, main_frame, frames, show_frame, app_data):

    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
    from PIL import Image, ImageDraw, ImageTk

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Akshaj Homework\ICS4U - Major Project 1\ICS4U - Major Project 1\build\assetsQuestions\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # def hideTFButtons():
    #     pass

    # def hideMCQButtons():
    #     for i in ansTexts:
    #         canvas.itemconfig(i, state="hidden")

    #     for i in ansImgs:
    #         canvas.itemconfig(i, state="hidden")
    
    def hide_prev():
        button_1.place_forget()

    def show_prev():
        button_1.place(
            x=169.0,
            y=441.0,
            width=178.0,
            height=38.0
        )

    def hide_next():
        button_2.place_forget()
    
    def show_next():
        button_2.place(
            x=360.0,
            y=441.0,
            width=178.0,
            height=38.0
        )
    
    def hide_submit():
        button_3.place_forget()
    
    def show_submit():
        button_3.place(
            x=360.0,
            y=441.0,
            width=178.0,
            height=38.0
        )

    #question set
    questions = [
    {
        "question": "I enjoy designing long-term plans and theoretical models for how things should work.",
        "options": "like_level",
        "types": ["Architect", "Logician"]
    },
    {
        "question": "I like arguing ideas for fun, even if I don't fully agree with the side I'm defending.",
        "options": "like_level",
        "types": ["Debater"]
    },
    {
        "question": "I feel most confident when I am in charge and making important decisions for a group.",
        "options": "like_level",
        "types": ["Commander", "Executive"]
    },
    {
        "question": "I often think about how my actions affect people emotionally.",
        "options": "like_level",
        "types": ["Advocate", "Mediator"]
    },
    {
        "question": "I am motivated by having a clear purpose or mission in life.",
        "options": "like_level",
        "types": ["Advocate", "Protagonist"]
    },
    {
        "question": "I enjoy helping others resolve conflicts and find common ground.",
        "options": "like_level",
        "types": ["Mediator", "Consul"]
    },
    {
        "question": "I prefer practical solutions over abstract theories.",
        "options": "true_false",
        "types": [["Logistician", "Defender", "Executive"],   # True: practical
                  ["Architect", "Logician", "Debater"]]       # False: abstract thinkers
    },
    {
        "question": "I like following proven systems and routines to get things done efficiently.",
        "options": "like_level",
        "types": ["Logistician", "Executive"]
    },
    {
        "question": "I feel responsible for protecting traditions.",
        "options": "like_level",
        "types": ["Defender"]
    },
    {
        "question": "I naturally take charge in social or group situations.",
        "options": "like_level",
        "types": ["Protagonist", "Commander"]
    },
    {
        "question": "I enjoy hands-on problem solving, especially with tools or technology.",
        "options": "like_level",
        "types": ["Virtuoso"]
    },
    {
        "question": "I like taking risks and exploring new physical experiences (sports, travel, action).",
        "options": "like_level",
        "types": ["Adventurer"],
    },
    {
        "question": "I get excited about starting new projects or business ideas.",
        "options": "like_level",
        "types": ["Entrepreneur"],
    },
    {
        "question": "I gain energy from being around people rather than spending time alone.",
        "options": "true_false",
        "types": [["Entertainer", "Campaigner", "Protagonist"],   # True: extroverted energy
                  ["Architect", "Logician", "Mediator"]]           # False: introverted energy
    },
    {
        "question": "I prefer flexibility over rigid schedules.",
        "options": "like_level",
        "types": ["Adventurer", "Entrepreneur"],
    },
    {
        "question": "I trust emotions and values more than logic when making decisions.",
        "options": "true_false",
        "types": [["Advocate", "Mediator", "Protagonist", "Campaigner"],  # True: value-driven
                  ["Architect", "Logician", "Debater", "Commander"]]      # False: logic-driven
    },
    {
        "question": "I notice small details in my surroundings that others miss.",
        "options": "like_level",
        "types": ["Virtuoso", "Logistician"],
    },
    {
        "question": "I often inspire others with my enthusiasm and ideas.",
        "options": "like_level",
        "types": ["Campaigner", "Protagonist"],
    },
    {
        "question": "I prefer having a clear plan rather than improvising as I go.",
        "options": "true_false",
        "types": [["Architect", "Logistician", "Executive"],   # True: planners
                  ["Adventurer", "Entertainer", "Campaigner"]] # False: spontaneous
    }
    ]

    userAnswers = [None] * len(questions)

    #to populate the scores for each personality type based on user's answers to the questions
    personalityType_scores = {
        "Architect": 0,
        "Logician": 0,
        "Commander": 0,
        "Debater": 0,
        "Advocate": 0,
        "Mediator": 0,
        "Protagonist": 0,
        "Campaigner": 0,
        "Logistician": 0,
        "Defender": 0,
        "Executive": 0,
        "Consul": 0,
        "Virtuoso": 0,
        "Adventurer": 0,
        "Entrepreneur": 0,
        "Entertainer": 0
    }

    def select_answer(index):
        for i in range(len(rects)):
            if i == index:
                canvas.itemconfig(rects[i], state="normal")
            else:
                canvas.itemconfig(rects[i], state="hidden")

        userAnswers[qCurrent] = index

    

    def submit_test():

        nonlocal qCurrent

        user = app_data["current_user"]
        #print("Current user:", app_data.get("current_user"))
        #data = app_data["users"][user]
        data = app_data["users"].get(user, {})

        data["test_completed"] = True

        userAnswers_str = []
        for i in range(len(userAnswers)):
            if not userAnswers[i] == None:
                index = userAnswers[i]
                userAnswers_str.append(canvas.itemcget(ansTexts[index], "text"))

        data["answers"] = ", ".join(userAnswers_str)

        data["personality_scores"] = personalityType_scores

        newLine = ""
        index = None
        found = False

        for i in range(len(userAnswers_str)):
            
            for j in questions[i]["types"]:
                if userAnswers_str[i] == "Strongly Agree":
                    personalityType_scores[j] += 4
                elif userAnswers_str[i] == "Agree":
                    personalityType_scores[j] += 3
                elif userAnswers_str[i] == "Disagree":
                    personalityType_scores[j] += 2
                elif userAnswers_str[i] == "Strongly Disagree":
                    personalityType_scores[j] += 1
        
        personalityData_str = ", ".join([f"{ptype}: {score}" for ptype, score in personalityType_scores.items()])

        with open(Path(__file__).parent / "personalInfo.txt", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                splitted = lines[i].strip().split(" | ")

                if splitted[0] == user.strip():
                    found = True
                    #splitted[1] = " # ".join([data["firstname"], data["lastname"], data["age"], data["gender"], data["personality_traits"], data["hobbies"], str(data["test_completed"]), data["answers"]])
                    splitted[1] = " # ".join([data["firstname"], data["lastname"], str(data["age"]), data["gender"], data["personality_traits"], data["hobbies"], str(data["test_completed"]), str(data["profile_pic"]), data["answers"], personalityData_str])
                    newLine = " | ".join(splitted) + "\n"
                    lines[i] = newLine
                    #index = i

            if not found:
                print("Error: user not found in personalInfo.txt")

        with open(Path(__file__).parent / "personalInfo.txt", "w") as g:
            
            for i in range(len(lines)):
                g.write(lines[i])

        print("Test submitted.")
        qCurrent = 0

        show_frame("tested")


    def hide_otherRects(rect):
        for i in rects:
            if not rect == i:
                canvas.config(i, state="hidden")

    rects = []

    def resetRects():
        # nonlocal rects
        # for i in rects:
        #     canvas.itemconfig(i, state="hidden")

        for rect in rects:
            canvas.itemconfig(rect, state="hidden")

    def on_click(event):

        clicked_items = canvas.find_overlapping(event.x, event.y, event.x, event.y)

        # check if user clicked an answer
        for item in clicked_items:
            tags = canvas.gettags(item)

            is_answer = False

            for tag in tags:
                if tag.startswith("answer"):
                    is_answer = True
                    break

            if is_answer:
                return # clicked an answer box, function terminates

        resetRects()
        userAnswers[qCurrent] = None


    #types of questions and the corresponding answer options
    answer_sets = {
    "like_level": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    "true_false": ["True", "False"]
    }
    

    qCurrent = 0

    

    def reset_questionsPage():
        nonlocal qCurrent, userAnswers

        # 1. Reset logic
        qCurrent = 0
        userAnswers = [None] * len(questions)


    if qCurrent == 0:
        resetRects()

    def load_question():
        
        resetRects() #hides all rectangles (resets them)


        q = questions[qCurrent]

        canvas.itemconfig(questionID, text=q["question"])

        if qCurrent == 0:
            hide_prev()
        else:
            show_prev()

        if qCurrent == 18:
            hide_next()
            show_submit()
        else:
            hide_submit()
            show_next()
            
        if q["options"] == "like_level":

            canvas.itemconfig(img1ID, state="normal", tags="answer1")
            canvas.itemconfig(ans1ID, state="normal", tags="answer1")

            canvas.itemconfig(img2ID, state="normal", tags="answer2")
            canvas.itemconfig(ans2ID, state="normal", tags="answer2")

            canvas.itemconfig(img3ID, state="normal", tags="answer3")
            canvas.itemconfig(ans3ID, state="normal", tags="answer3")

            canvas.itemconfig(img4ID, state="normal", tags="answer4")
            canvas.itemconfig(ans4ID, state="normal", tags="answer4")

            canvas.itemconfig(img5ID, state="hidden", tags="answer5")
            canvas.itemconfig(ans5ID, state="hidden", tags="answer5")

            canvas.itemconfig(img6ID, state="hidden", tags="answer6")
            canvas.itemconfig(ans6ID, state="hidden", tags="answer6")

            for option in range(len(answer_sets["like_level"])):
                canvas.itemconfig(ansTexts[option], text=answer_sets["like_level"][option])
        
        elif q["options"] == "true_false":

            canvas.itemconfig(img1ID, state="hidden", tags="answer1")
            canvas.itemconfig(ans1ID, state="hidden", tags="answer1")

            canvas.itemconfig(img2ID, state="hidden", tags="answer2")
            canvas.itemconfig(ans2ID, state="hidden", tags="answer2")

            canvas.itemconfig(img3ID, state="hidden", tags="answer3")
            canvas.itemconfig(ans3ID, state="hidden", tags="answer3")

            canvas.itemconfig(img4ID, state="hidden", tags="answer4")
            canvas.itemconfig(ans4ID, state="hidden", tags="answer4")

            canvas.itemconfig(img5ID, state="normal", tags="answer5")
            canvas.itemconfig(ans5ID, state="normal", tags="answer5")

            canvas.itemconfig(img6ID, state="normal", tags="answer6")
            canvas.itemconfig(ans6ID, state="normal", tags="answer6")

            canvas.itemconfig(ansTexts[4], text=answer_sets["true_false"][0])
            canvas.itemconfig(ansTexts[5], text=answer_sets["true_false"][1])


    def prev_question():
        nonlocal qCurrent

        qCurrent -= 1

        load_question()

        for i in range(len(ansTexts)):
            if userAnswers[qCurrent] == i:
                canvas.itemconfig(rects[i], state="normal")

    def next_question():

        nonlocal qCurrent

        qCurrent += 1

        load_question()

        # restore next question if exists
        if not userAnswers[qCurrent] == None:
            canvas.itemconfig(rects[userAnswers[qCurrent]], state="normal")


    questions_frame = frames["questions"]

    canvas = Canvas(
        questions_frame,
        bg = "#F9E699",
        height = 475,
        width = 714,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
        33.0,
        89.0,
        673.0,
        199.0,
        fill="#FFFFFF",
        outline="")

    
    img1 = Image.new("RGBA", (314, 87), (0, 0, 0, 0))
    draw1 = ImageDraw.Draw(img1)

    draw1.rectangle(
        [0, 0, 314, 87],
        fill=(255, 0, 0, 128)  # alpha = 128/255
    )

    tk_img1 = ImageTk.PhotoImage(img1)
    questions_frame.tk_img1 = tk_img1
    img1ID = canvas.create_image(33.0, 224.0, image=tk_img1, anchor="nw", tags="answer1")

    rect1ID = canvas.create_rectangle(
        28.0,
        219.0,
        352.0,
        316.0,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect1ID)
    
    img2 = Image.new("RGBA", (313, 87), (0, 0, 0, 0))
    draw2 = ImageDraw.Draw(img2)

    draw2.rectangle(
        [0, 0, 313, 87],
        fill=(12, 255, 0, 128)  # alpha = 128/255
    )

    tk_img2 = ImageTk.PhotoImage(img2)
    questions_frame.tk_img2 = tk_img2
    img2ID = canvas.create_image(360.0, 224.0, image=tk_img2, anchor="nw", tags="answer2")

    rect2ID = canvas.create_rectangle(
        355.0,
        219.0,
        678.0,
        316.0,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect2ID)


    img3 = Image.new("RGBA", (314, 87), (0, 0, 0, 0))
    draw3 = ImageDraw.Draw(img3)

    draw3.rectangle(
        [0, 0, 314, 87],
        fill=(0, 80, 255, 128)  # alpha = 128/255
    )

    tk_img3 = ImageTk.PhotoImage(img3)
    questions_frame.tk_img3 = tk_img3
    img3ID = canvas.create_image(33.0, 327.0, image=tk_img3, anchor="nw", tags="answer3")

    rect3ID = canvas.create_rectangle(
        28.0,
        322.0,
        352.0,
        419.0,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect3ID)


    img4 = Image.new("RGBA", (313, 87), (0, 0, 0, 0))
    draw4 = ImageDraw.Draw(img4)

    draw4.rectangle(
        [0, 0, 313, 87],
        fill=(208, 50, 192, 128)  # alpha = 128/255
    )

    tk_img4 = ImageTk.PhotoImage(img4)
    questions_frame.tk_img4 = tk_img4
    img4ID = canvas.create_image(360.0, 327.0, image=tk_img4, anchor="nw", tags="answer4")

    rect4ID = canvas.create_rectangle(
        355.0,
        322.0,
        678.0,
        419.0,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect4ID)

    img5 = Image.new("RGBA", (314, 87), (0, 0, 0, 0))
    draw5 = ImageDraw.Draw(img5)

    draw5.rectangle(
        [0, 0, 314, 87],
        fill=(255, 0, 0, 128)  # alpha = 128/255
    )

    tk_img5 = ImageTk.PhotoImage(img5)
    questions_frame.tk_img5 = tk_img5
    img5ID = canvas.create_image(33.0, 275.5, image=tk_img5, anchor="nw", tags="answer5")
    
    rect5ID = canvas.create_rectangle(
        28.0,
        270.5,
        352.0,
        367.5,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect5ID)

    img6 = Image.new("RGBA", (314, 87), (0, 0, 0, 0))
    draw6 = ImageDraw.Draw(img6)

    draw6.rectangle(
        [0, 0, 314, 87],
        fill=(0, 80, 255, 128) #128 is the alpha value for transparency
    )

    tk_img6 = ImageTk.PhotoImage(img6)
    questions_frame.tk_img6 = tk_img6
    img6ID = canvas.create_image(360.0, 275.5, image=tk_img6, anchor="nw", tags="answer6")

    rect6ID = canvas.create_rectangle(
        355.0,
        270.5,
        678.0,
        367.5,
        state="hidden",
        outline="#974646",
        width=3
    )

    canvas.tag_lower(rect6ID)

    ansImgs = [img1ID, img2ID, img3ID, img4ID, img5ID, img6ID]

    button_image_1 = PhotoImage(
        file=relative_to_assets("previous.png"))

    button_1 = Button(
        master=questions_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: prev_question(),
        relief="flat"
    )
    button_1.place(
        x=169.0,
        y=441.0,
        width=178.0,
        height=38.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("next.png"))

    button_2 = Button(
        master=questions_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_question(),
        relief="flat"
    )
    button_2.place(
        x=360.0,
        y=441.0,
        width=178.0,
        height=38.0
    )

    button_image_3 = PhotoImage(
    file=relative_to_assets("submit.png"))
    
    button_3 = Button(
        master=questions_frame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit_test(),
        relief="flat"
    )
    
    button_3.place(
        x=360.0,
        y=441.0,
        width=178.0,
        height=38.0
    )

    questionID = canvas.create_text(
        58.0,
        126.0,
        anchor="nw",
        text="The question.",
        width=615,
        justify="center",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    ans1ID = canvas.create_text(
        58.0,
        250.0,
        anchor="nw",
        text="fff",
        tags="answer1",
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    ans2ID = canvas.create_text(
        381.0,
        250.0,
        anchor="nw",
        text="fff",
        tags="answer2",
        fill="#000000",
        font=("Inter", 30 * -1)
    )


    ans3ID = canvas.create_text(
        58.0,
        353.0,
        anchor="nw",
        text="fff",
        tags="answer3",
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    ans4ID = canvas.create_text(
        381.0,
        353.0,
        anchor="nw",
        text="fff",
        tags="answer4",
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    ans5ID = canvas.create_text(
        58.0,
        301.5,
        anchor="nw",
        text="fff",
        tags="answer5",
        #wraplength=
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    ans6ID = canvas.create_text(
        381.0,
        301.5,
        # 58.0,
        # 301.5,
        anchor="nw",
        text="fff",
        tags="answer6",
        #wraplength=
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    canvas.tag_bind("answer1", "<Button-1>", lambda e: select_answer(0))
    canvas.tag_bind("answer2", "<Button-1>", lambda e: select_answer(1))
    canvas.tag_bind("answer3", "<Button-1>", lambda e: select_answer(2))
    canvas.tag_bind("answer4", "<Button-1>", lambda e: select_answer(3))
    canvas.tag_bind("answer5", "<Button-1>", lambda e: select_answer(4))
    canvas.tag_bind("answer6", "<Button-1>", lambda e: select_answer(5))

    canvas.bind("<Button-1>", on_click)

    ansTexts = [ans1ID, ans2ID, ans3ID, ans4ID, ans5ID, ans6ID]
    rects.extend([rect1ID, rect2ID, rect3ID, rect4ID, rect5ID, rect6ID])
    
    questions_frame.photo_images = [
        button_image_1,
        button_image_2,
        button_image_3
    ]

    questions_frame.load_question = load_question
    questions_frame.reset_questionsPage = reset_questionsPage
