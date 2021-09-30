import json

from ha_luu_bot import HaLuuBot

def main():
    try:
        with open('session.json') as f:
            session_cookies = json.load(f)
        client = HaLuuBot('username', 'password', session_cookies=session_cookies)
        client.listen()        

    except:
        username = input("Nhap tai khoan: ")
        password = input("Nhap mat khau: ")
        client = HaLuuBot(username, password)
        session_cookies_new = client.getSession()
        with open('session.json', 'w') as outfile:
            json.dump(session_cookies_new, outfile)
            print("Login Success!")
        client.listen()


if __name__ == '__main__':
    main()
