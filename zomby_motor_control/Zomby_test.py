import Zomby
from time import sleep

if __name__ == "__main__":
    zomby = Zomby.Zomby("COM6", 9600)

    zomby.forward(10)
    sleep(5)

    zomby.backward(10)
    sleep(5)

    zomby.stop()