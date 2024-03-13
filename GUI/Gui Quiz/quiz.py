from tkinter import *
import random 


names_list = []

global questions_answers
asked = []
score = 0


def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()
        
question_answers = {
    1: ["What will be the output of the following code : print(type(type(int)))",
        "type 'int'",
        "type 'type'",
        "Error",
        "0"],
    2: ["What is the output of the following code : L = ['a','b','c','d'] print(''.join(L))",
        "Error",
        "None",
        "abcd",
        "L"],
    3: ["What does the 'range' function in Python return?",
        "A list of integers",
        "A tuple of integers",
        "A generator object",
        "An error"],
    4: ["What is the result of 3*1**3?",
        "3",
        "9",
        "27",
        "1"],
    5: ["Which of the following is not a valid variable name in Python?",
        "my-var",
        "_my_var",
        "myVar",
        "MyVar"],
    6: ["What is the output of the following code : 'hello'.upper()",
        "HELLO",
        "hello",
        "Error",
        "'HELLO'"],
    7: ["What will be the output of the following code : 'Python'[1:4]",
        "yth",
        "Pyt",
        "thon",
        "Py"],
    8: ["What is the result of 2**3**2?",
        "512",
        "64",
        "72",
        "28"],
    9: ["Which of the following is used to create a comment in Python?",
        "#",
        "//",
        "/* */",
        "<!-- -->"],
    10: ["What is the output of the following code : 5 == 5.0",
         "True",
         "False",
         "Error",
         "None of the above"]
}


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
        Quiz(root)

        
        
class Quiz:
    def __init__(self, parent):
        background_color='OldLace'
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        randomiser()
        
        self.question_label = Label (self.quiz_frame, text = question_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0, padx=10,pady=10)
        
        self.var1 = IntVar()

        
        self.rb1 = Radiobutton(self.quiz_frame, text=question_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, padx=10,pady=10,variable=self.var1, background = background_color)
        self.rb1.grid(row=1, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame, text=question_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, padx=10,pady=10,variable=self.var1, background = background_color)
        self.rb2.grid(row=2, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame, text=question_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, padx=10,pady=10,variable=self.var1, background = background_color)
        self.rb3.grid(row=3, sticky=W)

        self.rb4 = Radiobutton(self.quiz_frame, text=question_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, padx=10,pady=10,variable=self.var1, background = background_color)
        self.rb4.grid(row=4, sticky=W)


        self.confirm_button = Button(self.quiz_frame, text="Confrim", bg="pink")
        self.confirm_button.grid(row=5)

        
        
        
    






if __name__ == "__main__":
    root = Tk()
    root.title('GUI QUIZ')
    quizStarter_object = QuizStarter(root)
    root.mainloop()
    