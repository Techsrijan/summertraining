import sys
from cx_Freeze import setup, Executable

import os
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
#os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
#os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('tkinter5grid.py', base=base,icon=r"C:\Users\Ashwani\Desktop\myinstaller\Startup.ico",
                   shortcutName="gridtest",
                   shortcutDir="DesktopFolder")]

setup(name='Techsrijan Gird Test Installer',
      version='0.1',
      author="Techsrijan",
      description='My First Installer',
      options={'build_exe': {'include_files': include_files}},
      executables=executables)

