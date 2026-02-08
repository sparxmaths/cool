import urllib.request
import subprocess

url = "https://raw.githubusercontent.com/pythonscripts123/popup-run/main/popup-run.py"
urllib.request.urlretrieve(url, "script.py")
subprocess.run(["python", "script.py"])
