#from PyQt5.QtWidgets import * 
#import sys, os
#from PyQt5.QtCore import *
#from PyQt5.QtGui import * 
#from PyQt5 import QtCore
#import pyodbc
#
#class EmailNotification(QWidget):
#	def __init__(self):
#		super().__init__() 
#		self.initGUI()
#	def initGUI(self):
#		self.scroll_area = QScrollArea()
#		self.scroll_area.setWidget(self)
#		self.scroll_area.setWidgetResizable(True)
#		self.scroll_area.resize(500,200)
#		
#		self.scroll_area.setWindowTitle("Email Notification")
#		
#		center = self.scroll_area.frameGeometry()
#		cp = QDesktopWidget().availableGeometry().center()
#		center.moveCenter(cp)
#		self.scroll_area.move(center.topLeft())
#		self.scroll_area.show()
#
#if __name__ == '__main__':
#	app = QApplication(sys.argv)
#	app.setStyleSheet("QApplication{background-color: rgb(255,0,0);border: 1px solid black;}")
#	dd = EmailNotification()
#	dd.show()
#	sys.exit(app.exec_())
#	
import smtplib

content = ("Test email from Python code")

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('narendra.kommoju964@gmail.com','xxxxxx')

mail.sendmail('narendra.kommoju964@gmail.com','k.narendra234@gmail.com',content) 

mail.close()
print("Sent")	
