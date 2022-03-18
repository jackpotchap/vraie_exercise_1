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
        self.listEtudiant = [Etudiant("gabriel", 2030491,"programation"),Etudiant("jeremy", 2030492,"résautique")]

        for etudiant in self.listEtudiant:
            self.textBrowser.setText(self.textBrowser.toPlainText() + etudiant.__str__())




    @pyqtSlot()
    def on_pushButton_clicked(self):
        date = self.dateEdit.text().split("-")[0]



        nom = self.lineEdit_nom_etudiant.text()
        num = self.lineEdit_num_etudiant.text()

        try:
            int(num)
        except:
            self.label_erreure.setText("Le numeros d'étudiant ne peut contenir de lettre")
        else:
            if testnom(nom, self) and testnum(num,self):

                print("allo")
                self.listEtudiant.append(etudiant.Etudiant(nom, num, str(self.comboBox.currentText())))



                self.textBrowser.setText(self.textBrowser.toPlainText()+self.listEtudiant[-1].__str__())

                self.lineEdit_nom_etudiant.setText("")
                self.lineEdit_num_etudiant.setText("")

    @pyqtSlot()
    def on_pushButton_supprimer_clicked(self):
        #  suprimer
        as_find = False
        for etudiant in self.listEtudiant:

            if str(etudiant.num) == self.lineEdit_num_etudiant.text():
                print("***")
                print(etudiant.num)
                print("---")
                print(self.lineEdit_num_etudiant.text())
                print("***")
                as_find = True
                self.listEtudiant.remove(etudiant)

                output = ""

                for etudiant in self.listEtudiant:
                    output += etudiant.__str__()

                self.textBrowser.setText(output)

        if as_find != True:
            self.label_erreure.setText("Le numeros d'étudiant ne corespond a aucun etudiant")





    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        as_find = False
        #modifier
        listEtudiant_T = []
        for etudiant in self.listEtudiant:

            if str(etudiant.num) == self.lineEdit_num_etudiant.text():
                nom = self.lineEdit_nom_etudiant.text()

                if testnom(nom, self):



                    etudiant.name = nom


                    self.lineEdit_nom_etudiant.setText("")
                    self.lineEdit_num_etudiant.setText("")

                as_find = True

                output = ""

                for e in self.listEtudiant:
                    print(e.name)
                    output += e.__str__()


                self.textBrowser.setText(output)

            listEtudiant_T.append(etudiant)

        if as_find != True:
            self.label_erreure.setText("Le numeros d'étudiant ne corespond a aucun etudiant")

        self.listEtudiant = listEtudiant_T

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        # ajouter
        output = ""

        for e in self.listEtudiant:
            print(e.name)
            output += e.__str__()
        with open('save.txt', 'w') as f:
            f.write(output)



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