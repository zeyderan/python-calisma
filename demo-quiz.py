class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')
        for q in question.choices:
            print('- '+q)

        answer = input('cevap : ')
        self.guess(answer)
    
    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1
        self.loadQuestion()
        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f'score : {self.score} puan')
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber <= totalQuestion:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))
        else:
            print('Quiz Bitti...'.center(100,'*'))

q1 = Question('en iyi programlama dili hangisidir ?', ['c#','python','js','java'],'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','js','java','c#'],'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['c#','python','java','js'],'python')


questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.loadQuestion()
