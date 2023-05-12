from tkinter import *
from tkinter import messagebox
import random
root = Tk()
frame = Frame(root)
frame.pack(expand = True)
root.geometry('650x650')
root.title('Tic tac toe ')


play_area = []
comp_area = []
single_player = False
x_score = 0
o_score = 0
games = 0

label = Label(frame, text = "X goes first\n\nScores:\nX = " + str(x_score) + "\nO = " + str(o_score), font = ("arial black", 10, "bold"))
label.grid(row = 0, column = 0, columnspan = 1, pady = 20)

def comp_move():
	global comp_area
	#print(len(play_area))
	comp_area.clear()
	while single_player == True:
		buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
		for button in buttons:
			if button.cget("text") == " ":
				comp_area.append(button)
		#print(comp_area)
		#print(x)
		try:
			if len(play_area) % 2 != 0:
				random.choice(comp_area).configure(text = 'O')
				play_area.append("button1")
				
				
			elif len(play_area) % 2 == 0:
				random.choice(comp_area).configure(text = 'X')
				play_area.append("button1")
		except:
			pass
		break	
		

def change_mode():
	global single_player
	x_score = 0
	o_score = 0
	label.configure(text = "X goes first\n\nScores:\nX = " + str(x_score) + "\nO = " + str(o_score))
	buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
	if single_player == False:
		single_player = True
		mode.configure(text = "Single Player")
		for button in buttons:
			button.configure(text = ' ')
			play_area.clear()
	elif single_player == True:
		single_player = False
		mode.configure(text = "Single Player")
		mode.configure(text = "Two Players")
		for button in buttons:
			button.configure(text = ' ')
			play_area.clear()

def button1_play():
	print(len(play_area))
	if button1.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button1.configure(text = 'O')
			play_area.append("button1")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button1.configure(text = 'X')
			play_area.append("button1")
			comp_move()
			win()
			board_full()
			


def button2_play():
	print(len(play_area))
	if button2.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button2.configure(text = 'O')
			play_area.append("button2")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button2.configure(text = 'X')
			play_area.append("button2")
			comp_move()
			win()
			board_full()
			


def button3_play():
	print(len(play_area))
	if button3.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button3.configure(text = 'O')
			play_area.append("button3")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button3.configure(text = 'X')
			play_area.append("button3")
			comp_move()
			win()
			board_full()
			

def button4_play():
	print(len(play_area))
	if button4.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button4.configure(text = 'O')
			play_area.append("button4")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button4.configure(text = 'X')
			play_area.append("button4")
			comp_move()
			win()
			board_full()
			

def button5_play():
	print(len(play_area))
	if button5.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button5.configure(text = 'O')
			play_area.append("button5")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button5.configure(text = 'X')
			play_area.append("button5")
			comp_move()
			win()
			board_full()
			

def button6_play():
	print(len(play_area))
	if button6.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button6.configure(text = 'O')
			play_area.append("button6")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button6.configure(text = 'X')
			play_area.append("button6")
			comp_move()
			win()
			board_full()
			

def button7_play():
	print(len(play_area))
	if button7.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button7.configure(text = 'O')
			play_area.append("button7")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button7.configure(text = 'X')
			play_area.append("button7")
			comp_move()
			win()
			board_full()
			

def button8_play():
	print(len(play_area))
	if button8.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button8.configure(text = 'O')
			play_area.append("button8")
			comp_move()
			win()
			board_full()
			
			
		elif len(play_area) % 2 == 0:
			button8.configure(text = 'X')
			play_area.append("button8")
			comp_move()
			win()
			board_full()
			

def button9_play():
	print(len(play_area))
	if button9.cget("text") == ' ':
		if len(play_area) % 2 != 0:
			button9.configure(text = 'O')
			play_area.append("button9")
			comp_move()
			win()
			board_full()
			
			
			
		elif len(play_area) % 2 == 0:
			button9.configure(text = 'X')
			play_area.append("button9")
			comp_move()
			win()
			board_full()
			

