import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame)
from PySide6.QtCore import Qt
from PyMemoryEditor import OpenProcess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resident Evil HD Remaster Randomizer")
        self.setFixedSize(600, 400)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        
        # Status section
        status_layout = QVBoxLayout()
        
        bhd_label = QLabel("bhd.exe: Waiting for choice")
        itemlist_label = QLabel("ItemList.txt: Waiting for choice")
        item_rand_label = QLabel("Item Randomizer: WAITING")
        enemy_rand_label = QLabel("Enemy Randomizer: WAITING")
        door_rand_label = QLabel("Door Randomizer: WAITING")
        lock_rand_label = QLabel("Lock Randomizer: WAITING")
        
        for label in [bhd_label, itemlist_label, item_rand_label, enemy_rand_label, door_rand_label, lock_rand_label]:
            status_layout.addWidget(label)

        # Character selection section
        char_label = QLabel("Choose who you are playing as:")
        main_layout.addWidget(char_label)

        # Button grid
        button_layout = QHBoxLayout()
        
        # Left column (Jill)
        jill_layout = QVBoxLayout()
        jill_normal = QPushButton("Jill - Normal")
        jill_hard = QPushButton("Jill - Hard")
        jill_layout.addWidget(jill_normal)
        jill_layout.addWidget(jill_hard)
        
        # Right column (Chris)
        chris_layout = QVBoxLayout()
        chris_normal = QPushButton("Chris - Normal")
        chris_hard = QPushButton("Chris - Hard")
        chris_layout.addWidget(chris_normal)
        chris_layout.addWidget(chris_hard)
        
        # Add columns to button layout
        button_layout.addLayout(jill_layout)
        button_layout.addLayout(chris_layout)

        # Style buttons
        for button in [jill_normal, jill_hard, chris_normal, chris_hard]:
            button.setFixedSize(150, 40)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #333333;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
            """)

        # Add layouts to main layout
        main_layout.addLayout(button_layout)
        main_layout.addLayout(status_layout)
        
        # Warning message
        warning_label = QLabel("DO NOT CLOSE THIS WINDOW UNTIL YOU HAVE FINISHED PLAYING OR YOUR ITEMS WILL STOP BEING RANDOMIZED!")
        warning_label.setStyleSheet("color: red;")
        warning_label.setWordWrap(True)
        warning_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(warning_label)

        # Set global window styles
        self.setStyleSheet("""
            background-color: #f0f0f0;
            color: #111111;
            font-family: Arial;
            font-size: 14px;
            """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
