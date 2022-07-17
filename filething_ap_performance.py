#iRaven/KyleS
# Batch sucks for this.
# Python doesn't :3

import os
from os import path
import shutil

rootdirlist = []
subdirlist = []
absolpathlist = []
files1 = []

# Partial source:
# https://stackoverflow.com/questions/59724872/rename-a-files-within-a-folder-of-a-folder-to-its-parent-folder


# Functions
def listFiles(srcpath):
    for (dirnames) in os.listdir(srcpath):
        rootdirlist.append(dirnames)
    for path, subdirs, files in os.walk(srcpath):
        subdirlist.append(subdirs)
        files1.append(files)
        for name in files:
            #debugging! print(os.path.join(path, name))
            absolpathlist.append(os.path.join(path, name))
        
    #Debugging
    #print("root dirs")
    #print(rootdirlist)
    #print("sub dirs")
    #rint(subdirlist)
    #print("files")
    #print(files1)
    
    print("absol file paths:")
    print(absolpathlist)

def renameMove(filelist, srcpath):
    for file in filelist:
        revfolder = path.basename(path.dirname(file))
        #revfolder = os.path.abspath(os.path.join(file, os.pardir))
        #revfolder = file.parent.name
        #stuname = file.parent.parent.name
        stuname = path.basename(path.dirname(path.dirname(file)))
        origname = os.path.basename(file)

        # bug de lol
        print ('rev folder: '+revfolder)
        print ('stuname: '+stuname)
        print ('orign: '+origname)
        
        if "Revision 1" in revfolder:
            revision = "Rev1"
            print("Revision 1 folder found for: " + stuname + origname)
        if "Revision 2" in revfolder:
            revision = "Rev2"
            print("Revision 2 folder found for: " + stuname + origname)

        newname = stuname+'_'+revision+'_'+origname
            
        print ("Renaming file!!! file name :"+origname+" in folder: "+stuname+revfolder)
        print ("Old filename: "+origname)
        print ("New filename: "+stuname+'_'+revision+'_'+origname)
        
        # moving - i just want to see if renaming works lmao
        shutil.move(file,srcpath+'/'+newname)

# Calls
argpath = input("gib path >:3 : ")
print (listFiles(argpath))

print (renameMove(absolpathlist, argpath))
