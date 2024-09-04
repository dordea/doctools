import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "include_files": ["files/"], "include_msvcr": True,}



# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="DocsTool",
    version="0.1",
    description="Documents tool!",
    options={"build_exe":build_exe_options},
    executables=[Executable("doctools.py", targetName='DocsTool.exe', base=base, icon="icon.ico")],
)