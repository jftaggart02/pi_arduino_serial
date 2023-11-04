import Zomby
from time import sleep

if __name__ == "__main__":
    zomby = Zomby.Zomby("COM11", 9600)

    # Forward at 10% speed
    zomby.forward(10)
    sleep(5)

    # Backward at 10% speed
    zomby.backward(10)
    sleep(5)

    # Turn right at 10% speed
    zomby.turnRight(10)
    sleep(5)

    # Turn left at 10% speed
    zomby.turnLeft(10)
    sleep(5)

    # Slow to a stop
    zomby.stop()
    sleep(5)