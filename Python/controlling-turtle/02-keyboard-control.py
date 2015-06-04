import turtle

wm = turtle.Screen()
t = turtle.Turtle()

print "I'm a turtle! You can tell me where to go by typing in commands!"

run = True
while(run):
	command = raw_input("Where should i go now? ")
	
	if command in ("f", "forward"):
		t.forward(50);
	elif command in ("l", "left"):
		t.left(90)
		t.forward(50)
	elif command in ("r","right"):
		t.right(90)
		t.forward(50)
	elif command in ("q", "quit", "exit"):
		run = False
		print "Click on the turtle to exit"
	else: 
		print "Sorry, i don't know what " + command + " means "
		
	
wm.exitonclick()