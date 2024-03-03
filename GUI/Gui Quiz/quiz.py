from tkinter import *


names_list = []

class QuizStarter:
    def __init__(self, parent):
        background_color='OldLace'
        
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        self.heading_label = Label (self.quiz_frame,
                                    text="GUI QUIZ",
                                    font=("Tw Cen MT", "18", "bold"),
                                    bg=background_color)
        self.heading_label.grid(row=0)

        self.user_label = Label(self.quiz_frame,
                                text='Please enter you name below',
                                font=("Tw Cen MT", "18", "bold"),
                                bg=background_color)
        self.user_label.grid(row=1, pady=20)
        
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)
        
        self.contunue_button = Button(self.quiz_frame,
                                      text='Continue',
                                      bg='pink',
                                      command=self.name_collection)
        self.contunue_button.grid(row=3, pady=3)
        
    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()
        
        
        






if __name__ == "__main__":
    root = Tk()
    root.title('GUI QUIZ')
    quizStarter_object = QuizStarter(root)
    root.mainloop()
    