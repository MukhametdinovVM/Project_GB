from time import sleep

class TrafficLight:

    _colour = ["Red", "Yellow", "Green"]

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight._colour[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            i += 1

Traffic = TrafficLight()
Traffic.running()
