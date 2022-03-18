import etudiant
import quitter



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot




class quitterQt(QtWidgets.QMainWindow, quitter.Ui_MainWindow):
    def __init__(self, parent=None):
        super(quitterQt, self).__init__(parent)
        self.setupUi(self)