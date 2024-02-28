import time
import requests
from bs4 import BeautifulSoup


def course_name(session, id_course):
    while True:
        try:
            cookies = {
                'MoodleSession': session
            }
            response = requests.get(f'https://moca.unimma.ac.id/course/view.php?id={id_course}', cookies=cookies,
                                    verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            heading = soup.find('h1', class_='h2').text
            if heading == "My Online Class" or heading == "":
                return False
            return heading
        except AttributeError:
            return False
        except:
            pass


def user_name(session):
    while True:
        try:
            cookies = {
                'MoodleSession': session
            }
            response = requests.get('https://moca.unimma.ac.id/admin/index.php', cookies=cookies, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')

            login_info = soup.find('div', class_='logininfo')
            if login_info:
                return login_info.a.text
        except AttributeError:
            return False
        except:
            pass

def loading_animation(event):
    while not event.is_set():
        for char in [".","..","...","   "]:
            print('\rHilmiStd/MocaScraper: Tunggu sebentar, sedang memproses permintaan ' + char,
                  end='', flush=True)
            time.sleep(0.1)
