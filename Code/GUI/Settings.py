import json
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
    "Test9",
    "Test10"
]

home_menu_entries = [
    "CPU usage",
    "Ram usage",
    "CPU temp",
    "Storage usage",
]

home_menu_entries_true = [
    "CPU_usage",
    "Ram_usage",
    "CPU_temp",
    "Storage_usage",
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

    base_y = 40
    spacing = 30  # etwas mehr Platz für Checkboxen

    for i, label in enumerate(home_menu_entries):
        # Schriftgröße abhängig von Cursor
        if i == cursor:
            font = font_big
            box_width = 3
        elif abs(i - cursor) == 1:
            font = font_normal
            box_width = 2
        else:
            font = font_small
            box_width = 1

        y = base_y + i * spacing

        display.draw.text((10, y), label, font=font, fill="white")


        if data.get(home_menu_entries_true[i]) == True:
            fill_color = "white"
        else:
            fill_color = "black"

        display.draw.rectangle((200, y + 6, 220, y + 26), outline="white", fill=fill_color, width=box_width)


    display.show()



def on_key(event):
    global cursor, current_screen

    key = event.keysym

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
            key_name = home_menu_entries_true[cursor]
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

def niu ():

    # Einstellung speichern
    settings = {"dark_mode": True}
    with open("settings.json", "w") as f:
      json.dump(settings, f)

    # Einstellung laden
    with open("settings.json", "r") as f:
        loaded_settings = json.load(f)

    print(loaded_settings["dark_mode"])  # Gibt: True aus
