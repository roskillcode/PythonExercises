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
        "0",
        2],  

    2: ["What is the output of the following code : L = ['a','b','c','d'] print(''.join(L))",
        "Error",
        "None",
        "abcd",
        "L",
        3],  

    3: ["What does the 'range' function in Python return?",
        "A list of integers",
        "A tuple of integers",
        "A generator object",
        "An error",
        1],  

    4: ["What is the result of 3*1**3?",
        "3",
        "9",
        "27",
        "1",
        1],  

    5: ["Which of the following is not a valid variable name in Python?",
        "my-var",
        "_my_var",
        "myVar",
        "MyVar",
        1],  

    6: ["What is the output of the following code : 'hello'.upper()",
        "HELLO",
        "hello",
        "Error",
        "'HELLO'",
        1], 

    7: ["What will be the output of the following code : 'Python'[1:4]",
        "yth",
        "Pyt",
        "thon",
        "Py",
        1],  

    8: ["What is the result of 2**3**2?",
        "512",
        "64",
        "72",
        "28",
        1],  

    9: ["Which of the following is used to create a comment in Python?",
        "#",
        "//",
        "/* */",
        "<!-- -->",
        1],  

    10: ["What is the output of the following code : 5 == 5.0",
         "True",
         "False",
         "Error",
         "None of the above",
         1]  
}



class QuizStarter:
    def __init__(self, parent):
        background_color='OldLace'
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        self.heading_label = Label (self.quiz_frame,
                                    text="Python Quiz",
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


        self.confirm_button = Button(self.quiz_frame, text="Confrim",font=("Helvetia", "13", "bold"), bg="SpringGreen3", command=self.text_progress)
        self.confirm_button.grid(row=5)

        self.score_label = Label(self.quiz_frame, text="Score: 0", font=("Tw Cen MT", "14", "bold"),
                                bg=background_color)
        self.score_label.grid(row=6)

    def questions_setup(self):
            randomiser()
            self.var1.set(0)
            self.question_label.config(text=question_answers[qnum][0])
            self.rb1.config(text=question_answers[qnum][1])
            self.rb2.config(text=question_answers[qnum][2])
            self.rb3.config(text=question_answers[qnum][3])
            self.rb4.config(text=question_answers[qnum][4])


    def text_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        
        if len(asked) >= len(question_answers):
            if choice == int(question_answers[qnum][5]):
                score += 1
                scr_label.configure(text="Score: " + str(score))
                self.confirm_button.config(text="Confirm")
            else:
                correct_answer = question_answers[qnum][5]
                correct_answer = question_answers[qnum][correct_answer]
                scr_label.configure(text="The correct answer was: " + str(correct_answer))
                self.confirm_button.config(text="Confirm")
        else:
            if choice == 0:
                self.confirm_button.config(text="Try again, You didn't select an option then submit again")
                choice = self.var1.get()
            else:
                if choice == int(question_answers[qnum][5]):
                    score += 1
                    scr_label.configure(text="Score: " + str(score))
                    self.confirm_button.config(text="Confirm")
                    self.questions_setup()
                else:
                    correct_answer = question_answers[qnum][5]
                    correct_answer = question_answers[qnum][correct_answer]
                    scr_label.configure(text="The correct answer was: " + str(correct_answer))
                    self.confirm_button.config(text="Confirm")
                    self.questions_setup()




        
        
        

        
        
        
    






if __name__ == "__main__":
    root = Tk()
    root.title('Python Quiz')
    quizStarter_object = QuizStarter(root)
    root.mainloop()
    