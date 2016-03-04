#!bin/python3
from error import error
from database import database
class admin:
    def __init__(self):
        self.commands = {
        "help":"Show this message",
        "exit":"Quit this program",
        "filename":"filename ?name?\n\
               Set the file name to output to - No Spaces.\n\
               Default 'out.txt'",
        "speeders": "outputs speeders to file",
        }
        self.sqlite = database()
        self.file_name = "out.txt"
        print("ALPR Admin Util V1.1")
        print("Enter 'help' for usage hints.\nEnter 'exit' to quit.")
        self.quit = True
        while self.quit:
            self.term_in = input("alpr_util> ").lower()
            self.term_in_split = self.term_in.split()
            if self.term_in_split[0] in self.commands:
                getattr(self, '%s' % self.term_in_split[0])()
            else:
                print("Error: unknown command: '",str(self.term_in), self.term_in_split,"'. Enter 'help' for help")
                error(51, "admin.init() error", False)

    def help(self):
        for key, value in self.commands.items():
            print('{:<12}  {}'.format(key, value))

    def exit(self):
        self.quit = False

    def filename(self):
        if len(self.term_in_split) == 2:
            self.file_name = str(self.term_in_split[1])
        else:
            print("Error: Too many arguments: Usage 'filename out.txt' - No Space Allowed in filenam")

    def speeders(self):
        self.return_speeders()

if __name__ == '__main__':
    start = admin()
