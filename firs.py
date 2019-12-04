# import sys
# from PyQt5.QtWidgets import QApplication, QDialog
#
# app = QApplication(sys.argv)
# window = QDialog()
#
# window.show()
# sys.exit(app.exec_())




from PyQt5 import QtWidgets, uic

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = uic.loadUi("./de2.ui")  # specify the location of your .ui file
    win.runButton.clicked.connect(lambda: print("1"))
    win.show()
    sys.exit(app.exec())