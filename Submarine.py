
#
# Program
#

#RANDOMIZE TIMER
import random


def Initialise():

	global a
	global power
	
	
	global sonarData
	

	#6300 :
	# Island data
	islandData = [	0, 1, 1, 1, 0, 0, 
					0, 1, 1, 1, 1, 0, 
					1, 1, 1, 0, 1, 1, 
					1, 1, 0, 0, 0, 1, 
					1, 1, 0, 0, 1, 1, 
					0, 1, 1, 0, 1, 0, 
					0, 0, 1, 0, 0, 0]
	
	#6090 :
	# Course/Direction data
	directionData = [-1,0, -1,1, 0,1, 1,1, 1,0, 1,-1, 0,-1, -1,-1]
	
	#1830 :
	# Sonar data
	sonarData = ["   ", "***", "(X)", "\S/", "!H!", " $ ", "-#-"]

	

					
	# Game area array
	#DIM a(20, 20)
	a = [[0 for row in range(0, 20)] for col in range(0, 20)]

	#DIM d(9)

	
	# Set up area
	for i in range(0, 20):
		
		for j in range(0, 20):
			
			a[i][j] = 0


	# Island
	#RESTORE 6300
	islandDataIndex = 0
	
	for i in range(7, 14):
		
		for j in range(7, 13):
			
			#READ a(x, y)
			a[i][j] = islandData[islandDataIndex]
			
			islandDataIndex = islandDataIndex + 1


	# Sub
	s1 = 10
	s2 = 10
	
	a[s1][s2] = 2


	# Enemy ships
	s = random.randint(1, 16) + 15
	
	#RESTORE 6090
	directionDataIndex = 0
	
	for x in range(1, ((random.randint(1, 4) + 1) * 2 - 1)):
		
		#READ d8, d9
		d8 = directionData[directionDataIndex]
		d9 = directionData[directionDataIndex + 1]
		
		directionDataIndex = directionDataIndex + 2
	
	for x in range(s):
		
		x1 = random.randint(0, 19)
		x2 = random.randint(0, 19)
		
		while (a[x2][x2] != 0):
			
			x1 = random.randint(0, 19)
			x2 = random.randint(0, 19)
			
		a[x1][x2] = 3


	# Headquarters
	s3 = random.randint(0, 19)
	s4 = random.randint(0, 19)
	
	while (a[s3][s4] != 0):
		
		s3 = random.randint(0, 19)
		s4 = random.randint(0, 19)

	a[s3][s4] = 4


	# Underwater mines
	for x in range(random.randint(1, 8) + 8):
		
		x1 = random.randint(0, 19)
		x2 = random.randint(0, 19)
	
		while (a[x1][x2] != 0):
			
			x1 = random.randint(0, 19)
			x2 = random.randint(0, 19)
            
		a[x1][x2] = 5


	# Sea monsters
	for x in range(1, 4):
		
		x1 = random.randint(0, 19)
		x2 = random.randint(0, 19)
		
		while (a[x1][x2] != 0):
			
			x1 = random.randint(0, 19)
			x2 = random.randint(0, 19)
			
		a[x1][x2] = 6
		
		#RESTORE 6090
		directionDataIndex = 0
		
		for y in range(1, 8):
			
			#READ m1, m2
			m1 = directionData[directionDataIndex]
			m2 = directionData[directionDataIndex + 1]
			
			directionDataIndex = directionDataIndex + 2


	# Set starting values
	#FOR i = 1 TO 9
	#d(i) = 0
	#NEXT
	
	#c = 30
	crew = 30
	
	#p = 6000
	power = 6000
	
	#f = 2500
	fuel = 2500
	
	#t = 10
	torpedoes = 10
	
	#m = 3
	missiles = 3
	
	d = 100
	
	d2 = 2
			
# End of Initialise()











