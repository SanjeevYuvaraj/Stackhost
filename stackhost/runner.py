import subprocess
import os

running = {}

def clone_repo(repo, bot_id):
    path = f"bots/{bot_id}"

    if os.path.exists(path):
        subprocess.run(["rm","-rf",path])

    subprocess.run(["git","clone",repo,path])
    return path


def install_req(path):
    req = f"{path}/requirements.txt"
    if os.path.exists(req):
        subprocess.run(["pip3","install","-r",req])


def start_bot(path, bot_id):

    log_file = open(f"logs/{bot_id}.log","w")

    process = subprocess.Popen(
        ["python3","bot.py"],
        cwd=path,
        stdout=log_file,
        stderr=log_file
    )

    running[bot_id] = process
    return process.pid


def stop_bot(bot_id):
    if bot_id in running:
        running[bot_id].terminate()


def restart_bot(path, bot_id):
    stop_bot(bot_id)
    return start_bot(path, bot_id)
