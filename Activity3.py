class bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print("Bird")
    def swim(swim):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("run faster")
peggy=penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()