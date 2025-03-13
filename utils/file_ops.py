import os

def read(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"file {path} not found")
    with open(path, "r") as f:
        return f.read()

def write(path, content):
    with open(path, "w") as f:
        f.write(content)
