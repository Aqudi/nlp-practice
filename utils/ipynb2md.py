import os
import subprocess

files = os.listdir(".")
ipynb = [file for file in files if file.endswith(".ipynb")]

for file in ipynb:
    print(f"{file} 변환 시작합니다.")
    filename = file.replace(".ipynb", "")
    subprocess.run(
        f'jupyter nbconvert "{filename}.ipynb" --to markdown --output "markdown/{filename}.md"')
