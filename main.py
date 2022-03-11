import sys

import etudiant
import interface

from etudiant import Etudiant

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class demoQt(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(demoQt, self).__init__(parent)
        self.setupUi(self)
        self.listEtudiant = [Etudiant("gabriel", 2030491),Etudiant("jeremy", 2030492)]

        for etudiant in self.listEtudiant:
            self.textBrowser.setText(self.textBrowser.toPlainText() + etudiant.__str__())




    @pyqtSlot()
    def on_pushButton_clicked(self):
        nom = self.lineEdit_nom_etudiant.text()
        num = self.lineEdit_num_etudiant.text()

        try:
            int(num)
        except:
            self.label_erreure.setText("Le numeros d'étudiant ne peut contenir de lettre")
        else:
            if testnom(nom, self) and testnum(num,self):


                self.listEtudiant.append(etudiant.Etudiant(nom, num))



                self.textBrowser.setText(self.textBrowser.toPlainText()+self.listEtudiant[-1].__str__())

                self.lineEdit_nom_etudiant.setText("")
                self.lineEdit_num_etudiant.setText("")




def testnom(text :str, window):

    if not text.replace(" ","").isalpha():

        window.label_erreure.setText("Le nom d'étudiant ne peut contenir de chiffre")
        return False
    return True

def testnum(text, window):
    if len(text) != 7:
        print(text)
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