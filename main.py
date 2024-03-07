import argparse
import json
import os
import time
import threading
from helper import login,asset,presence

def initialize_session(username, password, courses_data, dict, event):
    session = login.cookies(username, password)
    user_name = asset.user_name(session)
    courses = courses_data
    course_name = []
    for course in courses:
        course_name.append(asset.course_name(session, course))

    indices_to_remove = []
    for i, name in enumerate(course_name):
        if name == False:
            indices_to_remove.append(i)
    alert_course_id = []
    for index in sorted(indices_to_remove, reverse=True):
        alert_course_id.append(courses[index])
        del course_name[index]
        del courses[index]

    dict["session"] = session
    dict["user_name"] = user_name
    dict["courses"] = courses
    dict["course_name"] = course_name
    dict["alert_course_id"] = alert_course_id
    event.set()


def main(username, password, courses_data):
    data = {}

    event = threading.Event()
    my_thread = threading.Thread(target=initialize_session, args=(username, password, courses_data, data, event))
    my_thread.start()
    asset.loading_animation(event)
    my_thread.join()

    session = data["session"]
    user_name = data["user_name"]
    courses = data["courses"]
    course_name = data["course_name"]
    alert_course_id = data["alert_course_id"]

    start_time = time.time()
    max_duration = 4 * 60 * 60

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        try:
            print("\033[1;32m" + f'''  __  __                 ____                                 
 |  \/  | ___   ___ __ _/ ___|  ___ _ __ __ _ _ __   ___ _ __ 
 | |\/| |/ _ \ / __/ _` \___ \ / __| '__/ _` | '_ \ / _ \ '__|
 | |  | | (_) | (_| (_| |___) | (__| | | (_| | |_) |  __/ |   
 |_|  |_|\___/ \___\__,_|____/ \___|_|  \__,_| .__/ \___|_| ''' + "\033[0m" + "v1.0" + "\n"
                  + "\033[1;32m" + "                                             |_|               " + "\n" + "\033[0m"
                  )

            if len(alert_course_id) > 0:
                print(
                    "\033[1;31m" + f"Alert: Ada id_courses yang tidak valid pada config.json [{', '.join(map(str, alert_course_id))}]." + "\033[0m")
            print(
                "\033[1;32m" + "Manual" + "\033[0m" + ": Masukan nomor course untuk presensi & tekan CTRL + C untuk mengakhiri script.")
            print("\033[1;32m" + "Pengguna" + "\033[0m" + ": " + user_name + ".\n")

            for i in range(len(course_name)):
                print(f"{i + 1}. {course_name[i]}")

            choose = int(input("\033[1;32m" + "\nPilih course untuk presensi" + "\033[0m" + ": "))
            if choose - 1 < len(courses) and choose - 1 >= 0 and courses[choose - 1] != "":
                # reset cookies setelah 4 jam
                elapsed_time = time.time() - start_time
                if elapsed_time >= max_duration:
                    session = login.cookies(username, password)
                    start_time = time.time()
                event = threading.Event()
                my_thread = threading.Thread(target=presence.presence,
                                             args=(courses[choose - 1], session, event))
                my_thread.start()
                asset.loading_animation(event)
                my_thread.join()
                # presence.presence(courses[choose - 1], session)
            else:
                raise ValueError
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            print("HilmiStd/MocaScraper: Script diakhiri oleh user.")
            os._exit(1)
        except:
            pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Presensi pada kursus tertentu atau akses CLI UI")
    parser.add_argument("id_courses", nargs="?", help="id courses yang ingin dipresensi")
    args = parser.parse_args()
    try:
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_file_path, 'r') as file:
            json_data = file.read()
        data = json.loads(json_data)

        try:
            telegram = data['telegram']
        except:
            telegram = None

        username = data['username']
        password = data['password']
        data = data['id_courses']
    except:
        print("HilmiStd/MocaScraper: Pastikan isi config.json sudah benar sebelum memulai script.")
        os._exit(1)

    if args.id_courses:
        try:
            session = login.cookies(username, password)
            if telegram:
                presence.presence(args.id_courses, session, telegram=telegram)
            else:
                presence.presence(args.id_courses, session)
        except Exception as e:
            print("HilmiStd/MocaScraper:", e)

    else:
        try:
            main(username, password, data)
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            print("HilmiStd/MocaScraper: Script diakhiri oleh user.")
            os._exit(1)

