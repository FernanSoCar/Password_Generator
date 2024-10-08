import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["PySimpleGUI"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

    
setup (
    name = "Password Generator",
    version = "0.1",
    description = "Generate rando passwords for your websites, sofwares, email, etc.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("app.py", base=base)]
)