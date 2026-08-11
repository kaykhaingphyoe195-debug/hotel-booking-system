from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from database import authenticate_user
from register import RegisterWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.register_window = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Hotel Booking System - Login")
        self.setFixedSize(430, 500)

        title = QLabel("HOTEL BOOKING SYSTEM")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Login to your account")
        subtitle.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)

        register_btn = QPushButton("Create New Account")
        register_btn.setObjectName("secondary")
        register_btn.clicked.connect(self.open_register)

        password_row = QHBoxLayout()
        password_row.addWidget(self.password)

        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(15)
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(15)
        card_layout.addWidget(self.username)
        card_layout.addWidget(self.password)
        card_layout.addWidget(login_btn)
        card_layout.addWidget(register_btn)

        main = QVBoxLayout(self)
        main.addStretch()
        main.addWidget(card)
        main.addStretch()

    def login(self):
        username = self.username.text().strip()
        password = self.password.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please enter username and password.")
            return

        user = authenticate_user(username, password)

        if user:
            from main import BookingWindow
            self.booking_window = BookingWindow(user)
            self.booking_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

    def open_register(self):
        self.register_window = RegisterWindow(self)
        self.register_window.show()
        self.hide()