def win():
	global o_score
	global x_score
	global games
	if button1.cget("text") == "X" and button2.cget("text") == "X" and button3.cget("text") == "X" or button4.cget("text") == "X" and button5.cget("text") == "X" and button6.cget("text") == "X" or button7.cget("text") == "X" and button8.cget("text") == "X" and button9.cget("text") == "X" or button1.cget("text") == "X" and button4.cget("text") == "X" and button7.cget("text") == "X" or button2.cget("text") == "X" and button5.cget("text") == "X" and button8.cget("text") == "X" or button3.cget("text") == "X" and button6.cget("text") == "X" and button9.cget("text") == "X" or button1.cget("text") == "X" and button5.cget("text") == "X" and button9.cget("text") == "X" or button3.cget("text") == "X" and button5.cget("text") == "X" and button7.cget("text") == "X":
		x_score += 1
		#print(x_score)
		label.configure(text = "X goes first\n\nScores:\nX = " + str(x_score) + "\nO = " + str(o_score))
		messagebox.showinfo("Info", "X wins")
		buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
		for button in buttons:
			button.configure(text = ' ')
			play_area.clear()
		games += 1
		if games % 2 != 0:
			play_area.append(button1)
			comp_move()
			

	elif button1.cget("text") == "O" and button2.cget("text") == "O" and button3.cget("text") == "O" or button4.cget("text") == "O" and button5.cget("text") == "O" and button6.cget("text") == "O" or button7.cget("text") == "O" and button8.cget("text") == "O" and button9.cget("text") == "O" or button1.cget("text") == "O" and button4.cget("text") == "O" and button7.cget("text") == "O" or button2.cget("text") == "O" and button5.cget("text") == "O" and button8.cget("text") == "O" or button3.cget("text") == "O" and button6.cget("text") == "O" and button9.cget("text") == "O" or button1.cget("text") == "O" and button5.cget("text") == "O" and button9.cget("text") == "O" or button3.cget("text") == "O" and button5.cget("text") == "O" and button7.cget("text") == "O":
		o_score += 1
		label.configure(text = "X goes first\n\nScores:\nX = " + str(x_score) + "\nO = " + str(o_score))
		messagebox.showinfo("Info", "O wins")
		buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
		for button in buttons:
			button.configure(text = ' ')
			play_area.clear()
		games += 1
		if games % 2 != 0:
			play_area.append(button1)
			comp_move()
			
			


def draw():
	pass
	

def restart():
	buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
	for button in buttons:
		button.configure(text = ' ')
		play_area.clear()

def board_full():
	global games
	plays = [button1.cget("text"), button2.cget("text"), button3.cget("text"), button4.cget("text"), button5.cget("text"), button6.cget("text"), button7.cget("text"), button8.cget("text"), button9.cget("text")]
	if plays.count("X") == 5 and plays.count("O") == 4 or plays.count("O") == 5 and plays.count("X") == 4:
		messagebox.showinfo("Info", "Draw")
		buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
		for button in buttons:
			button.configure(text = ' ')
			play_area.clear()
		games += 1
		if games % 2 != 0:
			play_area.append(button1)
			comp_move()
			


button1 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button1_play)
button2 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button2_play)
button3 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button3_play)
button4 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button4_play)
button5 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button5_play)
button6 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button6_play)
button7 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button7_play)
button8 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button8_play)
button9 = Button(frame, text = ' ', width = 5, height = 2, font = ("arial black", 30, "bold"), command = button9_play)
restart = Button(frame, text = "Restart", font = ("arial black", 10, "bold"), command = restart)
mode = Button(frame, text = "Two Players", font = ("arial black", 10, "bold"), command = change_mode)
	
button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
restart.grid(row = 0, column = 2)
mode.grid(row = 0, column = 1)

root.mainloop()
