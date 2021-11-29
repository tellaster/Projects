class bcolors:
	GREEN = '\033[92m'
	CYAN = '\033[96m'
	ENDC = '\033[92m'

import time
import random

welcome = """*****************************************************************
*                                                               *
*  Welcome to the Chloroplast Protein Import Interactive Story  * 
*                                                               *
*****************************************************************"""

step1 = """
Today, we’re going to follow the journey of pSSU from translation to import into the stroma of the chloroplast. So, what is pSSU? It is a preprotein small subunit of the RuBisCo enzyme, which is responsible for fixing the carbon from carbon dioxide during the Calvin cycle. 
Ready to begin? Type in your answer and the press 'enter' or 'return': """

step2 = """
In the start of the journey in the cytoplasm, pSSU is in a complex with a cytosolic 80S ribosome, which translates mRNA into a polypeptide sequence. Before the entire mRNA sequence is translated, the unfolded preprotein forms a complex with a chaperone protein, Hsp70. The complex between pSSU and Hsp70 (and 14-3-3 proteins), because of the targeting sequence in the N-terminus of the preprotein, called the transit peptide. Hsp70 recognizes pSSU, because the targeting sequence, also called the transit peptide, is rich with serine and threonine, poor in tyrosine, and has an overall positive charge.
Where is the Hsp70 complex creation happening? Type in your answer: """

step3 = """ 
The job of Hsp70 as a chaperone protein is to ferry, with energy from ATP, the pSSU to the outer membrane of the chloroplast, while preventing it from folding. The pSSU shouldn’t be folded yet, because it would be too big for import into the chloroplast. The Hsp70 complex guides the pSSU to Toc34 on the outer membrane of the chloroplast. Toc34 is a membrane of a family of Toc receptor proteins. Toc stands for translocon on the outer chloroplast membrane. The Hsp70 complex needs to align with Toc34.
Guess the number that Toc34 is “thinking” of to make sure you’re on the same page (1-10): """

step4 = """
Luckily, there are up to 30,000 import sites on the outer membrane of the chloroplast, so it doesn’t take too many tries to align to at least one of the Toc receptors! In addition, energy is needed to initiate the import process. Generally, usable energy in the cell comes in two forms: ATP and GTP. Which one gets used for protein import into the chloroplast?
"""

step5 = """
Scientists have shown that both molecules, ATP and GTP, play a role in the import of proteins into the chloroplast. ATP is used by Hsp70 to do its job as chaperone, and both ATP and GTP are utilized by the Toc proteins.
What do the numbers after “Toc” mean? Since several different groups were researching chloroplast import proteins at the same time, they were give them different name, but these scientists needed uniform names so that the research could build on each other. As a result, each outer membrane protein was given a name of “Toc” + their molecular weight (in kDa). The components that make up a unit of an outer envelope translocon group are: Toc75, Toc34 (GTP user), Toc159 (GTP user), and Toc64. Since the pSSU is already docked with Toc34, it now needs to get into the intermembrane space of the chloroplast, which is between the outer and inner membranes. The Toc complex has a group  of beta sheets that form a passage through the outermsmbrane, which allows the precursor protein through. Since the pSSU is unfolded at this point and the passage formed by the Toc complex is pretty small, what is the most space efficient way to get it through the outer membrane of the chloroplast? 
A. As a messy clump, just force it through!
B. Like a strand of spaghetti, a single file line for the polypeptide chain
"""

step6 = """
The time that pSSU spends in the intermembrane space us relatively short. This is because the Toc complex is cross linked with another class of proteins in the inner membrane of the chloroplast. What would be the abbreviation for the proteins in this complex? 
"""

step7 = """
In the intermembrane space, Tic22 floats and is thought to serve as a chaperone from the Toc complex to the Tic complex. Some research indicates that Tic22 may assist in faster import rates, perhaps expediting the preprotein. While exact composition of the Tic complex remains undetermined, it is thought that the following proteins play a part in transporting the preprotein pSSU into the stroma: Tic20, Tic21, Tic32, Tic40, Tic55, Tic56, Tic62, Tic100, Tic110, and Tic214. The Tic complex is driven by ATP, but the exact components that utilizes ATP are not yet confirmed. Should scientists do more research into this?
"""

step8 = """
Once the pSSU is through the Tic complex, the pSSU has finally made it to the stroma, its intended destination. Here, stromal Hsp70 assists the pSSU until the transit peptide is cleaved by stroll peptidase. Finally, pSSU is ready to fold into a complete protein and becomes the mature SSU! It is ready to form a complex called L8S8 holo-complex or RuBisCo with the late subunit (LSU).
Type “sources” for sources or “exit” to close the program.
"""

sources = """
Bölter, B., & Soll, J. (2016). Once upon a time – chloroplast protein import research from infancy to future challenges. Molecular Plant, 9(6), 798–812. https://doi.org/10.1016/j.molp.2016.04.014 
Nakai, M. (2015). The Tic Complex Uncovered: The alternative view on the molecular mechanism of protein translocation across the inner envelope membrane of chloroplasts. Biochimica Et Biophysica Acta (BBA) - Bioenergetics, 1847(9), 957–967. https://doi.org/10.1016/j.bbabio.2015.02.011 
"""

