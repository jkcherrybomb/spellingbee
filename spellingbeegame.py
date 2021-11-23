import tkinter
import random

plik=open('slowa.txt')
dictionary=plik.readlines()
plik.close()

window = tkinter.Tk()
window.title("Spelling Bee")
window.columnconfigure(1, weight=3)

x = len(dictionary)
#global keepscore

for i in range(x):
	dictionary[i]=str(dictionary[i])
	dictionary[i]=dictionary[i][:-1:]

def randletters():
	letters = random.sample(range(97, 121), 7)
	letters = set(map(chr, letters))
	while (len(letters) > 7): 
		letters.pop()
	while (len(letters) < 7): 
		letters.add(char(random.randint(97, 121)))
	global letters2
	letters2 = list(letters)
	
	displayset = tkinter.Label(window, text = "Your set of letters is:").grid(row = 0, column = 0)
	currentletters = tkinter.Label(window, text = letters2).grid(row = 0, column = 1)
	global keepscore
	keepscore = 0
	displayscore = tkinter.Label(window, text = "Your score is:").grid(row = 0, column = 2)
	currentscore = tkinter.Label(window, text = keepscore).grid(row = 0, column = 3)
	letters.clear()
	
def check():
	word = str(inputword.get())
	if len(word) < 4:
		printing = tkinter.Label(window, text = "that's too short").grid(row = 2, column = 0)
		return 
	for i in word:
		if i not in letters2:
			printing = tkinter.Label(window, text ="You've used a letter outside the set").grid(row = 2, column = 0)
			return 
	if word in dictionary:
		printing = tkinter.Label(window, text = "Congrats! you're right!").grid(row = 2, column = 0)
		global keepscore
		keepscore += len(word)
		displayscore = tkinter.Label(window, text = "Your score is:").grid(row = 0, column = 2)
		currentscore = tkinter.Label(window, text = keepscore).grid(row = 0, column = 3)
	else:
		printing = tkinter.Label(window, text = "Sorry! Try again!").grid(row = 2, column = 0)
	
	

displayreset = tkinter.Button(window, text = "Give me a new set of letters", fg = "purple", command = randletters).grid(row = 2, column = 2)

tkinter.Label(window, text = "enter your word").grid(row = 1, column = 0)
inputword = tkinter.Entry(window)
inputword.grid(row = 1, column = 1)

checkbutton = tkinter.Button(window, text = "submit", fg = "purple", command = check).grid(row = 2, column = 3)




window.mainloop()

