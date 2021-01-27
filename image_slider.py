import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.screenWidth = 920
        self.screenHeight = 540
        # Create widgets

        # CREATING IMAGES
        size = (1920, 1080)
        self.img1 = ImageTk.PhotoImage(Image.open("img1.png").resize(size))
        self.canv1 = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight, 
            highlightthickness=0, bd=0)
        self.canv1.grid(row=0, column=0, sticky="nsew")
        self.canv1.create_image(0, 0, image=self.img1, anchor="center")

        self.img2 = ImageTk.PhotoImage(Image.open("img2.png").resize(size))
        self.canv2 = tk.Canvas(self, width=(self.screenWidth/2)+2, height=self.screenHeight, 
            highlightthickness=0, bd=0)
        self.canv2.grid(row=0, column=0, sticky="nsw")
        self.canv2.create_image(0, 0, image=self.img2, anchor="center")
    
        self.line = self.canv2.create_line(self.screenWidth/2, 0, self.screenWidth/2, self.screenHeight, 
            width=4, fill="white")    

        # self.circleImage = ImageTk.PhotoImage(Image.open("resources/circle.png").resize((64, 64)))
        # self.circle = self.canv2.create_image(self.screenWidth/2, self.screenHeight/2, image=self.circleImage) 
        self.canv2.bind('<B1-Motion>', self.slide_image)
    

    def slide_image(self, event):
        cur_length = int(event.x)
        cur_height = int(event.y)
        # if cur_height > ((self.screenHeight/2) - 100) and cur_height < ((self.screenHeight/2) + 100):
        if cur_length < self.screenWidth: 
            self.canv2.config(width=cur_length)
            self.canv2.coords(self.line, cur_length, 0, cur_length, self.screenHeight)
            # self.canv2.coords(self.circle, cur_length, self.screenHeight/2)
        else:
            self.canv2.config(width=self.screenWidth)
            self.canv2.coords(self.line, self.screenWidth, 0, self.screenWidth, self.screenHeight)
            # self.canv2.coords(self.circle, self.screenWidth, self.screenHeight/2)

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.geometry('+%d+%d' % (0, 0))
    root.title("Image Slider")
    app.mainloop()

if __name__ == '__main__':
    main()
