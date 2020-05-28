#########################################################
#           Pepper communications platform
#########################################################
from tkinter import *


# window = tk.Tk()
# label = tk.Label(
#     text="Python Demo\n2nd line",
#     fg="white",
#     bg="black",
#     width=125,
#     height=100
# )
# label.pack()
# window.mainloop()

class Window(Frame):

   # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Pepper Communication Platform")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit", command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        exit()



root = Tk()

#size of the window
root.geometry("1000x800")

app = Window(root)
root.mainloop()
