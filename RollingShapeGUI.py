import tkinter
from PIL import Image, ImageTk
root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)
shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="blue")
image1 = ImageTk.PhotoImage(Image.open("dvdimages.png"))
logo_id = myCanvas.create_image(100, 100, image=image1)
img_w = image1.width()
img_h = image1.height()
#initialize the constants xx, yy
xx = yy = 3
def move_shape():
    global xx, yy
    #move the shape with the constant xx, yy
    myCanvas.move(shape1, xx, yy)
    myCanvas.move(logo_id, xx, yy)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    x_img, y_img = myCanvas.coords(logo_id)
    img_left = x_img - (img_w / 2)
    img_right = x_img + (img_w / 2)
    img_top = y_img - (img_h / 2)
    img_bottom = y_img + (img_h / 2)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800 or img_left <= 0 or img_right >= 800:
        xx = -xx
    if y1 <= 0 or y2 >= 600 or img_top <= 0 or img_bottom >= 600:
        yy = -yy
    #call the function recursively
    myCanvas.after(30, move_shape)


#in the main program call the function move_shape()
myCanvas.after(10,move_shape)
myCanvas.pack()
root.mainloop()
