import subprocess

new = subprocess.run("pip freeze", shell=True, text=True, capture_output=True)
with open("requirements.txt", encoding="utf8") as f:
    old = f.read()

if new.stdout != old:
    subprocess.run("pip freeze > requirements.txt", shell=True)
    subprocess.run("git add requirements.txt", shell=True)
    print("FAILURE: requirements.txt is not up to date!")
    exit(1)
else:
    print("SUCCESS: requirements.txt is up to date!")
    exit(0)
