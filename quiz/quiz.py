# -*- encoding: "utf-8" -*-
import codecs
import random

class Question:
    
    result = ""
    count = 0
    finallist = []

#metoda do losowania listy z numerami pytań
    def drawingquestions (self, file, num):
        self.count = len(open(file, 'r').readlines())
        self.finallist = random.sample(list(range(1, self.count, 5)), num)
        return self.finallist
 
 #metoda do wypisywania pytania
    def getquestion(self, file, numb):
        text = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                text.append(line)
        char = ["","a","b","c"]
        n=0
        while(n < 4):
            print(char[n], text[numb-1])
            n += 1
            numb += 1
        self.result = text[numb-1].strip()          

class EasyQuestion (Question):
    file = "C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\easyquestions.txt"
    howmuch = 3

class MediumQuestion (Question):
    file = "C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\mediumquestions.txt"
    howmuch = 2

class DifficultQuestion (Question):
    file = "C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\difficultquestions.txt"
    howmuch = 1

class Player():

    def __init__(self, numberofquestion, points):
        self.numberofquestion = numberofquestion
        self.points = points

    answer = ""
    
    def podajimie(self):
        self.name = input("Podaj swoje imię ")
        print("Witaj w grze ", self.name, "! Przez Tobą 6 pytań.")
        print("Udzielaj odpowiedzi na pytania wprowadzając z klawiatury tylko nazwę podpunktu odpowiedzi.")
        print("Powodzenia!")

    def giveanswer(self):
        self.answer = input("Twoja odpowiedź: ")
        return self.answer

    def goodanswer(self):
        print("Masz rację!To dobra odpowiedź")
        self.points += 1
    
    def wronganswer(self):
        print("Niestety, to zła odpowiedź")
    
    def endgame(self):
        print(self.name, "to już koniec gry")
        print("Twoje punkty to ", self.points, " na 6")
        exit


#stworzenie zawodnika

player = Player(1, 0)
player.podajimie()

#losowanie pytan

easy = EasyQuestion.drawingquestions(Question, EasyQuestion.file, EasyQuestion.howmuch)
medium = MediumQuestion.drawingquestions(MediumQuestion, MediumQuestion.file, MediumQuestion.howmuch)
difficult = DifficultQuestion.drawingquestions(DifficultQuestion, DifficultQuestion.file, DifficultQuestion.howmuch)

#wypisywanie pytań

for player.numberofquestion in [1,2,3]:
    EasyQuestion.getquestion(Question, EasyQuestion.file, easy[0])
    player.giveanswer()
        
    if player.answer in EasyQuestion.result:
        player.goodanswer()
    else:
        player.wronganswer()

    del easy[0]

for player.numberofquestion in [4,5]:
    MediumQuestion.getquestion(MediumQuestion, MediumQuestion.file, medium[0]) 
    player.giveanswer()       
    if player.answer in MediumQuestion.result:
        player.goodanswer()
    else:
        player.wronganswer()
    del medium[0]

for player.numberofquestion in [6]:
    DifficultQuestion.getquestion(DifficultQuestion, DifficultQuestion.file, difficult[0])   
    player.giveanswer()   
    if player.answer in DifficultQuestion.result:
        player.goodanswer()
    else:
        player.wronganswer()
    del difficult[0]  

player.endgame()    