import turtle

wm = turtle.Screen()
t = turtle.Turtle()

print "I'm a turtle! You can tell me where to go by typing in commands!"

run = True
while(run):
	command = raw_input("Where should i go now? ")
	
	if command in ("f", "forward"):
		amount = raw_input("How far? ")
		t.forward(int(amount))
	elif command in ("l", "left"):
		amount = raw_input("How much should i turn? ")
		t.left(int(amount))
	elif command in ("r","right"):
		amount = raw_input("How much should i turn? ")
		t.right(int(amount))
	elif command in ("q", "quit", "exit"):
		run = False
		print "Click on the turtle to exit"
	else: 
		print "Sorry, i don't know what " + command + " means "
		
	
wm.exitonclick()