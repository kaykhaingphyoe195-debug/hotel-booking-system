# Hotel Booking System

A simple Hotel Booking System built with Python, PyQt5 and SQLite3.

## Features

- User Registration
- User Login
- SQLite3 database
- Username/email duplicate validation
- Password confirmation
- Invalid login error handling
- Hotel room list
- Room booking
- Logout

## Project Structure

- `main.py` - starts the application and contains the hotel booking screen
- `login.py` - login GUI and authentication
- `register.py` - registration GUI
- `database.py` - SQLite database operations
- `init_db.py` - database initialization
- `hotel_booking.db` - SQLite database

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python init_db.py
python main.py
```
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for suggestions and bug reports.
## Database Schema

### users

| Field | Type |
|---|---|
| id | INTEGER PRIMARY KEY |
| username | TEXT UNIQUE |
| password | TEXT |
| email | TEXT UNIQUE |

### rooms

| Field | Type |
|---|---|
| room_id | INTEGER PRIMARY KEY |
| room_number | TEXT UNIQUE |
| room_type | TEXT |
| price | REAL |
| status | TEXT |
# Hotel Booking System

A web-based application designed to streamline room reservations, manage guest bookings, and optimize hotel management operations.
## Installation Guide

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/hotel-booking-system.git](https://github.com/your-username/hotel-booking-system.git)
## Key Features

- User Authentication: Secure registration and login for guests and admins.
- Room Browsing: View available rooms with details, pricing, and amenities.
- Online Booking: Easy step-by-step room reservation process.
- Admin Dashboard: Manage bookings, update room statuses, and view customer reports.

## Tech Stack

- Frontend: HTML5, CSS3, JavaScript
- Backend: Node.js / Python / PHP (Adjust based on your project)
- Database: MySQL / PostgreSQL / MongoDB
## License

This project is licensed under the MIT License - see the LICENSE file for details.
## Database Structure

The database includes the following main entities:
- Users: Stores user profiles and authentication data.
- Rooms: Holds room numbers, types, status, and nightly rates.
- Bookings: Tracks check-in/check-out dates, total cost, and booking statuses.
- Payments: Records transaction history and payment methods.

## Project Status

This project is currently under active development. New updates and bug fixes are pushed regularly.
## GitHub

Recommended repository name:

`hotel-booking-pyqt`

The project can be developed using separate branches such as:

- `main`
- `feature-login`
- `feature-registration`

## Author
Kay Khaing Phyo
