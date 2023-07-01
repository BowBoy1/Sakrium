#
#SAKRIUM
#
#2023 Charlie's Game Jam
#

#Normal Imports


#Imports from other files
import LibraryInstaller


#running the LibraryInstaller file
# Libraries to check and install
libraries = ['pygame', 'superwires']

# Check and install libraries if necessary
for library in libraries:
   LibraryInstaller.check_library(library)
