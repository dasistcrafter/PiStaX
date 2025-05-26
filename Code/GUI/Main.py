from display_sim import SimDisplay
from PIL import ImageFont
import json
import psutil
import datetime
import subprocess
import socket
import time

# Fonts
font_stats = ImageFont.truetype("arial.ttf", 14)
font_time = ImageFont.truetype("arialbd.ttf", 14)

#key tracking
last_key = None
ipshow = False

# Load config
with open("settings.json", "r") as f:
    data = json.load(f)

display = SimDisplay()
select = 0
stats_shown = 0

# Connection checks
def is_wifi_connected():
    return bool(subprocess.getoutput("iwgetid -r"))

def is_bluetooth_on():
    return "UP RUNNING" in subprocess.getoutput("hciconfig")

def has_ip_address():
    try:
        socket.gethostbyname("google.com")
        return True
    except socket.gaierror:
        return False

def draw_buttons():
    display.clear("black")

    button_width = 40
    spacing = 6
    total_width = 5 * button_width + 4 * spacing
    start_x = (240 - total_width) // 2

    for i in range(5):
        x = start_x + i * (button_width + spacing)
        outline_color = "white"
        line_width = 4 if i == select else 2
        display.draw.rounded_rectangle(
            (x, 30, x + button_width, 70),
            radius=10,
            outline=outline_color,
            width=line_width
        )

    top_bar()
    show_stats()
    display.show()

def top_bar():
    now = datetime.datetime.now()

    if data.get("Time") == True:
        display.draw.text((175, 10), now.strftime("%X"), font=font_time, fill="white")

    if data.get("Date") == True:
        display.draw.text((10, 10), now.strftime("%x"), font=font_time, fill="white")

    if data.get("Time") == True:
        if is_wifi_connected():
            display.draw.text((75, 10), "WiFi", font=font_time, fill="white")

        if is_bluetooth_on():
            display.draw.text((100, 10), "BT", font=font_time, fill="white")

        if has_ip_address():
            display.draw.text((125, 10), "IP", font=font_time, fill="white")




def show_stats():
    global stats_shown
    stats_shown = 0

    if data.get("CPU_usage") == True:
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"CPU: {psutil.cpu_percent(interval=None)}%",
                          font=font_stats, fill="white")

    if data.get("CPU_temp") == True:
        freq = psutil.cpu_freq(percpu=False)
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"CPU frequency: {freq.current:.1f} MHz",
                          font=font_stats, fill="white")

    if data.get("RAM_usage") == True:
        ram = psutil.virtual_memory()
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"RAM: {ram.percent}%",
                          font=font_stats, fill="white")

    if data.get("Storage_usage") == True:
        disk = psutil.disk_usage('/')
        stats_shown += 1

        display.draw.text((10, (stats_shown * 20) + 100),
                        f"Storage: {disk.percent}%",
                        font=font_stats, fill="white")
            
        
    if data.get("show_ip") == True:
        stats_shown += 1
        if ipshow == False:
            display.draw.text((10, (stats_shown * 20) + 100),
                         f"press \"I\"+\"P\" to reveal IP" ,
                          font=font_stats, fill="white")        
        else:

            display.draw.text((10, (stats_shown * 20) + 100),
                            f"Test Ip" ,
                            font=font_stats, fill="white")
        
                                 

    
def on_key(event):
    global select, last_key, ipshow

    key = event.keysym.lower()

    if key == "left":
        select = max(0, select - 1)
    elif key == "right":
        select = min(4, select + 1)
    elif key == "return":
        print(f"⏎ Button {select + 1} pressed!")

    # Check for 'i' then 'p'
    if last_key == "i" and key == "p":
        ipshow = True
        display.window.after(2000, lambda: set_ipshow(False))  # auto-hide IP after 2 sec

    last_key = key
    draw_buttons()

def set_ipshow(value):
    global ipshow
    ipshow = value
    draw_buttons()

# Bind keyboard
display.window.bind("<Key>", on_key)

# Initial draw
draw_buttons()

# Auto update loop
def update_loop():
    draw_buttons()
    display.window.after(1000, update_loop)

update_loop()
display.mainloop()
