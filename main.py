import os
import subprocess
from pywinauto import Application, keyboard
import pathlib
from argparse import ArgumentParser
import logging
import time
from mss.windows import MSS as mss
import pyautogui
import pygetwindow as gw


def test(exe, out):
    with mss() as sct:
        logging.info('executable at: ' + exe)
        logging.info('output location at: ' + str(out))
        app = Application(backend='win32').start(exe)
        print(app.process)
        print(app)
        # window = app.top_window_()
        # time.sleep(1)
        # logging.info('game started with PID: ' + str(pid))
        # time.sleep(30)
        # window.set_focus()
        keyboard.send_keys('{ENTER}')
        # time.sleep(1)
        # pyautogui.press('enter')
        # sct.shot(output=str(out/"start.png"))
        # # TODO: start fps log
        # pyautogui.keyDown('w')
        # time.sleep(10)
        # pyautogui.keyUp('w')
        # # TODO: stop fps log
        # sct.shot(output=str(out/"end.png"))
        # # TODO: save fps log
        # pyautogui.press('escape')
        # time.sleep(1)
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('enter')
        # time.sleep(1)
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('enter')

        # pyautogui.keyDown('enter')
        # time.sleep(10)
        # filename = sct.shot(output=str(out/"1.png"))
        # print(filename)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('executable', help='path to executable file', )
    parser.add_argument('-o', '--output', dest='output', default=None, help='output directory', type=pathlib.Path)
    args = parser.parse_args()
    logging.basicConfig(filename=str(args.output/'log.txt'), encoding='utf-8', level=logging.DEBUG)
    test(args.executable, args.output)
