import json
import random
import pyautogui
from pywinauto.keyboard import send_keys
import time

dictionary = []
used_words = []
mpos = ()

print("Loading the dictionary...")

with open("words_dictionary.txt", "r") as handle:
    dictionary = handle.read().split("\n")


while True: 
    strin = input("~")
    for _ in dictionary:
        if _ in used_words:
            continue
        if strin in _:
            print(_)
            used_words.append(_)
            mpos = pyautogui.position()
            pyautogui.moveTo(500, 500)
            pyautogui.click()
            pyautogui.moveTo(mpos)
            pyautogui.typewrite(_, interval=0.04)
            send_keys('{ENTER}')
            pyautogui.click()
            break