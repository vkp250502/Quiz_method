# -*- coding: utf-8 -*-
"""quiz-system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wbGecxZVRk4Qe4Y8KhiojJEkQtFJ4x2_

# Quiz-System
"""

import random

"""# Step 1: Define the Question_data Class
We'll start by creating a Question class that represents a single question. Each question will have a question text, options (for multiple choice questions), and the correct answer.
"""

class Question_data:
    def __init__(self,sentence,options,answer):
        self.sentence = sentence
        self.options = options
        self.answer = answer

"""# Step 2: Create the Quiz Class
Next, we'll create a Quiz class that represents the entire quiz. This class will contain a list of Question objects and methods to add questions, generate a quiz, and evaluate the answers.
"""

# create quiz calss
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0


    def run_quiz(self):
        random.shuffle(self.questions)
        for i,question in enumerate(self.questions,1):
            print(f"Question {i}: {question.sentence}")
            random.shuffle(question.options)
            for j,option in enumerate(question.options,1):
                print(f"{j}. {option}")

            user_answer = input("Your answer (enter the number):\n ")
            #for multiple choice and true false questions
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question.options):
                user_answer = int(user_answer)
                if question.options[user_answer - 1] == question.answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"your answer is wrong correct answer is: {question.answer}\n")
            # for fill iin the blank questions
            elif user_answer.isdigit():
                if user_answer == question.answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"your answer is wrong correct answer is: {question.answer}\n")
            #for short answer type question
            elif type(user_answer) ==str:
                if str(user_answer).title() == question.answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"your answer is wrong correct answer is: {question.answer}\n")

            else:
                print("Invalid input. Please enter a valid option number.\n")

        print("Quiz over")
    def score_card(self):
        print(f"Your score is {self.score}/{len(self.questions)}")

"""# Adding some sample questions"""

#Multiple Choice Questions
question1 = Question_data("What is the capital of India",['Delhi','Lucknow','Agra','Mumbai'],"Delhi")
question2 =  Question_data("Which of the following is a non metal that remains liquid at room temperature?",['Phosphorous','Bromine','Chlorine','Helium'],"Bromine")
question3 =  Question_data("Chlorophyll is a naturally occurring chelate compound in which central metal is",['copper','magnesium','iron','calcium'],"magnesium")
question4 =  Question_data("Which of the following is used in pencils?",['Graphite','Silicon','Charcoal','Phosphorous'],"Graphit")
question5 =  Question_data("Which of the following metals forms an amalgam with other metals?",['Tin','Mercury','Lead','Zinc'],"Mercury")

# Fill in the Blanks
question6 =  Question_data("What is 10 x 34? = ", [], "340")
question7 =  Question_data("What is 10 /4? = ", [], "2.5")
question8 =  Question_data("Write one thousand five hundred three in number",[],"1503")
question9 =  Question_data("How many days in a weak",[],"7")
question10 =  Question_data("How many minutes in a hour",[],"60")

#True or False Type question
question11 =  Question_data("Sharks are mammals",[True,False],False)
question12 =  Question_data("Water is liquid ",[True,False],True)

#short answer type question
question13 =  Question_data("Who is the present 15 president of India?",[],"Droupadi Murmu")
question14 =  Question_data("What is the Capital of Utter Predesh",[],"Lucknow")

# define object of Quiz class
quiz= Quiz([question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14])

quiz.run_quiz()
quiz.score_card()

