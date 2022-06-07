from ssl import Options
import cx_Freeze
executables= [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    name="topDownShooter",
    options={"build_exe":{"packages":["pygame","sqlite3","sys"],
    "include_files":[""]}},
    executables=executables
)