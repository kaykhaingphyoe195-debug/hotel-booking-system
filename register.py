from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from database import register_user


class RegisterWindow(QWidget):
    def __init__(self, login_window=None):
        super().__init__()
        self.login_window = login_window
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Hotel Booking System - Registration")
        self.setFixedSize(430, 560)

        title = QLabel("CREATE ACCOUNT")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Register for Hotel Booking")
        subtitle.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.setEchoMode(QLineEdit.Password)

        register_btn = QPushButton("Register")
        register_btn.clicked.connect(self.register)

        back_btn = QPushButton("Back to Login")
        back_btn.setObjectName("secondary")
        back_btn.clicked.connect(self.back_to_login)

        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(self.username)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.confirm_password)
        layout.addWidget(register_btn)
        layout.addWidget(back_btn)

        main = QVBoxLayout(self)
        main.addStretch()
        main.addWidget(card)
        main.addStretch()

    def register(self):
        username = self.username.text().strip()
        email = self.email.text().strip()
        password = self.password.text()
        confirm = self.confirm_password.text()

        if not username or not email or not password or not confirm:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Input Error", "Please enter a valid email.")
            return

        if len(password) < 4:
            QMessageBox.warning(self, "Input Error", "Password must contain at least 4 characters.")
            return

        if password != confirm:
            QMessageBox.warning(self, "Input Error", "Passwords do not match.")
            return

        success, message = register_user(username, password, email)

        if success:
            QMessageBox.information(self, "Success", message)
            self.back_to_login()
        else:
            QMessageBox.critical(self, "Registration Failed", message)

    def back_to_login(self):
        self.close()
        if self.login_window:
            self.login_window.show()
