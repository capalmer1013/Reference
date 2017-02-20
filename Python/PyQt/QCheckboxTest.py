import sys
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QWidget

def main():
	def buttonClicked():
		if checkbox1.isChecked():
			checkbox1.setChecked(False)
		else:
			checkbox1.setChecked(True)
			

	app = QApplication(sys.argv)
	window = QMainWindow()
	centralWidget = QWidget(window)
	
	layout = QVBoxLayout(centralWidget)
	
	# make elements and put in layout
	button = QPushButton("okay", window)
	checkbox1 = QCheckBox("Checkbox 1", window)
	checkbox2 = QCheckBox("Checkbox 2", window)
	
	layout.addWidget(button)
	layout.addWidget(checkbox1)
	layout.addWidget(checkbox2)
	
	# connect button to QcheckBoxes
	button.clicked.connect(buttonClicked)
	window.setCentralWidget(centralWidget)
	window.show()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()

