#
#SAKRIUM LIBRARY INSTALLER
#
#2023 Charlie's Game Jam
#

#Imports
import subprocess

#This section checks for required external libraries and attempts to install any that are missing via PIP, this part was written almost entirely by ChatGPT
def check_library(library):
    try:
        subprocess.check_call(['pip', 'show', library])
    except subprocess.CalledProcessError:
        install_library(library)

def install_library(library):
    try:
        subprocess.check_call(['pip', 'install', library])
    except subprocess.CalledProcessError:
        print(f"Failed to install {library}. Please install it manually.")