from PIL import Image


xcordprintstart = 75      #int(input("enterX"))
ycordprintstart = 10      #int(input("enterY"))
ycordprint = ycordprintstart
xcordprint = xcordprintstart
x = 1
y = 1

currentpx = 0
color = "white"

#decoding pixe
im = Image.open(r"Wifi_logo.png")
with Image.open(r"Wifi_logo.png") as img:
    width , height = img.size

px = im.load()

width -=1
height -=1
while x != height:

    if y == width:
        y=0
        x+=1
        
    y +=1
    #print(currentpx)
    #print(x)
    #print(y)
    currentpx = [px[x,y]]

    if currentpx == [(255, 255, 255, 255)]:

        ycordprint = ycordprintstart
        xcordprint = xcordprintstart
        ycordprint = ycordprintstart + y
        xcordprint = xcordprintstart + x
        print(f"\t\t\tdisplay.draw.point(({xcordprint},{ycordprint}), fill=\"white\")")
