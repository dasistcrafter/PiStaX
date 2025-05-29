from display_sim import SimDisplay
from PIL import ImageFont
from PIL import Image
import json
import psutil
import datetime
import subprocess
import socket

# Fonts
font_stats = ImageFont.truetype("arial.ttf", 14)
font_time = ImageFont.truetype("arialbd.ttf", 14)

#wifi logo
Wifi_logo = [
    (76,13), (76,14), (77,13), (77,16), (77,17),
    (78,12), (78,15), (78,16), (79,12), (79,15),
    (79,18), (79,19), (80,12), (80,15), (80,18),
    (81,12), (81,15), (81,18), (81,20), (81,21),
    (82,12), (82,15), (82,18), (82,20), (82,21),
    (83,12), (83,15), (83,18), (84,12), (84,15),
    (84,18), (84,19), (85,12), (85,15), (85,16),
    (86,13), (86,16), (86,17), (87,13), (87,14)
]


#get IPv4
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


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
            for x, y in Wifi_logo:
                display.draw.point((x, y), fill="white")

        if is_bluetooth_on():
            display.draw.text((100, 10), "BT", font=font_time)

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
            if data.get("ip_timeout") != False:
                display.draw.text((10, (stats_shown * 20) + 100),
                            f"press \"I\"+\"P\" to reveal IP" ,
                            font=font_stats, fill="white")        
        else:
            display.draw.text((10, (stats_shown * 20) + 100),
                            IPAddr ,
                            font=font_stats, fill="white")
        if data.get("ip_timeout") == False:
            display.draw.text((10, (stats_shown * 20) + 100),
                            f"Test Ip" ,
                            font=font_stats, fill="white")
                                 

    
def on_key(event):
    global select, last_key, ipshow, ipshow_time
    ipshow_time = data.get("ip_timeout") * 1000 #convert the seconds to ms
    key = event.keysym.lower()

    if key == "left":
        select = max(0, select - 1)
    elif key == "right":
        select = min(4, select + 1)
    elif key == "return":
        print(f"⏎ Button {select + 1} pressed!")

    # Check for i then p
    if last_key == "i" and key == "p":
        if data.get("ip_timeout") != False:
            if data.get("ip_timeout") != True:
                ipshow = True
                display.window.after(ipshow_time, lambda: set_ipshow(False))

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
