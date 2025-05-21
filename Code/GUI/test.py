from PIL import Image, ImageDraw

def draw_toggle(draw, position, size=(60, 30), toggled=False):
    """
    Zeichnet einen Toggle Switch.
    :param draw: ImageDraw Objekt
    :param position: Tuple (x, y) für die linke obere Ecke des Toggles
    :param size: Größe als Tuple (Breite, Höhe)
    :param toggled: bool, True=AN, False=AUS
    """
    x, y = position
    width, height = size
    radius = height // 2  # Für abgerundete Enden

    # Farben
    bg_color = "#4CAF50" if toggled else "#CCC"  # Grün bei AN, Grau bei AUS
    knob_color = "white"

    # Kapsel (Hintergrund) zeichnen: 2 Halbkreise + Rechteck dazwischen
    draw.rounded_rectangle([x, y, x + width, y + height], radius=radius, fill=bg_color)

    # Knopf Position links (aus) oder rechts (an)
    knob_x = x + (width - height) if toggled else x
    knob_y = y

    # Knopf zeichnen (Kreis)
    draw.ellipse([knob_x, knob_y, knob_x + height, knob_y + height], fill=knob_color)

# Beispiel verwenden:

img = Image.new("RGB", (100, 50), "black")
draw = ImageDraw.Draw(img)

draw_toggle(draw, (20, 10), toggled=False)  # AUS
draw_toggle(draw, (20, 50), toggled=True)   # AN (unten, aber evtl raus aus Bild)

img.show()
