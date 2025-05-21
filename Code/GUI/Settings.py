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

# Menüeinträge
menu_entries = [
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

cursor = 0
current_screen = None  # Wird später gesetzt


def main():
    global current_screen
    current_screen = main

    display.clear("black")
    display.draw.text((10, 10), "Settings", font=font_big2x, fill="white")

    base_y = 40
    spacing = 20
    offset_down = 10

    for i, label in enumerate(menu_entries):
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
    display.draw.text((10, 10), "Home_menue", font=font_big2x, fill="white")
    display.show()


def on_key(event):
    global cursor

    key = event.keysym

    if key == "Up":
        cursor = max(0, cursor - 1)
    elif key == "Down":
        cursor = min(len(menu_entries) - 1, cursor + 1)
    elif key == "Return":
        print(f"⏎ Button {cursor} gedrückt: {menu_entries[cursor]}")

        elif menu_entries[cursor] == "Home_menue":
            home_menue()
            return
    
        elif key == "Escape":
        print("🔙 Zurück zum Hauptmenü")
    current_screen = main
    current_screen()


    # Nach Eingabe: aktuellen Screen erneut anzeigen
    current_screen()


# Tasteneingaben aktivieren
display.window.bind("<Key>", on_key)

# Erste Anzeige
main()

# Starten
display.mainloop()

# Einstellung speichern
settings = {"dark_mode": True}
with open("settings.json", "w") as f:
    json.dump(settings, f)

# Einstellung laden
with open("settings.json", "r") as f:
    loaded_settings = json.load(f)

print(loaded_settings["dark_mode"])
