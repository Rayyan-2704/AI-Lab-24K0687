class SmartLight:
    def __init__(self, room_name, status = False):
        self.room_name = room_name
        self.status = status

    def toggle_light(self):
        if self.status == True:
            self.status = False
            st = "OFF"
        else:
            self.status = True
            st = "ON"
        print(f"{self.room_name} light turned {st}.")

    def check_status(self):
        if self.status == False:
            st = "OFF"
        else:
            st = "ON"
        print(f"{self.room_name} light is {st}.")

def main():
    l1 = SmartLight("Living Room", True)
    l2 = SmartLight("Bedroom", False)
    l1.check_status()
    l2.check_status()
    l1.toggle_light()
    l2.toggle_light()

main()
