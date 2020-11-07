import webbrowser
import os

def openDocumentationFile():
    cwd = os.getcwd()
    webbrowser.open_new(cwd + "/doc/documentation.pdf")
