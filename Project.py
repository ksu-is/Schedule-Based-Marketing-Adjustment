from appointmentCreator import *
import sqlite3

conn = sqlite3.connect('appointment_information.db')
c = conn.cursor()
date_entry = Entry()

def enter_data():
    return date_entry.get()

data = enter_data()

if data == "":
    print("Increase marketing spending")
else:
    if check_data_existence(data):
        print("Decrease marketing spending")
    else:
        print("No action needed")
