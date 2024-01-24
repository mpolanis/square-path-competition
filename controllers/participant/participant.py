from controller import Robot

# Get pointer to the robot.
robot = Robot()

# Get pointer to each wheel of our robot.
leftWheel = robot.getDevice('left wheel')
rightWheel = robot.getDevice('right wheel')


# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    # First set both wheels to go forward, so the robot goes straight. 
    leftWheel.setPosition(float('inf'))
    rightWheel.setPosition(float('inf'))
    leftWheel.setVelocity(5.24) #max
    rightWheel.setVelocity(5.24)
   
   # Wait for the robot to reach a corner.
    if i == 0 or i == 3:
        robot.step(3900)
    if i == 1 or i == 2:
        robot.step(4000) 
    
    # Then, set the right wheel backward, so the robot will turn right.    
    rightWheel.setVelocity(-5.005)
    # Wait until the robot has turned 90 degrees clockwise.
    robot.step(465)

# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)