import tkinter
#MACC Scoreboard
#Version 1.5.1
#by William Brannock


# window setup()
window = tkinter.Tk()
window.title("MACC Scoreboard")
window.geometry('1080x720')

#global score variables
score_a = 0
score_b = 0

#functions
def home_correct():
	global score_a
	score_a = score_a + 5
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def away_correct():
	global score_b
	score_b = score_b + 5
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

def home_neg():
	global score_a
	score_a = score_a - 2
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def away_neg():
	global score_b
	score_b = score_b - 2
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

def reset_a():
	global score_a
	score_a = 0
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def reset_b():
	global score_b
	score_b = 0
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

#cycles through the subjects
subject_count = 0
def sub_cycle():
	subjects = ["Science", "Math", "All-Around", "English", "Social Studies"]
	global subject_count
	if (subject_count < 4):
		subject_count = subject_count + 1
	else:
		subject_count = 0
	subject_label.config(text = subjects[subject_count])
	subject_label.grid(row = 0, column = 0)
	

#subject lablel
subject_label = tkinter.Label(window, text = "Subject", font=("Helvetica", 50, 'italic'), anchor = "w")
subject_label.grid(row = 0, column = 0)
#subject button
sub_button = tkinter.Button(window, text = "Next Subject", command = sub_cycle).grid(row = 0, column = 1)

#scoreboard labels
tkinter.Label(window, text = "Home Score", font=("Helvetica", 50, 'bold')).grid(row = 1, column = 0)
tkinter.Label(window, text = "Away Score", font=("Helvetica", 50, 'bold')).grid(row = 1, column = 1)
tkinter.Label(window, text = "Made by William Brannock", font=("Helvetica", 20), anchor = "w", width = 40).grid(row = 8, column = 0)
tkinter.Label(window, text = "Available on Github at github.com/wbrannock", width = 40, anchor = "w", font=("Helvetica", 20, )).grid(row = 9, column = 0)

#Team A Score Display
display_a = tkinter.Label(window, text = str(score_a), font=("Helvetica", 125))
display_a.grid(row = 2, column = 0)
#Team B Score Display
display_b = tkinter.Label(window, text = str(score_b), font=("Helvetica", 125))
display_b.grid(row = 2, column = 1)



#score buttons
button1 = tkinter.Button(window, text = "+5 Team A", command = home_correct).grid(row = 3, column = 0)
button2 = tkinter.Button(window, text = "+5 Team B", command = away_correct).grid(row = 3, column = 1)
button3 = tkinter.Button(window, text = "-2 Team A", command = home_neg).grid(row = 4, column = 0)
button3 = tkinter.Button(window, text = "-2 Team B", command = away_neg).grid(row = 4, column = 1)

#redo buttons
redo_a = tkinter.Button(window, text = "Reset A", command = reset_a).grid(row = 5, column = 0)
redo_a = tkinter.Button(window, text = "Reset B", command = reset_b).grid(row = 5, column = 1)

#main loop to keep gui window open
window.mainloop()