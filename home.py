# uncompyle6 version 3.4.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Aug  6 2019, 01:09:22) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <debby>
import os, sys, time
from time import sleep as timeout

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.2)


os.system('cd ..')
