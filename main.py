import glob
import logging
import pathlib
import shutil
import time
from argparse import ArgumentParser

import pyautogui
from mss.windows import MSS
from pywinauto import Application

import pyuac


def test(exe, out):
    with MSS() as sct:
        logging.info('executable at: ' + exe)
        logging.info('output location at: ' + str(out))
        fraps = Application().start(r'C:\Fraps\fraps.exe')
        app = Application(backend='win32').start(exe)
        logging.info('started with PID: ' + str(app.process))
        time.sleep(60)
        pyautogui.press('enter')
        sct.shot(output=str(out/"start.png"))
        pyautogui.press('f11')
        pyautogui.keyDown('w')
        time.sleep(10)
        pyautogui.keyUp('w')
        pyautogui.press('f11')
        sct.shot(output=str(out/"end.png"))
        for file in glob.glob(r'C:\Fraps\Benchmarks\*'):
            shutil.move(file, out)
        app.kill()
        fraps.kill()


if __name__ == '__main__':
    if not pyuac.is_user_admin():
        pyuac.run_as_admin()
    else:
        parser = ArgumentParser()
        parser.add_argument('executable', help='path to executable file', )
        parser.add_argument('-o', '--output', dest='output', default=None, help='output directory', type=pathlib.Path)
        args = parser.parse_args()
        logging.basicConfig(filename=str(args.output/'log.txt'), encoding='utf-8', level=logging.DEBUG)
        test(args.executable, args.output)
