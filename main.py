# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
import tkinter as tk
import pickle

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import web
import kintai as kin

DISP_MODE = "ON"   # "ON" or "OFF"

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Input Form")
        self.geometry("550x250")

        self.entries = {}
        self.submitted_data = None

        self.create_label_entry("勤務開始誤差", "g_startMargin")
        self.create_label_entry("勤務時間誤差", "g_workMargin")
        self.create_label_entry("訪問場所（複数:空白区切り）", "g_visit")
        self.create_label_entry("時間外労働時間", "g_overMinute")
        self.create_label_entry("時間外労働理由", "g_overReason")
        self.create_label_entry("ログインID", "g_login")
        self.create_label_entry("パスワード", "g_pass")

        self.load_previous_input()

        self.submit_button = tk.Button(self, text="　記入開始　", command=self.submit, bg="red", fg="white")
        self.submit_button.pack(pady=10)

    def create_label_entry(self, label_text, key):
        frame = tk.Frame(self)
        frame.pack(pady=5)

        label = tk.Label(frame, text=label_text, width=16, anchor='e')
        label.pack(side=tk.LEFT, padx=(0, 5))

        entry = tk.Entry(frame, width=30)
        entry.pack(side=tk.LEFT)

        self.entries[key] = entry

    def load_previous_input(self):
        try:
            with open("new_previous_input.pkl", "rb") as f:
                previous_input = pickle.load(f)
                for key, entry in previous_input.items():
                    entry_widget = self.entries[key]
                    entry_widget.insert(0, entry)
        except FileNotFoundError:
            pass

    def submit(self):
        submitted_data = {}
        for key in ["g_startMargin", "g_workMargin", "g_visit", "g_overMinute", "g_overReason","g_login", "g_pass", ]:
            entry_widget = self.entries[key]
            input_text = entry_widget.get()
            submitted_data[key] = input_text
            # print(f"Submitted {key}: {input_text}")

        with open("new_previous_input.pkl", "wb") as f:
            pickle.dump(submitted_data, f)

        self.submitted_data = submitted_data
        self.destroy()


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':

    app = Application()
    app.mainloop()
    user_input = app.submitted_data
    ret = 0

    if user_input is not None:
        if DISP_MODE == "OFF":
            options = Options()
            options.add_argument('--headless')
            #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver = webdriver.Chrome(service=Service(), options=options)

        else:
            try:
                #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver = webdriver.Chrome(service=Service())
                # 自動でPCのChromeと同じバージョンのdriverをインストールする処理
                # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            except:
                # 例外発生時、配布されているもののうち最新のdriverをインストールする処理
                res = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
                options = Options()
                #driver = webdriver.Chrome(service=Service(ChromeDriverManager(res.text).install()), options=options)
                driver = webdriver.Chrome(service=Service(), options=options)

        ret = web.inputLogin(driver, user_input)
        #print(type(driver))
        if ret == 0:
            ret = kin.inputKintai(driver, user_input)

        driver.quit()

        print(f"ret={ret}")

    else:
        print("quit!")

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
