import sqlite3
import sys
sys.path.append(r"C:\Users\Santo\Desktop\django_project\blog\requirements")
from mac import get_mac_address
# from blog.requirements.mac import get_mac_address
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
mac_address = get_mac_address()

def getCurrentUser(): 
    cursor.execute("SELECT * FROM logged WHERE mac = ?", (mac_address,))
    user = cursor.fetchall()
    userId = " "
    if user:
        for info in user:
            userId = info[0]
    return userId
    