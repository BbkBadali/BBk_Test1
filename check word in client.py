
"""
import psutil
l = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'winword.exe'.upper() in p.info['name']]

if len(l) > 0:
  pid =l[0]['pid']
else:
  # No winword.exe found
  print("There is not any file opend")
  #return []

p = psutil.Process(pid)
fileList = p.as_dict(attrs=['open_files']) # Get the list of all files opened by winword.exe. It must be filtered on doc, docx because there are many other files.
print("filelist===", fileList)
"""


#---------------------------------------------------
from tkinter import *
import win32com.client
import wmi

# Initializing the wmi constructor
f = wmi.WMI()

flag=False
# Iterating through all the running processes
for process in f.Win32_Process():
  if "WINWORD.EXE" == process.Name:
      flag=True
    
if flag==True:
     word = win32com.client.GetObject(None, 'Word.Application')

     counter=0
     for doc in word.Documents:
         print("Next document is " + doc.name)
         counter+=1
    #print("split name===",word.Documents[0])

     top = Tk()
     top.title('List of Running Word Doc')
     top.geometry('400x400')
     top.resizable(width=False,height=False)

     Lb = Listbox(top,width=61,height=24)

     for i in range (counter):
        Lb.insert(i,word.Documents[i])

     Lb.pack()
     top.mainloop()
else:
      print ("No Word file is running.")