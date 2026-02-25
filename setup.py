from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "ddgs",
        "rich",
        "httpx",
        "email",
        "urllib",
    ],
    "includes": [
        "email.header",
        "email.parser",
        "email.feedparser",
        "email._policybase",
    ],
}

setup(
    name="qsearch",
    version="0.1",
    description="Tiny quick search CLI",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)