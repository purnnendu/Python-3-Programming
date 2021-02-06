import PIL

img = PIL.Image("1217-Steve-Jobs-Quote-Think-Different.jpg")
win = PIL.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = PIL.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = PIL.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()

