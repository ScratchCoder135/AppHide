import os
from tkinter.filedialog import askopenfilename
from tkinter import *
import shutil
import os, winshell
from win32com.client import Dispatch
#Import External Modules
win=Tk()
fakenames=["Calculator","Web Browser","Chat","Clock"]
win.maxsize(600,500)
win.minsize(600,500)
win.title("File Hider By Python")
lab=Label(text="Choose a file and we will help you to hide them!")
lab.configure(font=("Arial",20))
lab.grid(row=1,column=2)
tips=Label(text="")
tips.grid(row=4,column=2)
def choose():
  filename = askopenfilename()#Get information needed
  if filename:
    work_dir=os.getcwd()+"\\saved"
    if os.path.isdir(work_dir):
      c=os.path.exists(os.getcwd()+"\\saved\\"+os.path.basename(filename))
      d=not c
      if os.path.exists(os.getcwd()+"\\resources\\icon.ico") and d:
        filepath = os.path.abspath(filename)#Move the file
        shutil.move(filepath,os.getcwd()+"/saved")
        shell=Dispatch("WScript.Shell")
        urname=os.getlogin()
        savepath=f"C:\\Users\\{urname}\\Desktop\\Calculator.lnk"
        location=os.getcwd()+"\\saved\\"+os.path.basename(filename)
        current=os.getcwd()
        shortcut=shell.CreateShortCut(savepath)
        shortcut.Targetpath=location
        shortcut.WorkingDirectory=work_dir
        shortcut.IconLocation=f"{current}\\resources\\icon.ico"
        shortcut.save()
        tips.configure(text="Successfully moved file to the app disk!Open the disk to see your file!")
      else:
        tips.configure(text="Check the following directories and see if these files exists...\n\n\n~Appdir/resources\n\n~Appdir/saved/-The name of the file you want to choose-\n\nRetry if your answer is Yes,No")
    else:
         tips.configure(text=f"Error!Cannot find the folder {work_dir}")
  else:
    tips.configure(text=f"The file you chose have problems.")
b=Button(text="Choose File",command=choose)
b.grid(row=2,column=2)
label=Label(text="Recommended to link .lnk file on desktop as other files may cause errors.")
label.grid(row=3,column=2)
win.mainloop()
