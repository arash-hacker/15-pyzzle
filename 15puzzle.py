#!/usr/bin/python3

import random
import sys
import readchar

class Puzzle:

    def __init__(self):
        self.emoji=['**','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
        self.board=list(range(16))
        self.input=""
        self.counter=0
        self._randomize()
        pass

    def _randomize(self):
        random.shuffle(self.board)
        newboard=[]
        minboard=[]
        for i in range(4):
            for j in range(4):
                minboard.append(self.board[4*i+j])
            newboard.append(minboard)
            minboard=[]
        self.board=newboard


    def get_input(self):
        self.counter+=1
        print("------"+str(self.counter)+"-------")
        self.input=readchar.readchar()

    def react(self):
        row_x= [(index) for (index,item) in enumerate(self.board) if 0 in item][0]
        transpose=[list(x) for x in zip(*self.board)]
        col_x= [(index) for (index,item) in enumerate(transpose) if 0 in item][0]
        
        if self.input=='4':
            row_x_0=[i for i,j in enumerate(self.board[row_x]) if j==0][0]
            if row_x_0 != 0:
                self.board[row_x].remove(0)
                self.board[row_x].insert(row_x_0-1,0)

        elif self.input=='6':
            row_x_0=[i for i,j in enumerate(self.board[row_x]) if j==0][0]
            if row_x_0 != 3:
                self.board[row_x].remove(0)
                self.board[row_x].insert(row_x_0+1,0)

        elif self.input=='8':
            col_x_0=[i for i,j in enumerate(transpose[col_x]) if j==0][0]
            if col_x_0 != 0:
                transpose[col_x].remove(0)
                transpose[col_x].insert(col_x_0-1,0)
            self.board=[list(x) for x in zip(*transpose)]

        elif self.input=='2':
            col_x_0=[i for i,j in enumerate(transpose[col_x]) if j==0][0]
            if col_x_0 != 3:
                transpose[col_x].remove(0)
                transpose[col_x].insert(col_x_0+1,0)
            self.board=[list(x) for x in zip(*transpose)]
    
    def draw(self):
        for row in self.board:
            for j in range(4):
                print(' '+ self.emoji[ row[j] ] ,end='')
            print("\n")

    def end(self):
        print("The End.")
    
    def emoji(self,index):
        print(' '+self.emoji[index])

    def can_exit(self):
        return (False if self.input =="q" else True)

if __name__=="__main__":
    p=Puzzle()
    print('Press any key 2468q')
    while p.can_exit():
        p.get_input()
        p.react()
        p.draw()
    p.end()
