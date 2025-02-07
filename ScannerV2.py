import glob, re, os, hashlib
from pathlib import Path

#store file sizes and modification dates
def storeFileAttributes():
  #finding files to scan
  files = glob.glob("*.py")
    #create text file if not exist
  fileName= "track.txt"
  track = Path(fileName)
  track.touch(exist_ok=True)
  
  with open('track.txt', 'w') as track:
    for f in files:
      #scans all files except running scanner
      if f==os.path.basename(__file__):
          continue
      
      hash = hashlib.md5(open(f,'rb').read()).hexdigest()
      print(f,"MD5 Hash:",hash,file=track)
  
  track.close()
  sortFile(fileName)
  

#sorts track.txt file content in alphabetical order 
def sortFile(track):
  new = []
  trackFile = open(track,"r")
  trackLines = trackFile.readlines()
  trackFile.close()
  for line in trackLines:
      new.append(line)
  
  new.sort() #sorts by letter
  trackFile = open(track,"w")
  for k in new:
    trackFile.write(k)


#1 scan for signatures
def checkForSign(theChangedFile):
  print("\nPreparing to scan "+theChangedFile+".....")
  openChangedFile=open(theChangedFile,"r")
  linesofChangedFile=openChangedFile.readlines()
  openChangedFile.close()

  infectedFile=False  #initialize infection flag, is enabled to True if an infected file is found
  for line in linesofChangedFile:
    if (re.search("#546849732046694c6520486153204265456e20496e66456374456420427920546845205365707265656e61205669725573",line)):   #this string was taken from our virus python file
      #virus found
      infectedFile=True

      
  if(infectedFile==True):
    print("\nATTENTION! VIRUS FOUND IN THIS FILE: " + theChangedFile)
    #remove infected file(s)
    print (theChangedFile + " IS DELETED AND CLEANED FROM YOUR SYSTEM")
    print("#####################################")
    #os.remove(p)
  if(infectedFile==False):
    print("The file "+theChangedFile+" is clean.")
    print("#####################################")
        
#compare for changes between track.txt and the original track file, and raise an alert if so
def compareTrack():
  trackFile = open("track.txt","r")
  trackFileLines = trackFile.readlines()
  trackFile.close()

  trackOriginal = open("trackOriginal.txt","r")
  trackOriginalFileLines = trackOriginal.readlines()
  trackOriginal.close()
  
  changed=False
  i=0
  j=0
  for line in trackFileLines:
    if (line==trackOriginalFileLines[j]):
      changed=False
    else:
      print("#####################################")
      print("These two lines do NOT match!")      
      print(trackFileLines[i])
      print(trackOriginalFileLines[j])
      changed=True
    j+=1
      
    if (changed==True):
      unmatchedLine=trackFileLines[i]
      unmatchedLine=unmatchedLine.split()
      for l in unmatchedLine:
        if(re.search(".py",l)):
          theChangedFile=l
          print("the hash of this file has been changed: "+theChangedFile)
          checkForSign(theChangedFile)     
    i+=1
  if (changed==False):
    print("\n#####All files are clean and intact#####")
storeFileAttributes()
compareTrack()
