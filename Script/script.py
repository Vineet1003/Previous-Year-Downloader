#                   Netaji Subhas Institute of Technology

# Script to download all available previous year question papers
# Just enter your branch and semester

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os,urllib.request,getch,sys
html = urlopen("http://test.collegespace.in/mob-exam/")
text=html.read()
soup=BeautifulSoup(text,'html.parser')
pretext="http://test.collegespace.in"

print("\t\t\t\tNetaji Subhas Institute of Technology \n")
print("This is the portal to download previous year ques papers")
print("[Source: Collegespace]\n")
print(" Branch Selection Code : \n")
print("1. coe\n2. ece\n3. it\n4. mpae\n5. ice\n6. bt\n")
print("[Input Logic]")
print("Enter Your branch code and sem no. \n e.g \"coe 5\" ,  \"ece 7\" \n")
branch,sem=input().split()

#Get the url for respective branch and sem 
y=soup.find_all("div",attrs={'id': branch})
x=y[0].find_all("div",attrs={'id': branch+sem})
links=x[0].find_all('a')

#Get Path to store files
path=os.path.join(os.environ["HOMEDRIVE"],os.environ["HOMEPATH"],"Desktop")
name=input("Enter the name of the directory to store files:   ")
path=os.path.join(path,name)

#Check for presence of Directory..
try:
    os.makedirs(path)
except:
    print("\nSorry :( cannot create directory with that name")
    getch.getch()
    sys.exit()

   
print("\nYour files are ready to download\nPlease keep patience.. Some files may be large in size")
print("\nPress Enter to continue\n")
getch.getch()

#Retrieve file from and download
for i in links:
    print(i.get_text()," is downloading....")
    link=pretext+i.get('href')
    filename=path+"\\"+i.get_text()
    urllib.request.urlretrieve(link,filename)
#print("Done\n")

print("\nAll your files are downloaded")
getch.getch()
sys.exit()
  

