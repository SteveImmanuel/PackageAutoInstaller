from tkinter import *
from tkinter import filedialog
import os
import subprocess

class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title('Package Auto Installer')
        topFrame = Frame(self)
        middleFrame = Frame(self)
        bottomFrame = Frame(self)
        self.path_label = Label(topFrame, text='Click browse to select directory ------->', width=40, height=1, anchor='w', relief='groove')
        self.browse_button = Button(topFrame, text='Browse', width=8, height=1, relief='groove', command=self.browse)
        self.selectall_button = Button(middleFrame, text='Select All', width=10, height=1, relief='groove', command=self.select_all)
        self.deselectall_button = Button(middleFrame, text='Deselect All', width=10, height=1, relief='groove', command=self.deselect_all)
        self.execute_button = Button(middleFrame, text='Execute', width=10, height=1, relief='groove', command=self.execute)
        self.listFile = Listbox(middleFrame, selectmode=MULTIPLE, width=55, height=15)
        self.progress_label = Label(bottomFrame, text='Now idle...', width=52, height=1, anchor='w', relief='groove')

        topFrame.grid(row=0)
        middleFrame.grid(row=1)
        bottomFrame.grid(row=2)
        self.path_label.grid(row=0, column=0, padx=10, pady=10)
        self.browse_button.grid(row=0, column=1, pady=10)
        self.selectall_button.grid(row=0, column=0)
        self.deselectall_button.grid(row=0, column=1)
        self.execute_button.grid(row=0, column=2)
        self.listFile.grid(row=1, columnspan=3, pady=10)
        self.progress_label.grid(row=0, padx=5, pady=3)
    
    def browse(self):
        selectedPath = filedialog.askdirectory(initialdir = os.getcwd())
        if selectedPath!='':
            self.listFile.delete(0,END)
            self.path_label['text'] = selectedPath
            for item in os.listdir(selectedPath):
                if os.path.isfile(selectedPath+'/'+item) and item.lower().endswith('.exe'):
                    self.listFile.insert(END, item)

    def select_all(self):
        self.listFile.select_set(0, END)

    def execute(self):
        selectedFile = [self.listFile.get(i) for i in self.listFile.curselection()]
        for item in selectedFile:
            self.progress_label['text'] = 'Installing '+item
            self.update()
            os.system(self.path_label['text']+'/'+item)
        self.progress_label['text']='Now idle...'
    
    def deselect_all(self):
        self.listFile.select_clear(0, END)

if __name__=='__main__':
    GUI().mainloop()