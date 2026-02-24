import os

def save_env(path, variables):

    env_path = f"{path}/.env"

    with open(env_path,"w") as f:
        for k,v in variables.items():
            f.write(f"{k}={v}\n")
