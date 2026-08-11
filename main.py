import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt
from database import create_tables, seed_rooms, get_connection
from login import LoginWindow


class BookingWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setup_ui()
        self.load_rooms()

    def setup_ui(self):
        self.setWindowTitle("Hotel Booking System")
        self.resize(800, 600)

        title = QLabel("Hotel Booking System")
        title.setObjectName("title")

        welcome = QLabel(
            f"Welcome, {self.user[1]}   |   Email: {self.user[2]}"
        )

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Room ID", "Room No.", "Room Type", "Price ($)", "Status"]
        )
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        book_btn = QPushButton("Book Selected Room")
        book_btn.clicked.connect(self.book_room)

        logout_btn = QPushButton("Logout")
        logout_btn.clicked.connect(self.logout)

        buttons = QHBoxLayout()
        buttons.addWidget(book_btn)
        buttons.addWidget(logout_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addSpacing(10)
        layout.addWidget(self.table)
        layout.addLayout(buttons)

    def load_rooms(self):
        conn = get_connection()
        rooms = conn.execute(
            "SELECT room_id, room_number, room_type, price, status FROM rooms"
        ).fetchall()
        conn.close()

        self.table.setRowCount(len(rooms))

        for row, room in enumerate(rooms):
            for col, value in enumerate(room):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def book_room(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(self, "No Selection", "Please select a room.")
            return

        room_id = int(self.table.item(row, 0).text())
        room_no = self.table.item(row, 1).text()
        status = self.table.item(row, 4).text()

        if status != "Available":
            QMessageBox.warning(self, "Unavailable", "This room is not available.")
            return

        conn = get_connection()
        conn.execute(
            "UPDATE rooms SET status = 'Booked' WHERE room_id = ?",
            (room_id,)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(
            self, "Booking Successful",
            f"Room {room_no} has been booked successfully."
        )
        self.load_rooms()

    def logout(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()


def apply_style(app):
    app.setStyleSheet("""
        QWidget {
            background: #f4f6f8;
            font-family: Arial;
            font-size: 14px;
        }

        QFrame#card {
            background: white;
            border-radius: 15px;
            padding: 25px;
        }

        QLabel#title {
            font-size: 25px;
            font-weight: bold;
            padding: 10px;
        }

        QLineEdit {
            background: white;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 12px;
        }

        QPushButton {
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px;
            font-weight: bold;
        }

        QPushButton:hover {
            background: #1d4ed8;
        }

        QPushButton#secondary {
            background: #64748b;
        }

        QTableWidget {
            background: white;
            border: 1px solid #d1d5db;
        }

        QHeaderView::section {
            padding: 8px;
            font-weight: bold;
        }
    """)


if __name__ == "__main__":
    create_tables()
    seed_rooms()

    app = QApplication(sys.argv)
    apply_style(app)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec_())
