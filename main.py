# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 01:51:38 2021

@author: ediaz
"""
import kivy.app
import kivy.uix.label

class TestApp(kivy.app.App):
     def build(self):
         return kivy.uix.label.Label(text = 'Hello World')
    
app = TestApp()
app.run()


# class TestApp(kivy.app.App):
#     pass
# app = TestApp(title = 'Hello')
# app.run()