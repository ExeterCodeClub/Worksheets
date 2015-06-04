import turtle

wm = turtle.Screen()
t = turtle.Turtle()

print "I'm a turtle! You can tell me where to go by typing in commands!"

run = True
while(run):
	command = raw_input("Where should i go now? ")
	
	if command == "f":
		t.forward(50);
	if command == "l":
		t.left(90)
		t.forward(50)
	if command == "r":
		t.right(90)
		t.forward(50)
	if command == "q":
		run = False
	

wm.exitonclick()