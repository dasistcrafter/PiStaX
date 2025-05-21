from display_sim import SimDisplay

display = SimDisplay()
select = 0  # Ausgewählter Button (0–4)

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
            (x, 10, x + button_width, 50),
            radius=10,
            outline=outline_color,
            width=line_width
        )
    display.show()

def on_key(event):
    global select
    key = event.keysym

    if key == "Left":
        select = max(0, select - 1)
    elif key == "Right":
        select = min(4, select + 1)
    elif key == "Return":
        print(f"⏎ Button {select + 1} gedrückt!")

    draw_buttons()

# Tasteneingaben aktivieren
display.window.bind("<Key>", on_key)

# Erste Anzeige
draw_buttons()

# Starten
display.mainloop()
