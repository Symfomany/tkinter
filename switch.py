import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.ttk as ttk
import csv

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,  **kwargs)
        
        self.title_font = tkfont.Font(family='Roboto', size=18, weight="normal")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self,  width=768, height=576)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, Result):
            if F.__name__ == "Result": 
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")           
            else:
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Go to Page Trois",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("Result"))
        button.pack()



class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=768, height=576)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(pady=10)
        
        l = tk.Label (text = "Type de mesure")
        l.pack()

        e1 = tk.Entry(self)

        l = tk.Label (text = "Foret")
        l.pack()

        e2 = tk.Entry(self)
        e1.pack( pady=10)
        e2.pack(pady=10)

        o = ttk.Combobox(self, values=["ligne 1", "ligne 2", "ligne 3", "ligne 4"])
        o.pack(pady=10)
        

        var_choix = ""

        choix_rouge = tk.Radiobutton(self, text="Rouge", variable=var_choix, value="rouge")
        choix_vert = tk.Radiobutton(self, text="Vert", variable=var_choix, value="vert")
        choix_bleu = tk.Radiobutton(self, text="Bleu", variable=var_choix, value="bleu")

        choix_rouge.pack()
        
        choix_vert.pack()
        choix_bleu.pack()

      
        button = tk.Button(self, text="Submit Form",
                           command=lambda: controller.show_frame("Result"))
        
        button.pack()

        # cadre = tk.Frame(self, width=768, height=576, borderwidth=1)
        # cadre.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



class Result(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open('./results.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()