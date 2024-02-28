import os
import time
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def presence(id_course, session, event=None):
    while True:
        try:
            # ke 3
            url = f'https://moca.unimma.ac.id/course/view.php?id={id_course}'
            cookies = {
                'MoodleSession': session
            }
            response = requests.get(url, cookies=cookies, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            link_elem = soup.find('a', href=lambda
                href: href and 'https://moca.unimma.ac.id/mod/attendance/view.php' in href)
            href_value = link_elem['href']
            # print("Link attendance view: " + href_value)
            break
        except TypeError:
            if event:
                event.set()
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
            print("\033[1;33m" + "HilmiStd/MocaScraper:", f"Belum enroll course ini, kunjungi {url} untuk enroll.",
                  "\033[0m")
            return
        except:
            pass

    while True:
        try:
            # ke 4
            response = requests.get(href_value, cookies=cookies, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            link_elem = soup.find('a', href=lambda
                href: href and 'https://moca.unimma.ac.id/mod/attendance/attendance.php' in href)
            href_value_2 = link_elem['href']
            # print("Link attendance form: " + href_value_2)
            break

        except TypeError:
            if event:
                event.set()
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
            print("\033[1;33m" + "HilmiStd/MocaScraper:", f"Belum ada presensi di course ini.",
                  "\033[0m")
            return
        except:
            pass

    while True:
        try:
            # ke 5
            response = requests.get(href_value_2, cookies=cookies)
            soup = BeautifulSoup(response.text, 'html.parser')

            # validasi input present or late
            keywords = ['Present', 'Hadir', 'Late', 'Terlambat']

            for keyword in keywords:
                span_elem = soup.find('span', class_='statusdesc', string=keyword)
                if span_elem:
                    break

            if span_elem is None:
                raise AttributeError

            status = span_elem.find_previous('input')['value']
            sessid = soup.find('input', {'name': 'sessid'})['value']
            sesskey = soup.find('input', {'name': 'sesskey'})['value']

            payload = {
                "sessid": sessid,
                "sesskey": [sesskey, sesskey],
                "_qf__mod_attendance_form_studentattendance": "1",
                "mform_isexpanded_id_session": "1",
                "status": status,
                "submitbutton": "Save changes"
            }

            headers = {
                'Host': 'moca.unimma.ac.id',
                'Cookie': 'MoodleSession=' + session,
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
            }

            url = "https://moca.unimma.ac.id/mod/attendance/attendance.php"
            response2 = requests.post(url=url, data=payload, headers=headers, verify=False,
                                      allow_redirects=False)
            # print(response2.text)
            if event:
                event.set()
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
            print(f"HilmiStd/MocaScraper: Berhasil presensi, silahkan cek di {href_value}.")
            return
        except AttributeError:
            if event:
                event.set()
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
            print("\033[1;33m" + "HilmiStd/MocaScraper: Pilihan Present/Hadir dan Late/Terlambat tidak ditemukan.",
                  "\033[0m")
            return
        except:
            pass
