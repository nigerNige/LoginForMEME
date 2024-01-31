import time
from colormnd import *

def loading_dot(x, y):
    
    loading = yellow("loading")
    dot = yellow(".")
    
    print(f"{loading}", end="", flush=True)
    time.sleep(x)

    for i in range(y):
        print(f"{dot}", end="", flush=True)
        time.sleep(x)
