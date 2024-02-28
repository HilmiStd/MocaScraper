import os
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cookies(username=None, password=None):
    while True:
        try:
            url = 'https://moca.unimma.ac.id/login/index.php'
            response = requests.get(url, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            logintoken_value = soup.find('input', {'name': 'logintoken'})['value']
            # print("Login Token: " + logintoken_value)

            cookie_header = response.headers.get('Set-Cookie')
            moodle_session_pertama = cookie_header.split('=')[1].split(';')[0]
            # print("Sesi moodle 1: " + moodle_session_pertama)

            payload = {
                'logintoken': logintoken_value,
                'username': username,
                'password': password
            }
            headers = {
                'Host': 'moca.unimma.ac.id',
                'Cookie': 'MoodleSession=' + moodle_session_pertama,
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
            }
            response2 = requests.post(url, data=payload, headers=headers, verify=False, allow_redirects=False)
            cookie_header = response2.headers.get('Set-Cookie')
            moodle_session_kedua = cookie_header.split('=')[1].split(';')[0]
            # print("Sesi moodle 2: " + moodle_session_kedua)
            return moodle_session_kedua
        except AttributeError:
            print(
                '\nHilmiStd/MocaScraper: Username atau password salah, pastikan sudah mengisi config.json dengan benar.')
            os._exit(1)
        except:
            pass
