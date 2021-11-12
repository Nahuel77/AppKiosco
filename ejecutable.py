from cx_Freeze import setup, Executable 

exe = [Executable("main.py", base = "Win32GUI", icon = "icon.ico")]

setup(
    name = "Kiosco",
    version = "1.0",
    executables = exe
) 