def step1func(answer):
	modanswer = answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	affirmative = ['yes', 'yeah', 'sure']
	negative = ['no', 'nope', 'exit']
	if modanswer in affirmative:
		response = True
		return response
	elif modanswer in negative:
		response = False
		return response
	else:
		print(bcolors.GREEN + "Uh oh, can you change your answer to be a yes or no? I don't understand what you're saying: ")
		newanswer = input(bcolors.CYAN)
		step1func(newanswer)

def step2func(answer):
	modanswer = answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	correct = ['cytosol', 'cytoplasm']
	if modanswer in correct:
		print(bcolors.GREEN + "Correct!")
		time.sleep(1)
	else:
		print(bcolors.GREEN + "Try again, that's not correct. Hint: Where are proteins translated from mRNA?")
		newanswer = input(bcolors.CYAN)
		step2func(newanswer)

def checkint():
	try:
		modanswer = int(input(bcolors.CYAN))
		return modanswer
	except:
		print(bcolors.GREEN + "Please enter an integer from 1 to 10: ")
		return checkint()

def enter1to10():
	modanswer = checkint()
	numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	if modanswer in numlist:
		return modanswer
	else:
		print(bcolors.GREEN + "Please enter an integer from 1 to 10: ")
		return enter1to10()

def step3func():
	step3answer = enter1to10()
	step3listtried = []
	step3listtried.append(step3answer)
	correctint = random.randint(1,10)
	while correctint != step3answer:
		print(bcolors.GREEN + "Huh, not quite.")
		print(bcolors.GREEN + "Here's what you've tried so far: " + str(step3listtried))
		print(bcolors.GREEN + "Try again: ")
		step3answer = enter1to10()
		step3listtried.append(step3answer)
	print(bcolors.GREEN + "Yay! You got it!")

def step4func():
	step4answer = input(bcolors.CYAN)
	modanswer = step4answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	correct = ['atp and gtp', 'both', 'both atp and gtp', 'atp & gtp']
	if modanswer in correct:
		print(bcolors.GREEN + "Correct!")
		time.sleep(1)
	else:
		print(bcolors.GREEN + "Try again. Hint: This is a trick question. There are multiple sources of energy.")
		step4func()

def step5func():
	step5answer = input(bcolors.CYAN)
	modanswer = step5answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	correct = ['b', 'b only']
	if modanswer in correct:
		print(bcolors.GREEN + "Correct!")
		time.sleep(1)
	else:
		print(bcolors.GREEN + "Try the other option!")
		step5func()

def step6func():
	step6answer = input(bcolors.CYAN)
	modanswer = step6answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	correct = ['tic']
	if modanswer in correct:
		print(bcolors.GREEN + "Correct!")
		time.sleep(1)
	else:
		print(bcolors.GREEN + "Try again. Hint: Look at the abbreviation for the outer membrane import complex proteins! ")
		step6func()

def step7func():
	step7answer = input(bcolors.CYAN)
	modanswer = step7answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	if modanswer == 'yes':
		print(bcolors.GREEN + "I agree! Let's move on to the last step!")
		time.sleep(1)
	elif modanswer == 'no':
		print(bcolors.GREEN + "I don't agree, but let's move on!")
		time.sleep(1)
	else:
		print(bcolors.GREEN + "Hmmm, I'm not sure what you answered, but we'll move on.")
		time.sleep(1)


def sourceorexit():
	step8answer = input(bcolors.CYAN)
	modanswer = step8answer.lower()
	modanswer = modanswer.replace(" ","")
	modanswer = modanswer.replace(".","")
	if modanswer == 'sources':
		print(bcolors.GREEN + sources)
		time.sleep(1)
		print(bcolors.GREEN + "Type anything to close the program.")
		sourceorexit()
	else:
		print(bcolors.GREEN + "Bye!")
		time.sleep(1)
		exit()


def main():
	print(bcolors.GREEN + welcome)
	print(bcolors.GREEN + step1)
	step1answer = input(bcolors.CYAN)
	if step1func(step1answer) == True:
		print(bcolors.GREEN + "Woohoo!")
	else:
		print(bcolors.GREEN + "Ah darn. We'll shut down the program. Thank you for trying!")
		time.sleep(3)
		quit()
	print(bcolors.GREEN + step2)
	step2answer = input(bcolors.CYAN)
	step2func(step2answer)
	print(bcolors.GREEN + step3)
	step3func()
	print(bcolors.GREEN + step4)
	step4func()
	print(bcolors.GREEN + step5)
	step5func()
	print(bcolors.GREEN + step6)
	step6func()
	print(bcolors.GREEN + step7)
	step7func()
	print(bcolors.GREEN + step8)
	sourceorexit()


main()
