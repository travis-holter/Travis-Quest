from sys import exit
import random


def death(reason):
	'''Exits the program when the character dies, gives the reason for death'''
	print ("You died: ", reason)
	exit(0)


def first_room():
	'''Explains the game and moves the player on to the gift room '''
	print (" ")
	print ("\033[0;32mWelcome to Travis Quest!\033[0m")
	print ("""
	In this game you are presented with numbered choices,
	to play just type in the number that corresponds to your choice, and press enter.
	Come on, just type in the number, you can do it! Let's try:
	""")
	print ("\033[00;31mWhat will you do next?\033[0m")
	print ("1. Continue the game")
	print ("2. Give up and die")
	choice = input("> ")
	if choice == "1":
		gift_room()
	elif choice == "2":
		death("Way to give up, loser!")	
	else:
		print ("I don't understand! Type in 1 or 2, that's it!")
		print ("Let's start over and try again....")
		first_room()


def gift_room():
	'''Let's the player choose a gift before the dungeon rooms start '''
	global gift
	global str
	global dex
	global con
	print ("\033[0;32mNICE! You figured it out!\033[m")
	print ("""
	In this game you will go on a perilous journey through five rooms. At the end of the
	five rooms is the game's boss, Travis the Terrible! You muse defeat him to win. To
	help you on your journey, you get a gift! Choose wisely:
	""")
	print ("\033[00;31mIt's dangerous to go alone, take this!\033[0m")
	print ("1. Take the \'Big Sword\' - Helps you kill monsters")
	print ("3. Take the \'Telepathic Implant\' - Read minds and adds drama")
	print ("2. Take the \'Steroids\' - Gives good Strength and Dexterity!")
	print ("4. Take the \'History Book\' - Gives you historic information. NERD!")
	print ("5. Take the \'Calculator\' - Let's you see the percentage chance of success")
	print ("6. Take the \'Sexy Wig\' - Has the sensual power of seduction")
	choice = input("> ")
	if choice == "1":
		gift = gifts[0]
		print ("\033[0;32mNice Sword! Let's go kill everything!\033[0m")
	elif choice == "2":
		gift = gifts[1]
		str += 1
		dex += 1
		print ("\033[0;32mBro, you are looking jacked!\033[0m")
	elif choice == "3":
		gift = gifts[2]
		print ("\033[0;32mOW! That surgery hurt, now you hear voices.\033[0m")
	elif choice == "4":
		gift = gifts[3]
		print ("\033[0;32mYou are such a nerd. Have fun reading, NERD!\033[0m")
	elif choice == "5":
		gift = gifts[4]
		print ("\033[0;32mA wise choice, let's crunch some numbers!\033[0m")
	elif choice == "6":
		gift = gifts[5]
		print ("\033[0;32mNice choice - wait, you actually took the wig!?\033[0m")
		print ("\033[0;32mYou know that was just a joke, right? *SIGH*\033[0m")
	else:
		death("You are too dumb to type a number.")
	print ("\033[0;31mHit ENTER to go to the next room.\033[0m")
	input("> ")


