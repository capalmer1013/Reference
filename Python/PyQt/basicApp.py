import sys
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication


def main():
	app = QApplication(sys.argv)
	window = QMainWindow()
	window.show()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()
