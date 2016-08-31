# coding=utf8

import os
from Tkinter import *
import Tkconstants, tkFileDialog
import thread

import convert_png


class Application(Frame):
    def ask_dir(self, tag):
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = '選擇目標文件夾'

        filename = tkFileDialog.askdirectory(**self.dir_opt)

        if tag == 1:
            self.origin_inputField.delete(0, len(self.origin_inputField.get()));
            self.origin_inputField.insert(0, filename)
        if tag == 2:
            self.target_inputField.delete(0, len(self.target_inputField.get()));
            self.target_inputField.insert(0, filename)    
    
    def ask_tp_exe(self):
        self.of_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['defaultextension'] = '.exe'
        options['filetypes'] = [('執行檔', '.exe')]
        options['parent'] = root
        options['title'] = '選擇Texture Packer exe'
        options['multiple'] = False

        filename = tkFileDialog.askopenfilename(**self.of_opt)
        self.tp_inputField.delete(0, len(self.tp_inputField.get()));
        self.tp_inputField.insert(0, filename)
    
    def ask_pngquant_exe(self):
        self.of_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['defaultextension'] = '.exe'
        options['filetypes'] = [('執行檔', '.exe')]
        options['parent'] = root
        options['title'] = '選擇pngquant exe'
        options['multiple'] = False

        filename = tkFileDialog.askopenfilename(**self.of_opt)
        self.pngquant_inputField.delete(0, len(self.pngquant_inputField.get()));
        self.pngquant_inputField.insert(0, filename)    
        
        
    def ask_blacklist(self):
        self.of_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('文字檔', '.txt')]
        options['parent'] = root
        options['title'] = '選擇黑名單清單'
        options['multiple'] = False

        filename = tkFileDialog.askopenfilename(**self.of_opt)
        self.blacklist_inputField.delete(0, len(self.blacklist_inputField.get()));
        self.blacklist_inputField.insert(0, filename)    
    
    def ask_pngoptlist(self):
        self.of_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('文字檔', '.txt')]
        options['parent'] = root
        options['title'] = '選擇縮圖清單'
        options['multiple'] = False

        filename = tkFileDialog.askopenfilename(**self.of_opt)
        self.pngoptlist_inputField.delete(0, len(self.pngoptlist_inputField.get()));
        self.pngoptlist_inputField.insert(0, filename)    
        
    def convert_t(self):
        
        convert_png.TEXTURE_PACKER_EXE = self.tp_inputField.get()
        convert_png.TARGET_DIR = self.origin_inputField.get()
        convert_png.OUTPUT_DIR = self.target_inputField.get()
        convert_png.PNG_QUANT_EXE = self.pngquant_inputField.get()
        convert_png.BLACK_LIST = self.blacklist_inputField.get()
        convert_png.PNG_OPT_LIST = self.pngoptlist_inputField.get()
        
        convert_png.convert( )
        
        with open('.config', "w") as f:
            setting = {}
            setting['tp'] = self.tp_inputField.get()
            setting['target'] = self.origin_inputField.get()
            setting['output'] = self.target_inputField.get()
            setting['blacklist'] = self.blacklist_inputField.get()
            setting['pngquant'] = self.pngquant_inputField.get()
            setting['pngoptlist'] = self.pngoptlist_inputField.get()
            f.write(str(setting))
            f.close()

        
        self.convertButton.config(state="normal")
        
    def convert(self):   
        self.convertButton.config(state="disabled")
        thread.start_new_thread( self.convert_t, () )
                
        
    
    def createWidgets(self):
        
        #===
        self.tp_label_dir_choose = Label(self, text="Texture packer路徑")
        self.tp_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.tp_inputField = Entry(self, width=50)
        self.tp_inputField.pack({"anchor": "w", "padx":10})

        self.tp_inputButton = Button(self, text="選擇路徑..", command= self.ask_tp_exe)
        self.tp_inputButton.pack({"anchor": "w", "padx":10})
        
        #===

        self.pngquant_label_dir_choose = Label(self, text="pngquant路徑")
        self.pngquant_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.pngquant_inputField = Entry(self, width=50)
        self.pngquant_inputField.pack({"anchor": "w", "padx":10})

        self.pngquant_inputButton = Button(self, text="選擇路徑..", command= self.ask_pngquant_exe)
        self.pngquant_inputButton.pack({"anchor": "w", "padx":10})
        
        #===
        self.origin_label_dir_choose = Label(self, text="欲轉換目標路徑")
        self.origin_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.origin_inputField = Entry(self, width=50)
        self.origin_inputField.pack({"anchor": "w", "padx":10})

        self.origin_inputButton = Button(self, text="選擇路徑..", command= lambda: self.ask_dir(1))
        self.origin_inputButton.pack({"anchor": "w", "padx":10})
        #===
        self.target_label_dir_choose = Label(self, text="目的地路徑")
        self.target_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.target_inputField = Entry(self, width=50)
        self.target_inputField.pack({"anchor": "w", "padx":10})

        self.target_inputButton = Button(self, text="選擇路徑..", command= lambda: self.ask_dir(2))
        self.target_inputButton.pack({"anchor": "w", "padx":10})
        #===
        self.blacklist_label_dir_choose = Label(self, text="排除清單路徑")
        self.blacklist_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.blacklist_inputField = Entry(self, width=50)
        self.blacklist_inputField.pack({"anchor": "w", "padx":10})

        self.blacklist_inputButton = Button(self, text="選擇路徑..", command= self.ask_blacklist)
        self.blacklist_inputButton.pack({"anchor": "w", "padx":10})
        #===
        self.pngoptlist_label_dir_choose = Label(self, text="png縮圖清單路徑(需設置pngquant路徑)")
        self.pngoptlist_label_dir_choose.pack({"anchor": "w", "padx":10, "pady":10})

        self.pngoptlist_inputField = Entry(self, width=50)
        self.pngoptlist_inputField.pack({"anchor": "w", "padx":10})

        self.pngoptlist_inputButton = Button(self, text="選擇路徑..", command= self.ask_pngoptlist)
        self.pngoptlist_inputButton.pack({"anchor": "w", "padx":10})
        #===
        self.convertButton = Button(self, text="轉檔", command= self.convert, width=50)
        self.convertButton.pack({"anchor": "w", "padx":10, "pady":10})
        
        try:
            setting = eval(open('.config', 'r').read())
            self.tp_inputField.insert(0, setting['tp'])
            self.origin_inputField.insert(0, setting['target'])
            self.target_inputField.insert(0, setting['output'])
            self.blacklist_inputField.insert(0, setting['blacklist'])
            self.pngquant_inputField.insert(0, setting['pngquant'])
            self.pngoptlist_inputField.insert(0, setting['pngoptlist'])
        except:
            print 'load setting file fail.'
            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()