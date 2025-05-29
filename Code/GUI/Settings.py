import json
from tkinter import Image
from display_sim import SimDisplay
from PIL import ImageFont

# Fonts
font_small = ImageFont.truetype("arial.ttf", 16)
font_normal = ImageFont.truetype("arial.ttf", 18)
font_big = ImageFont.truetype("arialbd.ttf", 22)
font_big2x = ImageFont.truetype("arialbd.ttf", 28)

# Display
display = SimDisplay()

#load settings
with open("settings.json", "r") as f:
    data = json.load(f)

#load image
imgWifi = Image.open("Wifi_logo.png").convert("RGBA")



# Menüeinträge
main_menu_entries = [
    "Test1",
    "Test2",
    "Test3",
    "Test4",
    "Home_menue",
    "Show Usage",
    "Test7",
    "Test8",
    "Test9"
]

home_menu_entries = [
    "CPU_usage",
    "Ram_usage",
    "CPU_temp",
    "Storage_usage",
    "Time",
    "Date",
    "show_ip",
    "ip_timeout",
    "Location",
    "weather"
]

cursor = 0
current_screen = None

def save_settings():
    with open("settings.json", "w") as f:
        json.dump(data, f)

def main():
    global current_screen
    current_screen = main

    display.clear("black")
    display.draw.text((10, 10), "Main Menu", font=font_big2x, fill="white")

    base_y = 40
    spacing = 20
    offset_down = 10

    for i, label in enumerate(main_menu_entries):
        if i == cursor:
            font = font_big
        elif abs(i - cursor) == 1:
            font = font_normal
        else:
            font = font_small

        y = base_y + i * spacing
        if i > cursor:
            y += offset_down

        display.draw.text((10, y), label, font=font, fill="white")

    display.show()


def home_menue():
    global current_screen
    current_screen = home_menue

    display.clear("black")
    display.draw.text((10, 10), "Home Menu", font=font_big2x, fill="white")

    base_y = 50
    visible_lines = 6
    spacing = 30 


    scroll_offset = 0
    if cursor > 5:
        scroll_offset = (cursor - 5) * spacing + 10


    for i, label in enumerate(home_menu_entries):
        
        if i == cursor:
            font = font_big
            box_width = 3
        elif abs(i - cursor) == 1:
            font = font_normal
            box_width = 2
        else:
            font = font_small
            box_width = 1

        y = base_y + i * spacing - scroll_offset

        if y < base_y - spacing or y > base_y + visible_lines * spacing:
          continue

        display.draw.text((10, y), label, font=font, fill="white")

        if i > 7:
            base_y -= i * 30


        if data.get(home_menu_entries[i]) == True:
            fill_color = "white"
        else:
            fill_color = "black"

        if i != 7:
            display.draw.rectangle((200, y + 6, 220, y + 26), outline="white", fill=fill_color, width=box_width)
        
        else:
            global ip_sub_text_start
            ip_sub_text_start = " "
            global ip_sub_text_end
            ip_sub_text_end = " "
            if data.get("ip_timeout") == True:
                ip_sub_text_start = " "
                ip_sub_text_end = " "
            if data.get("ip_timeout") == False:
                ip_sub_text_start = " "
                ip_sub_text_end = " "
            if data.get("ip_timeout") == 25:
                ip_sub_text_start = "<"
                ip_sub_text_end = " "
            if data.get("ip_timeout") == 1:
                ip_sub_text_start = " "
                ip_sub_text_end = ">"
            if data.get("ip_timeout") <= 24:
                if data.get("ip_timeout") >= 2:
                    ip_sub_text_start = "<"
                    ip_sub_text_end = ">"
            if data.get("ip_timeout") >= 2:
                if data.get("ip_timeout") <= 24:
                    ip_sub_text_start = "<"
                    ip_sub_text_end = ">"

            global show_ip_time_current
            show_ip_time_current = data.get("ip_timeout")
            display.draw.text((160, y+4), f"{ip_sub_text_start} {show_ip_time_current} {ip_sub_text_end}", font=font_normal, fill="white")
            print(ip_sub_text_end)
            print(ip_sub_text_start)



            

    display.show()



def on_key(event):
    global cursor, current_screen

    key = event.keysym

    if key in ["Left", "Right"]:
        if current_screen == home_menue and cursor == 7:
            key_name = home_menu_entries[cursor]
            if key == "Left":
                data[key_name] = max(1, data.get(key_name, 0) - 1)
            elif key == "Right":
                data[key_name] = min(25, data.get(key_name, 0) + 1)

    save_settings()
    if key == "Up":
        cursor = max(0, cursor - 1)

    elif key == "Down":
        if current_screen == main:
            cursor = min(len(main_menu_entries) - 1, cursor + 1)
        elif current_screen == home_menue:
            cursor = min(len(home_menu_entries) - 1, cursor + 1)

    elif key == "Return":
        print(f"⏎ Button {cursor} gedrückt")

        if current_screen == main and main_menu_entries[cursor] == "Home_menue":
            cursor = 0
            current_screen = home_menue

        elif current_screen == home_menue:
            key_name = home_menu_entries[cursor]
            data[key_name] = not data.get(key_name, False)
            print(f"{key_name}: {data[key_name]}")
            #save
            save_settings()

    elif key == "Escape":
        cursor = 0
        current_screen = main

    current_screen()


# Tasteneingaben aktivieren
display.window.bind("<Key>", on_key)

 # Erste Anzeige
main()

# Starten
display.mainloop()
