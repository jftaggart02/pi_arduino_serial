import Zomby
from time import sleep

if __name__ == "__main__":
    zomby = Zomby.Zomby("COM6", 9600)

    # Forward at 10%
    zomby.forward(10)
    sleep(5)

    # Backward at 10%
    zomby.backward(10)
    sleep(5)

    zomby.stop()