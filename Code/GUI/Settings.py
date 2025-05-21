import json
from display_sim import SimDisplay
from PIL import ImageFont

#Fonts:
# Schriftgröße 14 normal
font_small = ImageFont.truetype("arial.ttf", 16)

# Schriftgröße 24 fett (bold)
font_normal = ImageFont.truetype("arial.ttf", 20)  # Arial Bold

# Schriftgröße 18 kursiv
font_big = ImageFont.truetype("arialbd.ttf", 22)  # Arial Italic


display = SimDisplay()


cursor = 0  # Ausgewählter Button (0–4)

def draw_buttons():
    display.clear("black")

    font_to_use = font_big if cursor == 1 else font_normal if cursor in [0, 2] else font_small
    display.draw.text((10, 40), "Test1", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 2 else font_normal if cursor in [1, 3] else font_small
    display.draw.text((10, 60), "Test2", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 3 else font_normal if cursor in [2, 4] else font_small
    display.draw.text((10, 80), "Test3", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 4 else font_normal if cursor in [3, 5] else font_small
    display.draw.text((10, 100), "Test4", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 5 else font_normal if cursor in [4, 6] else font_small
    display.draw.text((10, 120), "Test5", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 6 else font_normal if cursor in [5, 7] else font_small
    display.draw.text((10, 140), "Test6", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 7 else font_normal if cursor in [6, 8] else font_small
    display.draw.text((10, 160), "Test7", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 8 else font_normal if cursor in [7, 9] else font_small
    display.draw.text((10, 180), "Test8", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 9 else font_normal if cursor in [8, 10] else font_small
    display.draw.text((10, 200), "Test9", font=font_to_use , fill="white")

    font_to_use = font_big if cursor == 10 else font_normal if cursor in [9, 11] else font_small
    display.draw.text((10, 220), "Test10", font=font_to_use , fill="white")

    display.show()

def on_key(event):
    global cursor
    key = event.keysym

    if key == "Up":
        cursor = max(0, cursor - 1)
    elif key == "Down":
        cursor = min(10, cursor + 1)
    elif key == "Return":
        print(f"⏎ Button {cursor} gedrückt!")


    draw_buttons()

# Tasteneingaben aktivieren
display.window.bind("<Key>", on_key)

# Erste Anzeige
draw_buttons()

# Starten
display.mainloop()


# Einstellung speichern
settings = {"dark_mode": True}
with open("settings.json", "w") as f:
    json.dump(settings, f)

# Einstellung laden
with open("settings.json", "r") as f:
    loaded_settings = json.load(f)

print(loaded_settings["dark_mode"])  # Gibt: True aus
