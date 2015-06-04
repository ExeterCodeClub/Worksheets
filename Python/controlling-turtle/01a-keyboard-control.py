import turtle

wm = turtle.Screen()
t = turtle.Turtle()

print "I'm a turtle! You can tell me where to go by typing in commands!"

run = True
while(run):
	command = raw_input("Where should i go now? ")
	
	if command == "f":
		t.forward(50);
	if command == "q":
		run = False
	# can you add in commands for turning left and right?
	# Hint: to make our turtle turn right, we would write t.right(90) to turn 90 degrees. 
	

wm.exitonclick()