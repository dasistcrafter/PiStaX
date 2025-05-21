# main.py
from display_sim import SimDisplay  # später: import ST7789

display = SimDisplay()

# Text und Formen anzeigen
display.clear("black")
display.draw.rectangle((10, 10, 230, 230), outline="white")
display.draw.text((70, 110), "Hello ST7789!", fill="lime")
display.show()

# Warten (GUI anzeigen)
display.mainloop()
