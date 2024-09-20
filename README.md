# ISS Overhead Alert System

This Python script monitors the International Space Station (ISS) and sends an alert when the ISS is overhead during nighttime. It uses APIs to fetch ISS position data, sunrise/sunset times, and sends email notifications.

## Prerequisites

1. Python 3.x installed.
2. Required Python packages:
   - `requests`
   - `smtplib`
   - `dotenv`

## Setup

1. Clone this repository or download the script.
2. Create a `.env` file in the same directory with the following content:

my_email=your_email@gmail.com password=your_email_password (app password in gmail)

Replace `your_email@gmail.com` and `your_email_password` with your actual Gmail credentials. 3. Run the script (`python iss_alert.py`).

## Functionality

- Fetches ISS position data.
- Determines if the ISS is overhead within a specified latitude/longitude range.
- Checks if it's nighttime based on sunrise/sunset times.
- Sends an email alert if the ISS is overhead during nighttime.

## Notes

- Adjust the latitude/longitude coordinates (`MY_LAT` and `MY_LONG`) as needed.
- Ensure your Gmail account allows "Less secure apps" (for sending emails).
