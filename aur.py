#Simple AUR helper written in Python.

import sys
import os
import argparse
import shutil

def cloneFromAUR(packageName):
  try:
    shutil.rmtree(packageName, ignore_errors=True) # Make sure there is no leftovers from an old clone
  except:
    print("")
  print("Cloning", packageName)
  clone = "git clone https://aur.archlinux.org/" + packageName + ".git" 
  os.system(clone) # Cloning
  print("Done! Building...")
  os.chdir(packageName)
  
  os.system("makepkg -si")
  os.chdir("..")
  print("Finished! Removing leftovers and exiting...")
  shutil.rmtree(packageName, ignore_errors=True) # Clean up once we have finished
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-G", help = "Clone and build an AUR package")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.G:
    cloneFromAUR(args.G)