#1680 :
# #1: Sonar
def SonarControl():
	
	global power
	
	
	#IF d(2) >= 0 THEN 1720
	#print "Sonar is under repair "; n$; "."
	#GOTO 880

	#1720 :
	#IF c > 5 THEN 1750
	#print "Not enough crew to work sonar "; n$; "."
	#GOTO 880

	#1750 :
	#INPUT "Option #"; o
	#ON INT(o + 1) GOTO 1790, 2010
	#GOTO 1750


	#1790 :
	# print out map
	#print
	print()
	
	#FOR x = 1 TO 20
	for x in range(0, 20):
		
		#FOR y = 1 TO 20
		for y in range(0, 20):

			#1830 :
			#DATA "   ","***","(X)","\S/","!H!"," $ ","-#-"
			
			#IF a(x, y) <> 0 THEN 1880
			if a[x][y] != 0:
				
				SonarControl_1880(x, y)
				
			else:
				
				print(" . ", end = '')
				
			#IF x <> 1 AND x <> 20 AND y <> 1 AND y <> 20 THEN 1880
			#if x != 0 and x != 20 and y != 0 and y != 20:
				
				#SonarControl_1880(x, y)
				
			#else:
				
				#print(" . ", end = '')

			#1860 :
			#print " . ";
			#print(" . ", end = '')
			#GOTO 1950

		#1950 :
		#NEXT
		
		#print
		print()
	
	#NEXT

	#1980 :
	#p = p - 50
	power = power - 50
	
	#IF p > 0 THEN 880
	#GOTO 1660

# End of SonarControl()


# 1880 :
def SonarControl_1880(x, y):

	#RESTORE 1830
	sonarDataIndex = 0
			
	#FOR x1 = 1 TO a(x, y) + 1
	for x1 in range(1, a[x][y] + 1):
		
		#READ a$
		sonarDisplay = sonarData[x1]
		
		sonarDataIndex = sonarDataIndex + 1
				
	#NEXT
			
	#IF d < 50 AND RND(1) < .23 AND a(x, y) <> 1 AND a(x, y) <> 2 THEN 1860
	#IF RND(1) < .15 AND a(x, y) > 2 THEN 1860
	
	#print a$;
	print(sonarDisplay, end = '')

# End of SonarControl_1880()

# 2010 :
def SonarControl_2010():
	
	# Directional information
	
	#FOR i = 1 TO 5
	#b(i) = 0
	#NEXT
	
	#print "Direction   # Of Ships    Distances"
	print("Direction   # Of Ships    Distances")
	
	#RESTORE 6090
	#FOR x = 1 TO 8
	#READ x1, y1
	#x3 = 0
	
	#FOR x4 = 1 TO 20
	#IF s1 + x1 * x4 < 1 OR s1 + x1 * x4 > 20 OR s2 + y1 * x4 < 1 OR s2 + y1 * x4 > 20 THEN 2140
	#IF a(s1 + x1 * x4, s2 + y1 * x4) <> 3 THEN 2130
	#x3 = x3 + 1
	#b(x3) = x4

	#2130 :
	#NEXT

	#2140 :
	#IF x3 = 0 THEN 2200
	#print "   "; x, x3,
	#FOR x4 = 1 TO x3
	#print b(x4);
	#NEXT
	#print

	#2200 :
	#NEXT
	#GOTO 1980

# End of SonarControl_2010()













#CLS

#print TAB(33); "Seabat"
#print
#print
#print

#INPUT "What is your name "; n$
#print

	
#print "You must destroy"; s; "enemy ships to win "; n$; "."



#880 :
# Command section
def CommandControl():
	
	print()
	print()
	#print("What are your orders " + n$ + " ")
	
	#input o
	
	#ON INT(o + 1) GOTO 1040, 1680, 2220, 2680, 3250, 3410, 3700, 3880, 4400, 4660
	
	print("The commands are:")
	print()
	print("     #0: Navigation")
	print("     #1: Sonar")
	print("     #2: Torpedoes")
	print("     #3: Missiles")
	print("     #4: Maneuvering")
	print("     #5: Status/Damage Report")
	print("     #6: Headquarters")
	print("     #7: Sabotage")
	print("     #8: Power Conversion")
	print("     #9: Surrender")
	
	#GOTO 880

# End of CommandControl()








Initialise()

SonarControl()








