import webbrowser
import sys


sys.path.append("./modules")

def get(st:str=""):
    """Download a package «stuff» from pypi web page using a browser. Put the package in the «modules» folder. 
    Use «import modules.stuff» to import the «stuff» package."""
    if st:
        webbrowser.open(f"https://pypi.org/project/{st}/#files")
    else:
        webbrowser.open(f"https://pypi.org/search/")

if __name__ == "__main__":
    get()
    
