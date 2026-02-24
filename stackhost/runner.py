import subprocess
import os

running_process = {}

def clone_repo(repo, user_id):
    path = f"bots/{user_id}"

    if os.path.exists(path):
        subprocess.run(["rm", "-rf", path])

    subprocess.run(["git", "clone", repo, path])
    return path


def install_requirements(path):
    req = f"{path}/requirements.txt"
    if os.path.exists(req):
        subprocess.run(["pip3", "install", "-r", req])


def start_bot(path, user_id):
    process = subprocess.Popen(
        ["python3", "bot.py"],
        cwd=path
    )

    running_process[user_id] = process
    return process.pid


def stop_bot(user_id):
    if user_id in running_process:
        running_process[user_id].terminate()