def rock_room():
	'''The player encounters fallen rocks'''
	print ("\033[0;32mIt's a room filled with rocks!\033[0m")
	print ("A large boulder blocks your path. You wonder what to do:")
	if gift == "History Book":
		print ("""
		You open your history book:
		\033[0;36mMany of the rocks in this room were formed by lava flows that were 
		created by ancient pissed off dragons. Ancient dragons loved to breathe fire
		on things until they melted. The dragon fire has made these rocks unusually 
		dense. The average weight of one of the boulders is eleventy billions tons. 
		Climbing rocks is always risky, but only an idiot would try to dig under them.
		""")
	print ("\033[0;31mWhat will you do next?\033[0m")
	print ("1. Climb over the rocks")
	if gift == "Calculator":
		print ("\033[0;36m75% chance of success\033[0m")
	print ("2. Dig under the rocks")
	if gift == "Calculator":
		print ("\033[0;36m25% chance of success\033[0m")
	if str > 0:
		print ("\033[0;36m3. (Good Strength) Lift the rocks out of the way!\033[0m")
		if gift == "Calculator":
			print ("\033[0;36m100% chance of success\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1" and fate == 1:
		death("Your foot slips, you fall and break every bone in your body!")
	elif choice == "1" and fate > 1:
		print ("You climb over the rocks easily, you are good at this!")
	elif choice == "2" and fate < 4:
		death("As you dig under the rock, it breaks loose and crushes you. That was dumb.")
	elif choice == "2" and fate == 4:
		print ("You tunnel all the way without getting crushed. You have a feeling that")
		print ("You are very lucky to have gotten away with that!")
	elif choice == "3" and str > 0:
		print ("You lift the boulder above your head and set it down in the corner. You")
		print ("are strong AF!")
	else:
		death("You are too dumb to type a number.")
	print ("\033[0;31mHit ENTER to go to the next room!\033[0m")
	input("> ")


def math_test_room():
	'''The player encounters a math test'''
	global gift
	global int
	print ("\033[0;32mIt's a room full of students taking a math test!\033[0m")
	
	print ("""
	\"You\'re late!'\" says an Orcish math teacher. He shoves you over to an empty desk
	and you take a seat. There is a very difficult math test in front of you.
	""")
	if gift == "History Book":
		print("""
		\033[0;36mYou find a biography page for the Orcish math teacher. His is named
		\'Grumsh the cheater-hater\', and he is known for ripping the spines from
		students that are caught cheating.\033[0m
		""")
	print ("\033[0;31mWhat will you do next?\033[0m")
	print ("1. Just try your best and hope you can remember how to factor trinomials")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success\033[0m")
	print ("2. Cheat!")
	if gift == "Calculator":
		print ("\033[0;36m25% chance of success\033[0m")
	if gift == "Calculator":
		print ("\033[0;36m3. (Calculator) Use the calculator for the test!")
		print ("100% chance of success AND increase your Intellegince!\033[0m")
	if gift == "Sexy Wig":
		print ("\033[0;36m3. (Sexy Wig) Seduce the math teacher\033[0m")
	if gift == "Big Sword":
		print ("\033[0;36m3. (Big Sword) Kill the math teacher!\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1":
		print("""
		You have no idea what you are doing and you utterly fail at the test. The Orcish
		teacher looks at your paper and slowly shakes his head. \"You suck at math. Now
		get out of here!\" For some reason you thought he would kill you if you failed.
		""")
	elif choice == "2" and fate < 4:
		print ("The orc catches you. He yells \"DELICIOUS SPINAL FLUID!\"")
		death("The teacher catches you cheating and rips your spine out!")
	elif choice == "2" and fate == 4:
		print("""
		You cheat through the whole test and somehow get away with it. Do you feel proud
		of yourself? CHEATER?!
		""")
	elif choice == "3" and gift == "Calculator":
		int += 1
		print("""
		You combine hard work and the right tools nd ace the test! Nice job, you feel
		proud and smarter.
		""")
		print ("\033[0;32mYour intelligence increased!\033[0m")
	elif choice == "3" and gift == "Sexy Wig":
		print("""
		You put on the wig and gaze deep into the orcs eyes. He comes over and introduces
		himself as \'Grumsh the cheater-hater\'. You strike up a conversation and before
		you know it three hours have passed. You are surprised the discover that you have
		so much in common. He invites you to dinner and you agree. It is a lovely evening
		and he leans in and gives you a kiss. His tusks brush softly across your lips and
		you invite him back to your place.
		Over the next few weeks you fall passionately in love. About two years later you
		are married and have your first child (somehow). Then one day, there is a sudden
		tear in the fabric of spacetime. An evil shadow monster made of tentacles emerge
		and devours your family. Grumsh shouts \'Save yourself my love!\' He is torn into 
		a million pieces. With tears in your eyes, you jump into the time vortex and
		travel back in time to the day you first met. Maybe this time, you can make a
		better choice...
		""")
		math_test_room()
	elif choice == "3" and gift == "Big Sword":
		print("""
		You unsheathe your sword and let loose your battle cry: \"Math is for losers!\"
		The orcish math teacher grabs a giant club from behind his desk and runs at you!
		You barely move out of the way as he brings it down and smashes the chair you
		were supposed to sit in. You spin the blade around in a big circle and cut off
		his head! His body collapses and his head rolls up to your feet, with a scowl on
		it\'s face. You burn the room down for good measure as you move into the next.
		""")
	else:
		death("You are too dumb to type a number.")
	print ("\033[0;31mHit ENTER to do to the next room!\033[0m")
	input("> ")


def yoga_room():
	'''The player encounters a yoga master'''
	global gift
	global wis
	print ("\033[0;32mIt\'s a room with a yoga class!\033[0m")
	print("""
	The class has several people contorted into strange pretzel shaped positions on yoga
	mats on the floor. A young man with a long ponytail and wearing a pink bandana
	approaches you. \'Namasstea\' he says. \'Would you care to hear the long and fuzzy
	tale of my people?\'
	""")
	if gift == "History Book":
		print("""
		You open your history book:
		\033[0;36mYoga is an ancient art practiced by hippies and lizard people that want
		to hide their true identities and live in secret amongst actual humans. They are
		harmless and actually have wise things to say if you take the time to 
		listen.\033[0m
		""")
	print ("\033[0;31mWhat do you do next?\033[0m")
	print ("1. Listen and learn the ways of the yoga master.")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success AND increase your Wisdom!\033[0m")
	print ("2. Punch him in the face and run away.")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success")
	choice = input("> ")
	if choice == "1":
		print("""
		The young man talks for a very long time about ancient meditation techniques
		and lizard people. It takes hours, but you feel your mind open up and the cosmic
		wisdom of the universe flows into you.
		""")
		print ("\033[0;32mYour Wisdom got good!\033[0m")
		wis += 1
	elif choice == "2":
		print("""
		You break his nose and he falls to the ground screaming. There are surprised
		gasps from the people in class and a little girl starts crying. You realize that
		you are a horrible, horrible person and you run out of the room.
		""")
	else:
		death("You are too dumb to type a number.")
	print ("\033[0;31mHit ENTER to go to the next room!\033[0m")
	input("> ")


def weight_room():
	'''The player encounters a weight lifting bro'''
	global gift
	global str
	print ("\033[0;32mIt\'s a room filled with weight lifting equipment!\033[0m")
	print("""
	A huge bro approaches you. His biceps are as thick as your head and he is wearing one
	of those t-shirts with the sides cut out so you can se his armpits. He says \"Bro,
	do you even lift?\"
	""")	
	if gift == "History Book":
		print("""
		You open your history book:
		\033[0;36mYou find a chapter dedicated to physical fitness and body building. You
		learn that lifting weights is very good for you. Fascinating.\033[0m
		""")
	print ("\033[0;31mWhat do you do?\033[0m")
	print ("1. Fight him")
	if gift == "Calculator":
		print ("\033[0;36m25% chance of success\033[0m")
	print ("2. Lift weights")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success\033[0m")
	if gift == "Steroids":
		print ("\033[0;36m3. Share your steroids\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1" and fate < 4:
		print("""
		You punch his face as hard as you can and you break your hand. That was stupid.
		""")
		death("The bro rips your spine out!")
	elif choice == "1" and fate == 4:
		print("""
		You wait until he isn\'t looking and then you stab him in the neck with a 
		screwdriver. Wait, where did you get a screwdriver? You must be pretty lucky to
		have pulled that off. You move into the next room covered in blood.
		""")
	elif choice == "2":
		print("""
		Bro spots you as you bench several reps of heavy weight. You move on to curls,
		squats and deadlifts. You spend all night at the gym, lifting, hydrating and
		drinking protein shakes. You feel bigger but you are too sore to move. Nice
		lift, bro!
		""")
		print ("\033[0;32mYour Strength got good!\033[0m")
		str += 1
	elif choice == "3" and gift == "Steroids":
		print("""
		\"YES! Bro, yes! Yes. Give me those!\" says bro. You give him your steroids and
		he grows enormous. He becomes impossibly huge, growing through the roof and into
		the heavens. He blots out the sun and bellows: \"Who sucks now, TERRY?! BWA HA
		HA HA!\" The earth quakes as he stomps off, looking for revenge, apparently. You
		move into the next room.
		""")
	else:
		death("You were too dumb to type a number")
	print ("\033[0;31mHit ENTER to go to the next room!\033[0m")
	input("> ")


def medusa_room():
	'''The player encounters Medusa'''
	global gift
	global dex
	print ("\033[0;32mIt's a room with a Medusa in it!\033[0m")
	print("""
	You enter a room with several surprisingly lifelike stone statues. They all have
	horrified looks on their faces and they are all looking in the same direction.
	""")
	if gift == "History Book":
		print("""
		You open your History Book:
		\033[0;36mOne of the most dangerous monsters known to exist is the medusa. It is 
		said to be so hideous that looking upon it\'s face turns you to stone. Only a 
		complete idiot would look at one!\033[0m
		""")
	print ("\033[0;31mWhat do you do?\033[0m")
	print ("1. Look up to see what the statues are looking at.")
	if gift == "Calculator":
		print ("\033[0;36m0% chance of success\033[0m")
	print ("2. Close your eyes and run wildly for the exit")
	if gift == "Calculator":
		print ("\033[0;36m50% chance of success\033[0m")
	if dex > 0 and gift == "Sexy Wig":
		print ("\033[0;36m3. Cover your eyes with the Sexy Wig")
		print ("4. (Good Dexterity) Backflip over everything!\033[0m")
	elif gift == "Sexy Wig":
		print ("\033[0;36m3. Cover your eyes with the Sexy Wig\033[0m")
	elif dex > 0:
		print ("\033[0;36m3. Backflip over everything!\033[0m")
	choice = input("> ")
	fate = random.randint(1,2)
	if choice == "1":
		print("""
		You look up to stare straight into the eyes of Medusa! Your body feels heavy and
		solid. Your last thought before turning to stone is \'Damn, that was stupid!\'
		""")
		death("You turned into a statue.")
	elif choice == "2" and fate == 1:
		print("""
		You run straight into a statue and fall over. You open your eyes to see Mesuda
		standing over you! She stares into your eyes and turns your body to stone.
		Bummer.
		""")
		death("You turned into a statue.")
	elif choice == "2" and fate == 2:
		print("""
		You blindly stumble around until you run into a door! You open your eyes long 
		enough to see the door handle and quickly exit the room without looking back.
		Lucky!
		""")
	elif choice == "3" and gift == "Sexy Wig":
		print("""
		You invite Medusa out for drinks. The two of you stay up all night talking and 
		you develop a deep genuine connection. You go back to Medusa\'s place and have a
		wild and passionately intimate night. You keep your wig over your eyes the
		entire time. In the morning you wake up with greyscale, but it was worth it.
		""")
	elif choice == "3" and dex > 0:
		print("""
		You close your eyes and start doing backflips! Backflip, backflip, backflip!
		You bound over statues, obstacles and Medusa herself! It was so cool! Too bad you
		had your eyes closed the whole time.
		""")
	elif choice == "4" and dex > 0:
		print("""
		You close your eyes and start doing backflips! Backflip, backflip, backflip!
		You bound over statues, obstacles and Medusa herself! It was so cool! Too bad you
		had your eyes closed the whole time.
		""")
	else:
		death("You were too dumb to type a number.")
	print ("\033[0;31mHit ENTER to go to the next room\033[0m")
	input("> ")


def skeleton_room():
	'''The player encounters a dozen skeletons'''
	global gift
	global str
	global wis
	print ("\033[0;32mIt\"s a room filled with skeletons!\033[0m")
	print("""
	About a dozen reanimated skeletons block your path. A couple of them have swords, one
	of them has a halberd.
	""")
	if gift == "History Book":
		print("""
		You open your history book:
		\033[0;36mSkeletons are poor warriors because they break easy. It\'s better to 
		fight than run away, although victory is never a guarantee.\033[0m
		""")
	print ("\033[0;31mWhat do you do?\033[0m")
	print ("1. Punch your way out!")
	if gift == "Calculator":
		print ("\033[0;36m75% chance of success\033[0m")
	print ("2. Run for the exit!")
	if gift == "Calculator":
		print ("\033[0;36m0% chance of success\033[0m")
	if gift == "Big Sword" and wis > 0:
		print ("\033[0;36m3. Slay them with your Big Sword!")
		print ("4. (Good Wisdom) Act like a zombie and walk by\033[0m")
	elif gift == "Big Sword":
		print ("\033[0;36m3. Slay them with your Big Sword!\033[0m")
	elif gift == "Calculator" and wis > 0:
		print ("\033[0;36m3. (Good Wisdom) Act like a zombie and walk by")
		print ("100% chance of success\033[0m")
	elif wis > 0:
		print ("\033[0;36m3. (Good Wisdom) Act like a zombie and walk by\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1" and fate > 1:
		print("""
		Skulls and bones shatter and crumble to dust under your mighty fists! Your
		knuckles ache, but now you feel stronger!
		""")
		print ("\033[0;32mYour strength got good!\033[0m")
		str += 1
	elif choice == "1" and fate == 1:
		print("""
		Skulls and bones shatter and crumble to dust under your mighty fists! But then,
		you strip over a femur and impale yourself on that halberd. Unlucky!
		""")
		death("You were impaled by a halberd.")
	elif choice == "2":
		print ("You run for the door and a dozen skeletons stab you to death. Bad idea!")
		death("You were stabbed to death by skeletons")
	elif choice == "3" and gift == "Big Sword":
		print("""
		You scream a mighty warcry and cleave your way through them like a hot knife
		through butter. Nice!
		""")
	elif choice == "3" and wis > 0:
		print("""
		You raise your hands and stumble forward with a blank expression. \"Braaaaaains!\"
		The skeletons ignore you as you stumble past, taking you for a fellow undead.
		Nice move.
		""")
	elif choice == "4" and wis > 0:
		print("""
		You raise your hands and stumble forward with a blank expression. \"Braaaaaains!\"
		The skeletons ignore you as you stumble past, taking you for a fellow undead.
		Nice move.
		""")
	else:
		death("You were too dumb to type a number")
	input("\033[0;31mHit ENTER to go to the next room!\033[0m")

def carmen_sandiego_room():
	'''The player encounters carmen sandiego'''
	global gift
	global dex
	print ("\033[0;32mYou enter a rom with the legendary theif, Carmen Sandiego!\033[0m")
	print ("""
	There she stands, the legendary thief Carmen Sandiego! She has managed to
	steal every national monument at one time or another. She disappeared sometime in the
	90\'s, you don\'t remember why.
	""")
	if gift == "History Book":
		print ("You open your history book:")
		print ("""
		\033[0;36mCarmen Sandiego is the world\'s greatest thief. She has evaded
		the law her entire life and always has an escape plan. Thieves are usually quite
		vain and love to talk about how awesome they are.\033[0m
		""")
	print ("\033[0;31mWhat do you do?\033[0m")
	print ("1. Yell \"You\'re under arrest!\"")
	if gift == "Calculator":
		print ("\033[0;36m0% chance of success\033[0m")
	print ("2. \"So... know any good card tricks?\"")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success\033[om")
	if gift == "Telepathic Implant":
		print ("\033[0;36m3. Learn her secrets with your telepathic implant\033[0m")
	if gift == "Big Sword":
		print ("\033[0;36m3. Kill her with your Big Sword!\033[0m")
	choice = input("> ")
	if choice == "1":
		print("""
		She throws down a smoke bomb and escapes. That was a dumb idea, but at least you
		didn\'t die.
		""")
	elif choice == "2":
		print ("""
		She is delighted to show you sleight of hand tricks using playing cards. 
		You feel like you could cheat at gambling now!
		""")
		print ("\033[0;32mYour dexterity got good!\033[0m")
		dex += 1
	elif choice == "3" and gift == "Telepathic Implant":
		print ("""
		You read her mind and discover her secrets! She has a massive network of
		underground tunnels that go all over the globe. You find a passageway that
		connects to this room and you follow it to the center of the earth. There you
		find all of the world\'s stolen monuments! You return them to their respective
		nations and are hailed as a world hero!
		""")
		print ("\033[0;32mYou found the super duper secret ending! Congratulations!\033[0m")
		exit(0)
	elif choice == "3" and gift == "Big Sword":
		print ("""
		You cleave right through her with a mighty swing! But... it doesn\'t
		hurt her? It\'s a hologram! As her image fades away you hear her distant voice
		mock you:\"Better luck next time gumshoe!\"
		""")
	else:
		death("You were too dumb to type a number")
	input("\033[0;31mHit ENTER to go to the next room!\033[0m")
	
def library_room():
	'''The player encounters a librarian'''
	global gift
	global cha
	global int
	print ("\033[0;32mIt\'s a giant library!\033[0m")
	print ("""
	There is an enormous selection of books and a cute librarian with glasses giving you
	a stern look. They seem skeptical that you can read.
	""")
	if gift == "History Book":
		print ("You open your history book:")
		print ("""
		\033[0;36mLibrarians are unimpressed with people who can\'t read and 
		they love people who have their own books. In fact, you should show the librarian 
		this book!\033[0m
		""")
	print ("\033[0;31mWhat will you do?\033[0m")
	print ("1. Read the first book off the shelf")
	if gift == "Calculator":
		print ("\033[0;36m100% chance of success\033[0m")
	print ("2. Say \"Reading is for losers!\"")
	if gift == "Calculator":
		print ("\033[0;36m0% chance of success\033[0m")
	if gift == "History Book":
		print ("\033[0;36m3. Show the librarian your history book\033[0m")
	if gift == "Sexy Wig":
		print ("\033[0;36m3. Seduce the librarian with your sexy wig\033[0m")
	choice = input("> ")
	if choice == "1":
		print ("""
		The first book on the shelf is \"Charisma for Dummies.\" It is an interesting
		read and you find yourself taking notes.
		""")
		print ("\033[0;32mYour charisma got good!\033[0m")
		cha += 1
	elif choice == "2":
		print ("""
		The librarian takes out a rocket launcher from behind the desk and shoots you
		with a missle. You explode. Ha ha! loser.
		""")
		death("You blew up")
	elif choice == "3" and gift == "History Book":
		print ("""
		\"Oh my goodness! What a big book!\" The librarian takes a look at your book
		and you both stay up all night reading. You feel smarter.
		""")
		print ("\033[0;32mYour intellegence got good!\033[0m")
		int += 1
	elif choice == "3" and gift == "Sexy Wig":
		print ("""
		You put on your sexy wig and seduce the librarian with some charming smalltalk.
		The two of you go down into the reading dungeon. Things get weird fast and 
		halfway through a Shakespeare recital you decide to escape. Seven cheesecakes
		and a shameful trip to the Amazon later, you decide you will never speak of the 
		night again.
		""")
	else:
		death("You were too dumb to type a number")
	input("\033[0;31mHit ENTER to go to the next room\033[0m")
	
def dance_contest_room():
	'''The player encounters a dance contest'''
	global gift
	global cha
	print ("\033[0;32mYou walk onto a stage in the middle of a dance contest!\033[0m")
	print ("""
	There are many contestants performing and they all freeze when you walk onto the
	stage. A panel of confused judges stare at you and everything goes quiet. There are
	thousands of people in the audience and there are cameras everywhere.
	""")
	if gift == "History Book":
		print ("""
		You take out your history book but you drop it on the floor! This is no time to 
		read, do something!
		""")
	print ("\033[0;31mWhat do you do?\033[0m")
	print ("1. Try to dance")
	if gift == "Calculator":
		print ("\033[0;36m75% chance of success\033[0m")
	print ("2. Try to sing")
	if gift == "Calculator":
		print ("\033[0;36m25% chance of success\033[0m")
	if cha > 0:
		print ("\033[0;36m3. Charm the judges with your charisma\033[0m")
		if gift == "Calculator":
			print ("\033[0;36m100% chance of success\033[0m")
	if cha > 0 and gift == "Telepathic Implant":
		print ("\033[0;36m4. Make the judges cry by reading thier minds with your")
		print ("telepathic implant\033[0m")
	if cha == 0 and gift == "Telepathic Implant":
		print ("\033[0;36m3. Make the judges cry by reading thier minds with your")
		print ("telepathic implant\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1" and fate > 1:
		print ("""
		You remember some dance moves you saw on T.V. and you stumble through them. By 
		the grace of the sun you manage to survive until the next act. You sneak away
		unscathed.
		""")
	elif choice == "1" and fate == 1:
		print ("""
		You try to dance but you trip and fall flat on your face. The judges are
		displeased and they summon a demon to dispatch you. The crowd cheers for blood
		as you are torn limb from limb. Bummer!
		""")
		death("You were ripped apart by a demon")
	elif choice == "2" and fate > 3:
		print ("""
		You sing a love song you heard on the radio once. You are amazed that you
		remember how it went and you manage to finish the song with minimal booing from
		the crowd. You sneak away when nobody is looking.
		""")
	elif choice == "2" and fate < 4:
		print ("""
		You start singing the \'Hokey Pokey\' but the crowd drowns you out with annoyed
		booing before you can finish the first verse. They pelt you to death with rotten
		tomatoes. Dang.
		""")
		death("You were killed by rotten fruit")
	elif choice == "3" and cha > 0:
		print ("""
		You are so smooth that you build instant rapport with the judges. After some
		flirtation and inside jokes you miraculously win first place in the contest. It\'s
		funny how that works, huh?
		""")
	elif choice == "3" and gift == "Telepathic Implant":
		print ("""
		You read the judges mind and give them exactly what they want. You sing the most
		beautiful love song in existence and it brings them to tears. You receive a
		standing ovation and win first place. Great job!
		""")
	elif choice == "4" and gift == "Telepathic Implant":
		print ("""
		You read the judges mind and give them exactly what they want. You sing the most
		beautiful love song in existence and it brings them to tears. You receive a
		standing ovation and win first place. Great job!
		""")
	else:
		death("You were too dumb to type a number")
	input("\033[0;31mHit ENTER to go to the next room\033[0m")

def death_room():
	'''The player encounters lava, bees, and falling rocks'''
	global gift
	print ("\033[0;32mIt\'s a room filled with death!\033[0m")
	print ("""
	There is a river of lava! Rocks are falling everywhere! A swarm of bees is 
	chasing you! Oh my!
	""")
	if gift == "History Book":
		print ("You open your history book:")
		print ("""
		\033[0;36mLava has a historical precedent for melting people who touch
		it. Duh. If a rock fell on you it would definitely kill you, but bee stings are
		only fatal sometimes. You just need to take a chance!\033[0m
		""")
	print ("\033[0;31mWhat will you do?\033[0m")
	print ("1. Swim through the lava!")
	if gift == "Calculator":
		print ("\033[0;36m0% chance of success\033[0m")
	print ("2. Run throught the bees!")
	if gift == "Calculator":
		print ("\033[0;36m75% chance of success\033[0m")
	print ("3. Weave through the falling rockss!")
	if gift == "Calculator":
		print ("\033[0;36m25% chance of success\033[0m")
	choice = input("> ")
	fate = random.randint(1,4)
	if choice == "1":
		print ("""
		You jump into the lava and burn to death in the most horrible ten
		seconds of your life. Dude! Why?
		""")
		death("Dissolved by lava")
	elif choice == "2" and fate > 1:
		print("""
		You do the only sensible thing and run through a swarm of angry stingers!
		They must be more focused on the rocks and lava, you get past un-stung! Awesome.
		""")
	elif choice == "2" and fate == 1:
		print ("The bees all pull out knives. \"Stab the mammal!\" they scream. Uh oh.")
		death("Stabbed to death by a swarm of knife fighting bees")
	elif choice == "3" and fate == 4:
		print ("""
		You weave through the rocks like a ninja! You feel more lucky than
		skilled though, you should have died.
		""")
	elif choice == "3" and fate < 4:
		print ("""
		You run for it but there is no way for you to predict where the rocks
		will fall. A very nice slab of granite crushes your skull.
		""")
		death("Killed by a nice slab of granite")
	else:
		death("You were too dumb to type a number")
	input("\033[0;31mHit ENTER to go to the next room\033[0m")
		
def travis_room():
	'''The player encounters Travis the Terrible'''
	global gift
	global str
	global dex
	global int
	global wis
	global cha
	print ("\033[0;32mYou enter a room with the most handsome man alive, Travis!\033[0m")
	print("""
	This will be the most difficult challenge you have ever faced! Travis has a natural
	20 in every stat, he can punch mountains in half, he can kill by raising an eyebrow
	and he has a degree. You must use everything at your disposal and make a careful 
	choice!
	""")
	if gift == "History Book":
		print ("You open up your history book:")
		print ("... but Travis disintegrates it with his laser eyes! Oh shit!")
	if gift == "Calculator":
		print ("""
		You take out your trusty calculator to figure the chances of success for your
		options, but something strange happens. Travis blesses it with artificial
		intelligence! Then he gives it a logical paradox and it self-destructs! You are 
		now left with only a pile of broken circuits and your wits.
		""")
	print ("\033[0;31mWhat will you do?\033[0m")
	if gift == "Big Sword":
		print ("\033[0;36mb. Kill him with your big sword!\033[0m")
	if gift == "Calculator":
		print ("\033[0;36mc. Throw your bits of broken calculator under his feet!\033[0m")
	if gift == "Steroids":
		print ("\033[0;36ms. Rage out with your steroids!\033[0m")
	if gift == "Telepathic Implant":
		print ("\033[0;36mt. Read his mind with your telepathic implant\033[0m")
	if gift == "Sexy Wig":
		print ("\033[0;36mx. Seduce him with your sexy wig\033[0m")
	if gift == "History Book":
		print ("\033[0;36mh. Blow the ashes of your history book into his eyes\033[0m")
	if str > 0:
		print ("\033[0;36mR. Punch his face off with your superior stength!\033[0m")
	if dex > 0:
		print ("\033[0;36md. Do backflips until he dies!\033[0m")
	if wis > 0:
		print ("\033[0;36mw. Use your superior wisdom to connect with him\033[0m")
	if int > 0:
		print ("\033[0;36mi. Use intellegence to fight him in a battle of wits!\033[0m")
	if cha > 0:
		print ("\033[0;36mch. Charm him by being a charismatic motherfucker!\033[0m")
	print ("f. follow your heart")
	choice = input("> ")
	if choice == "b" and gift == "Big Sword":
		print("""
		You slice at him with your big sword, but it shatters! Travis's skin is made of
		diamond! The dust from your sword makes Travis sneeze and the force blasts all
		of your flesh from your bones. Now you are a skeleton.
		"""	)
		death("Sneezed into a skeleton")
	if choice == "c" and gift == "Calculator":
		print("""
		Travis steps on the pointy circuits and they hurt his feet. \'Ow!\' he yells and
		he jumps up on a chair. \'It\'s like stepping on legos!'\' You feel relieved, now
		you\'ve got him where you want him! \'What are you looking so relieved for? The
		FLOOR IS LAVA!\' You look down and sure enough your shins have melted. As you
		sink you wonder, \'How did he do that?\'
		""")
		death("Sunk into lava floor")	
	if choice == "s" and gift == "Steroids":
		print("""
		You take all of your steroids and become huge! Your muscles grow and grow until
		you are the size of a building! You are so swole you can\'t even move! You have a
		heart attack and die. Travis was playing video games, he didn\'t even notice.
		""")
		death("heart attack")
	if choice == "t" and gift == "Telepathic Implant":
		print("""
		You read his mind and what you see is indescribable. The terrible beauty of
		Travis\'s mind fills your being. You hear a soft buzzing noise and your head
		explodes, but it was worth it.
		""")
		death("your head exploded")
	if choice == "x" and gift == "Sexy Wig":
		print("""
		You put on your sexy wig and use your best moves to seduce Travis. Your efforts
		have no effect and he just stares at you, unimpressed. He summons the
		Dragon-Megazord and it stomps you to death. It was pretty cool, too bad you\'re
		dead!
		""")
		death("stomped on by Dragon-Megazord")
	if choice == "h" and gift == "History Book":
		print("""
		You blow the ashes of your history book into Travis\'s eyes but he just opens 
		his mouth and inhales them! \'YES! FEED MY YOUR KNOWLEDGE!\' He cracks your head
		open and eats your brain, but he didn\'t learn anything.
		""")
		death("You had your brain eaten")
	if choice == "R" and str > 0:
		print("""
		You punch his face off!... But it fles around the room in a big circle?! His 
		boomerang face laughs at you from all directions as it flies around the room. Then
		it cuts off your head like a razor disc before reattaching itself to Travis\'s 
		head. That was weird AF!
		""")
		death("you got decapitated")
	if choice == "d" and dex >0:
		print("""
		You begin to backflip, and backflip... and backflip. The world turns into blurry
		vertical lines of light as the directions up and down lose meaning. You hear a 
		voice: \"YES! MORE BACKFLIPS!\" Travis comes into focus as you realize he has
		synchronized his backflips to go along with yours. He grabs your arm. \"FASTER!
		These are like vitamins to me!\" He pulls you into faster and faster backflips. 
		Blood pools in your extremities like you are in a centerfuge. Your arms and legs
		fly off and you die, but hey, that was pretty cool, huh?
		""")
		death("dismembered by backflips")
	if choice == "w" and wis>0:
		print("""
		You tell Travis a fable about a wise monk who learned the value of mercy by
		watching grasshoppers and ants. You tell the story well and Travis appears to 
		understand. \"I see now.\" He says. \"In order to achieve enlightenment I need to
		rip your arms off, just as one would rip the arms off of a grasshopper!\" Before
		you can say anything he rips your arms off and you bleed out. You should have
		been wise enough to choose another option!
		""")
		death("arms ripped off")
	if choice == "i" and int > 0:
		print("""
		You challenge Travis to a battle of wits. You set out two cups of wine and tell
		him that you have secretly poisoned one of them with iocane power. The battle
		of wits has begun! You are stunned when Travis drinks both cups and then pops your
		head off and drinks all the blood from your body like you were a soda can. It 
		turns out the antidote to iocane powder is drinking a human sized container of
		blood. 
		""")
		death("drunk like a soda pop")
	if choice == "ch" and cha>0:
		print("""
		You open a can of charismatic whoop ass and lay it on thick. Travis isn\'t
		impressed. Like, at all. You get the feeling he put in charismatic and sexy
		roleplay options for the lols, but he would rather crush your bones. So, he does.
		""")
		death("crushed bones")
	if choice == "f":
		print("""
		You search your feelings and know your choice. Your heart sings a song of
		undeniable courage and passion. You know exactly what to do. You walk up to
		Travis, look him dead in the eye and flex your muscles. \"Travis, you\'re dumb
		and nobody likes you.\" A single tear runs down Travis\'s cheek and you both
		understand a deep and powerful truth. He acknowledges your strong heart and allows
		you to pass. Truly, you are the master of Travis Quest.
		""")
		con = "\033[5;31mCON\033[0m"
		gr = "\033[5;33mGR\033[0m"
		atu = "\033[5;32mATU\033[0m"
		la = "\033[5;36mLA\033[0m"
		tio = "\033[5;34mTIO\033[0m"
		ns = "\033[5;35mNS\033[0m"
		print (con + gr + atu + la + tio + ns + "\033[5;37m!\033[0m")
		exit(0)
	else:
		death("you were too dumb to type a letter")
		
rooms = ["rock_room", "math_test_room", "yoga_room", "weight_room", "medusa_room",
"skeleton_room", "carmen_sandiego_room", "library_room", "dance_contest_room",
"death_room"]
gifts = ["Big Sword", "Steroids", "Telepathic Implant", "History Book", "Calculator",
 "Sexy Wig"]
str = 0
dex = 0
wis = 0
int = 0
cha = 0
gift = "nothing"
first_room()
for i in range(0,5):
	print (" ")
	print ("\033[0;32mIt is time to enter a new room! You open the door...\033[0m")
	random_number = random.randint(0,9-i)
	current_room = rooms.pop(random_number)
	if current_room == "rock_room":
		rock_room()
	elif current_room == "math_test_room":
		math_test_room()
	elif current_room == "yoga_room":
		yoga_room()
	elif current_room == "weight_room":
		weight_room()
	elif current_room == "medusa_room":
		medusa_room()
	elif current_room == "skeleton_room":
		skeleton_room()
	elif current_room == "carmen_sandiego_room":
		carmen_sandiego_room()
	elif current_room == "library_room":
		library_room()
	elif current_room == "dance_contest_room":
		dance_contest_room()
	elif current_room == "death_room":
		death_room()
	else:
		print ("something went horribly wrong")
travis_room()