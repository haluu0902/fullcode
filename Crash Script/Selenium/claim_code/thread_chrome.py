from threading import Thread
import control_chrome

class OpenChromeThread:
    def __init__(self, numberOfAccounts):
        self.numberOfThreads = 2
        self.numberOfAccounts = int(numberOfAccounts/self.numberOfThreads)
        self.listThread = []
    def open_chrome_thread(self):
        for i in range(self.numberOfThreads):
            self.listThread.append(control_chrome.ControllChrome(self.numberOfAccounts))
            Thread(target=self.listThread[i].open_browser()).start()
    def send_code_thread(self, code):
        for i in range(self.numberOfThreads):
            Thread(target=self.listThread[i].send_code(code)).start()

#a = OpenChromeThread(4,"aaa")
#a.open_chrome_thread()
#input("Con: ")
#a.send_code_thread()