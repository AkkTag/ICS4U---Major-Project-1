from common import setup_window, convert_scores
from login import setup_login_page
from loading import setup_loading_page
from details import setup_details_page
from dashboard import setup_dashboard_page
from matches import setup_matches_page
from questions import setup_questions_page
from tested import setup_tested_page
from pathlib import Path

#from existing information in personalInfo.txt, loading the information for every user befure app starts
def load_users_from_file(app_data):
    app_data["users"] = {}


    with open(Path(__file__).parent / "personalInfo.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            user, info = line.split(" | ")
            fields = info.split(" # ")
            # fields = line.split(",")

            app_data["users"][user] = {
                "firstname": fields[0],
                "lastname": fields[1],
                "age": int(fields[2]),
                "gender": fields[3],
                "personality_traits": fields[4],
                "hobbies": fields[5],
                "test_completed": fields[6] == "True",
                "profile_pic": None,  # Placeholder, will be updated when details page is loaded
                "answers": fields[8] if len(fields) > 8 else "",
                "personality_scores": convert_scores(fields[9]) if len(fields) > 9 else {}
            }

window, main_frame, frames, show_frame = setup_window()

app_state = {
    "auth_mode": None  # "login" or "signup"
}

app_data = {
    "users": {},          # username → user info
    "current_user": None  # currently logged-in username
    #"test"
}

load_users_from_file(app_data)

#setting up each frame of the app
logged_in = setup_login_page(window, main_frame, frames, show_frame, app_state, app_data) 

details_entries = setup_details_page(window, main_frame, frames, show_frame, app_data)

setup_dashboard_page(window, main_frame, frames, show_frame, app_data, details_entries)

setup_matches_page(window, main_frame, frames, show_frame, app_data)
setup_questions_page(window, main_frame, frames, show_frame, app_data)

setup_tested_page(window, main_frame, frames, show_frame, app_data)

setup_loading_page(window, main_frame, frames, show_frame, details_entries, app_state, app_data)

window.resizable(False, False)
window.mainloop()