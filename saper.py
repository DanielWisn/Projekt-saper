import os
import time
import random
import keyboard
from typing import Literal

class Saper:

    def __init__(self, n: int) -> None:
        self.N = n
        self.direction: Literal["up", "down", "left", "right","stay"] = "right"
        self.saperX = 1
        self.saperY = 1
        self.startTime = time.time()
        self.check_lose = False
        self.is_first_move = True

    def set_direction(self, dir):
        self.direction = dir

    def generate_board(self):
        table = []

        table.append(["*"] * self.N)

        for _ in range(self.N - 2):
            table.append(["*"] + ["."] * (self.N - 2) + ["*"])

        table.append(["*"] * self.N)

        self.table = table 

        return table

    def clear_trace(self):

        self.table[self.saperY][self.saperX] = "#"

        if self.table[self.saperY][self.saperX] == "#":
            self.table[self.saperY][self.saperX] = "."
        elif self.table[self.saperY][self.saperX] == "+":
            pass


    def generate_true_board(self):
        true_table = []

        true_table.append(["*"] * self.N)
        
        for _ in range(self.N - 2):
            true_table.append(["*"] + ["."] * (self.N - 2) + ["*"])
                

        true_table.append(["*"] * self.N)

        self.true_table = true_table

        return true_table

    def generate_numbers(self):
        for y in range(len(self.true_table)):
            for x in range(len(self.true_table[y])):
                if self.true_table[x][y] == ".":
                    number_mines = 0
                    if self.true_table[x+1][y+1] == "x":
                        number_mines += 1
                    if self.true_table[x-1][y-1] == "x":
                        number_mines += 1
                    if self.true_table[x+1][y] == "x":
                        number_mines += 1
                    if self.true_table[x-1][y] == "x":
                        number_mines += 1
                    if self.true_table[x][y+1] == "x":
                        number_mines += 1
                    if self.true_table[x][y-1] == "x":
                        number_mines += 1
                    if self.true_table[x-1][y+1] == "x":
                        number_mines += 1
                    if self.true_table[x+1][y-1] == "x":
                        number_mines += 1
                    self.true_table[x][y] = f"{number_mines}"


    def move_saper(self):
        match self.direction:
            case "left":
                if self.saperX == 1:
                    self.saperX = 1
                else:
                    self.saperX -= 1
            case "right":
                if self.saperX == self.N - 2:
                    self.saperX = self.N -2
                else:
                    self.saperX += 1

            case "up":
                if self.saperY == 1:
                    self.saperY = 1
                else:
                    self.saperY -= 1
                
            case "down":
                if self.saperY == self.N - 2:
                    self.saperY = self.N -2
                else:
                    self.saperY += 1
            case "stay":
                self.saperY = self.saperY
                self.saperX = self.saperX
    def set_flag(self): 
        self.table[self.saperY][self.saperX] = "+"

    def first_move(self,positionX,positionY):
            neighbours = [
                (positionX+1,positionY+1),
                (positionX-1,positionY-1),
                (positionX+1,positionY),
                (positionX-1,positionY),
                (positionX,positionY+1),
                (positionX,positionY-1),
                (positionX-1,positionY+1),
                (positionX+1,positionY-1)]
            if int(self.true_table[positionX][positionY]) > 0:
                self.table[positionX][positionY] = self.true_table[positionX][positionY]
            else:
                self.table[positionX][positionY] = " "
                for i in neighbours:
                    # print(positionX,positionY)
                    # print(neighbours)
                    # print(i)
                    self.first_move(i[0],i[1])
            self.is_first_move = False
    def check(self):
        if self.is_first_move == True:
            self.first_move(self.saperY,self.saperX)
        elif self.is_first_move == False:
            check_lose = False
            if self.true_table[self.saperY][self.saperX] == "x":
                check_lose = True
            else:
                check_lose = False
                self.table[self.saperY][self.saperX] = self.true_table[self.saperY][self.saperX]
        
            self.check_lose = check_lose

            return check_lose

    def generate_mines(self,number):
        for i in range(number):
            x = random.randint(1, self.N - 2)
            y = random.randint(1, self.N - 2)

            self.true_table[x][y] = "x"

    def print_board(self):
        self.table[self.saperY][self.saperX] = "#"
        print(f'Time: {int(time.time()-self.startTime)}')
        for line in self.table:
            print(" ".join(line))

    def print_true_board(self):
        for line in self.true_table:
            print(" ".join(line))

s = Saper(25) 
keyboard.on_press_key("left", lambda x: s.set_direction("left"))
keyboard.on_press_key("up", lambda x: s.set_direction("up"))
keyboard.on_press_key("down", lambda x: s.set_direction("down"))
keyboard.on_press_key("right", lambda x: s.set_direction("right"))
keyboard.on_press_key("space", lambda x: s.set_flag())
keyboard.on_press_key("c", lambda x: s.check())

s.generate_true_board()
s.generate_mines(40)
s.generate_numbers()
s.generate_board()
while True:
    if s.check_lose == True:
        print("Lose")
        break
    if s.direction != "stay":
        s.move_saper()
        os.system("cls") 
        s.print_board()
        #s.print_true_board()
        s.clear_trace()
        s.direction = "stay"
        time.sleep(1)
    

# import random
# import json

# points = random.randrange(0, 1_000_000_000, 1000)

# print(points)

# name = input("Enter your name")

# try:
#     with open("score.txt") as fp:
#         napis = fp.read()

#         najlepsze_wyniki = json.loads(napis)
# except:
#     najlepsze_wyniki = []


# najlepsze_wyniki.append({"name":name,"points":points})

# with open("score.json",'w') as fp:

#     najlepsze_wyniki = json.dumps(najlepsze_wyniki)
#     fp.write(najlepsze_wyniki)





