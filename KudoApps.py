# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:21:51 2020

@author: HP
"""
#importing library
import os

#application class
class apps_container:
            
    #opens notepad
    def notepad_app(self):
        os.system("notepad.exe")
    
    #opens MS paint
    def paint_app(self):
        os.system("mspaint.exe")  
    
    #opens calculator
    def calc_app(self):
        os.system("calc.exe")
        
    #opens MS excel
    def excel_app(self):
        xl = os.popen(
            r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        
    #open MS word
    def word_app(self):
        ww = os.popen(
            r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        
    #opens MS powerpoint
    def ppt_app(self):
        pp = os.popen(
            r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")        
    
