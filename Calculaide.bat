@echo off
start cmd /k "cd /d C:\Users\erick\PycharmProjects\calculaide\venv\Scripts & activate & cd /d "C:\Users\erick\PycharmProjects\calculaide\src\" & python manage.py runserver"

timeout 3

start "" "C:\Program Files\Mozilla Firefox\firefox.exe" --kiosk http://127.0.0.1:8000
