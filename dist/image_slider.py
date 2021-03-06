import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Simple input for file name
        self.file1 = tk.Label(self, text="File 1")
        self.file1.grid(row=0, column=0)
        self.entry1 = tk.Entry(self)
        self.entry1.insert(10, "img1.png")
        self.entry1.grid(row=0, column=1, pady=10, sticky="nsew")

        self.file2 = tk.Label(self, text="File 2")
        self.file2.grid(row=1, column=0)
        self.entry2 = tk.Entry(self)
        self.entry2.insert(10, "img2.png")
        self.entry2.grid(row=1, column=1, sticky="nsew")
        
        self.enter = tk.Button(self, text='Start', command=self.available_image)
        self.enter.grid(row=2, column=0, padx=10, pady=20, sticky="nsew")


    def available_image(self):
        # Check whether the given filename exist
        try:
            Image.open("image/" + self.entry1.get())
            Image.open("image/" + self.entry2.get())
            self.create_slider()
            self.file1.delete()
            self.file2.delete()
            self.entry1.delete()
            self.entry2.delete()
            self.fileNotFound.delete()
            self.enter.delete()
        except:
            print("image/" + self.entry1.get())


    def create_slider(self):
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        file1 = "image/" + self.entry1.get()
        file2 = "image/" + self.entry2.get()
        # CREATING IMAGES
        size = (self.screenWidth, self.screenHeight)
        self.img1 = ImageTk.PhotoImage(Image.open(file1).resize(size))
        self.canv1 = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight, 
            highlightthickness=0, bd=0)
        self.canv1.grid(row=0, column=0, sticky="nsew")
        self.canv1.create_image(self.screenWidth/2, self.screenHeight/2, image=self.img1, anchor="center")

        self.img2 = ImageTk.PhotoImage(Image.open(file2).resize(size))
        self.canv2 = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight, 
            highlightthickness=0, bd=0)
        self.canv2.grid(row=0, column=0, sticky="nsw")
        self.canv2.create_image(self.screenWidth/2, self.screenHeight/2, image=self.img2, anchor="center")

        self.line = self.canv2.create_line(self.screenWidth/2, 0, self.screenWidth/2, self.screenHeight, 
            width=4, fill="white")    

        # self.circleImage = ImageTk.PhotoImage(Image.open("resources/circle.png").resize((64, 64)))
        # self.circle = self.canv2.create_image(self.screenWidth/2, self.screenHeight/2, image=self.circleImage) 
        self.canv2.bind('<B1-Motion>', self.slide_image)
    

    def slide_image(self, event):
        cur_length = int(event.x)
        cur_height = int(event.y)
        # if cur_height > ((self.screenHeight/2) - 100) and cur_height < ((self.screenHeight/2) + 100):
        print(cur_length, cur_height)
        # if cur_length < self.screenWidth: 
        self.canv2.config(width=cur_length)
        self.canv2.coords(self.line, cur_length, 0, cur_length, self.screenHeight)
            # self.canv2.coords(self.circle, cur_length, self.screenHeight/2)
        # else:
            # self.canv2.config(width=self.screenWidth)
            # self.canv2.coords(self.line, self.screenWidth, 0, self.screenWidth, self.screenHeight)
            # self.canv2.coords(self.circle, self.screenWidth, self.screenHeight/2)

def main():
    root = tk.Tk()
    root.state('zoomed')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Image Slider")
    app = Application(master=root)
    app.mainloop()
    

if __name__ == '__main__':
    main()
