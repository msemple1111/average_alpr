#!bin/python3
from error import error
from database import database
class admin:
    def __init__(self):
        self.file_name = "out.txt" #the file where the output will be saved

        self.commands = {
        "help":"Show this message",
        "exit":"Quit this program",
        "speeders": "Outputs speeders and addresses to file",
        "speeders_foreign": "Outputs foreign speeders to file"
        }#a dictionary of the commands that can be run
        self.sqlite = database() #start the database class for data retriaval
        print("ALPR Admin Util V0.2")
        print("Enter 'help' for usage hints.\nEnter 'exit' to quit.\n> ")#welcome message
        self.quit = False#while loop
        while self.quit == False:
            self.term_in = input("alpr_util> ").lower() #terminal input line
            if self.term_in in self.commands: #if terminal input command is in commands list
                getattr(self, '%s' % self.term_in)() #run the function with the same name
            else:
                print("Error: unknown command: '"+str(self.term_in)+"'. Enter 'help' for help")#or display an error message and reloop

    def help(self):
        for key, value in self.commands.items():#display each command
            print('{:<16}  {}'.format(key, value))#format string with spaces

    def exit(self):
        self.quit = True #end program

    def save_to_file(self, string_out): #save the input string to a file
        with open(self.file_name, 'w') as afile: #open file
            afile.write(string_out)#write to file

    def make_speed_string(self, list_in):#make the string to output
        plate = self.sqlite.get_plate(list_in[1])#get the plate string from sqlite
        site, speed_limit = self.sqlite.get_site(list_in[3])#get the site name and speed limit from sqlite
        speed = list_in[6] + speed_limit #workout speed of car
        speed_mph = round((speed * 2.2369362920544), 2) #convert m/s to mph and round to 2dp
        speed_limit_mph = round((speed_limit * 2.2369362920544), 2)#convert m/s to mph and round to 2dp
        string = "Plate: " + plate + "   Speed: " + str(speed_mph) + "mph    Speed limit: " + str(speed_limit_mph) +"mph   Road: " + site#compile string
        return string#ouput string

    def make_address_string(self, p_id):#make the string to output
        get_owner = self.sqlite.get_owner(p_id)#get owner and address from sqlite
        if get_owner == None:#none type means that plate has no address associated
            return '' #return nothing
        owner, address = get_owner #split up the tuple
        string = "Owner: " + owner + "   Address: " + address#compile string
        return string#ouput string

    def speeders(self):
        speeders = self.sqlite.return_speeders()#get list of all the speeders
        string_out = ''#create empty string for output
        for x in speeders: #do one speeder at a time
            string_out = string_out + self.make_speed_string(x) + "   "#make the speeding string
            string_out = string_out + self.make_address_string(x[1]) + "\n"#make the address string
        print(string_out)#print string first
        self.save_to_file(string_out)#then save it to file
        print("Saved speeders to:",self.file_name)#print where it was saved

    def speeders_foreign(self):#only compiles foreign speeders
        speeders = self.sqlite.return_foreign_speeders()#get list of all the foreign speeders
        string_out = ''#create empty string for output
        for x in speeders:#do one speeder at a time
            string_out = string_out + self.make_speed_string(x) + "\n"#make the speeding string
        print(string_out)#print string first
        self.save_to_file(string_out)#then save it to file
        print("Saved speeders to:"+self.file_name)#print where it was saved


if __name__ == '__main__':#only run if admin.py is executed directly
    start = admin()#run class
