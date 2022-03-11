import sys

import interface

import etudiant

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class demoQt(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(demoQt, self).__init__(parent)
        self.setupUi(self)
        self.listEtudiant = []


    @pyqtSlot()
    def on_pushButton_clicked(self):
        nom = self.lineEdit_nom_etudiant.text()


        try:
            num = int(self.lineEdit_num_etudiant.text())
        except:
            self.label_erreure.setText("Le numeros d'étudiant ne peut contenir de lettre")
        else:
            if testnom(nom, self) and testnum(num,self):
                self.listEtudiant.append(etudiant.Etudiant(nom,num))

        for etudiant in self.listEtudiant:










def testnom(text :str, window):
    if text.isalpha():
        window.label_erreure.setText("Le nom d'étudiant ne peut contenir de chiffre")
        return False
    return True

def testnum(text :str, window):
    if len(text)==7:
        window.label_erreure.setText("Le numéros d'étudiant doit etre de 7 lettre de long")
        return False
    return True

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = demoQt()
        form.show()
        app.exec()

if __name__ == "__main__":
    main()