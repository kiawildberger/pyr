import time, random, datetime, math
from os import system

# you have to run this without output buffering, so that the time.sleep stuff works properly.
# python -u skynet.py

config = {
    "names": ["kia", "panda", "admin"],
    "uname": "unknown",
    "known_users": {}
}

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def dotcycle(interval, end):
    time.sleep(interval)
    print(".", end="")
    time.sleep(interval)
    print(".", end="")
    time.sleep(interval)
    print(".", end="")
    time.sleep(interval)
    if end == True:
        print("")

global name
name = ""

# iF nAmE eQuAlS mAiN as;dogaslxkdfm
system("clear")
time.sleep(2)
print(c.OKCYAN + "ENTERING SERVER", end="")
dotcycle(0.2, False)
time.sleep(1.8)
print(c.WARNING+" NEED AUTHENTICATION"+c.ENDC)
time.sleep(0.5)

def command(g):
    args = str.split(g, " ")
    com = args[0]
    if com == "smash":
        name = args[1]
        if random.randint(0, 10) > 6: # user exists
            time.sleep(1)
            print(c.OKCYAN+"locating user "+name+"@skynet", end="")
            dotcycle(0.4, True)
            time.sleep(4)
            print(c.WARNING+"sending terminal SMASH packets", end="")
            time.sleep(0.5)
            dotcycle(0.4, False)
            print(c.OKGREEN+" OK"+c.ENDC)
            time.sleep(1)
            print(c.WARNING+"sending falsy EXIF data", end="")
            time.sleep(0.8)
            dotcycle(0.4, False)
            print(c.OKGREEN+" OK"+c.ENDC)
            time.sleep(1.5)
            print(c.WARNING+"decrypting firewalls", end="")
            time.sleep(0.2)
            dotcycle(0.5, False)
            print(c.OKGREEN+" OK"+c.ENDC)
            time.sleep(1)
            print(c.WARNING+"breaching postgresql gateway", end="")
            time.sleep(1.2)
            dotcycle(0.4, False)
            print(c.OKGREEN+" OK"+c.ENDC)
            time.sleep(2)
            print(c.FAIL+"sending final firewall configurations", end="")
            time.sleep(0.4)
            dotcycle(0.4, False)
            time.sleep(2.5)
            print(c.OKBLUE+"SENT", end="")
            time.sleep(1)
            dotcycle(0.5, False)
            time.sleep(1.5)
            print(c.OKCYAN+"RECEIVED")
            time.sleep(2)
            print(c.WARNING+"SMASHv2 uploaded to target "+c.HEADER+name+"@skynet"+c.OKGREEN+" SUCCESS"+c.ENDC)
            time.sleep(2)
            command(input(config["uname"]+"~ "))
        else: # no
            time.sleep(1)
            print(c.OKCYAN+"locating user "+name+"@skynet", end="")
            dotcycle(0.4, True)
            time.sleep(0.8)
            print(c.WARNING+"cannot find user - "+c.BOLD+"are they reachable? check your internet connection or ask them if they're online"+c.ENDC)
            command(input(config["uname"]+"~ "))
    elif com == "logout" or com == "exit":
        # no args
        time.sleep(1)
        print(c.OKCYAN+"LEAVING SERVER", end="")
        time.sleep(1.5)
        dotcycle(0.4, False)
        time.sleep(1)
        print(c.HEADER+" logged out "+c.OKGREEN+config["uname"]+c.ENDC)
        time.sleep(2)
        exit()
    elif com == "find":
        if args[1] == config["uname"]:
            print(c.OKCYAN+"locating user "+args[1]+"@skynet", end="")
            dotcycle(0.8, True)
            print(f"{c.FAIL}command find |{c.WARNING} cannot {c.HEADER}FIND{c.WARNING} current user")
            command(input(config["uname"]+"~ "))
        else:
            print(c.OKCYAN+"locating user "+args[1]+"@skynet", end="")
            dotcycle(0.8, True)
            print(f"{c.OKBLUE}fetching metadata")
            dotcycle(0.2, False)
            dotcycle(0.2, False)
            dotcycle(0.2, False)
            dotcycle(0.2, False)
            dotcycle(0.2, False)
            dotcycle(0.2, False)
            print(f"{c.OKGREEN}OK{c.ENDC}")
            sleeptime = random.random()*1+random.random()
            sleeptime = round(sleeptime*50)/10
            time.sleep(sleeptime)
            j = random.randint(0, 10)
            if j > 7:
                reasons = ["user unavailable", "user not found", "bad connection", "authentication failed", "does not exist", "cannot access database"]
                print(f'{c.FAIL} cannot find user {args[1]}: {reasons[random.randint(0, len(reasons)-1)]} {c.ENDC}')
                time.sleep(1)
            else:
                prefix = f"{c.OKCYAN}user {args[1]} |"
                startdate = datetime.date(2008, 8, 14)
                enddate = datetime.date.today()
                delta = (enddate - startdate).days
                randomdays = random.randrange(delta)
                created = startdate + datetime.timedelta(days=randomdays)
                delta = (enddate - created).days
                randomdays = random.randrange(delta)
                lastactive = created + datetime.timedelta(days=randomdays)
                print(f"{prefix} {c.HEADER}found after {sleeptime}s : {c.ENDC}")
                print(f"{prefix} {c.WARNING}userid {random.randint(6875394, 5682479183)}")
                print(f"{prefix} {c.OKBLUE}created {created}")
                print(f"{prefix} {c.OKBLUE}last active {lastactive}")
                print(f"{prefix} {c.OKBLUE}latency {random.randint(20, 400)}ms{c.ENDC}")
                # print(f"{prefix} {c.OKBLUE}")
            command(input(config["uname"]+"~ "))
    elif com == "clear":
        system("clear")
        command(input(config["uname"]+"~ "))
    elif com == "help":
        time.sleep(1)
        print(f"""< << <<< skynet help menu >>> >> >
{c.OKCYAN}find{c.ENDC}   : finds users and their metadata
{c.OKCYAN}logout{c.ENDC} : logs user out and sends {c.FAIL}SIGTERM{c.ENDC}
{c.OKCYAN}smash{c.ENDC}  : uploads {c.HEADER}SMASHv2{c.ENDC} bug to target. only to be used in extreme circumstances""")
        command(input(config["uname"]+"~ "))
    else:
        time.sleep(1)
        print(c.WARNING+"COMMAND "+g.upper()+" NOT FOUND"+c.OKBLUE+" ("+config["uname"]+"@skynet)"+c.ENDC)
        time.sleep(1)
        command(input(config["uname"]+"~ "))


def password(p): # dammit i like javascript's function smashing where they all go to the top of the file
    if p in config.get("names"):
        time.sleep(random.randint(2, 4))
        system("clear")
        time.sleep(random.randint(1, 3))
        print(c.OKGREEN+"WELCOME TO SKYNET"+c.ENDC)
        config["uname"] = p
        time.sleep(1.5)
        command(input(p+"~ "))
    else:
        time.sleep(random.randint(1, 4))
        print(c.FAIL+"could not be identified, try again"+c.ENDC)
        password(input("~ "))

try:
    password(input("~ "))
except KeyboardInterrupt:
    time.sleep(1)
    print(c.FAIL+"\nforced logout: "+c.HEADER+config["uname"]+"@skynet")
    time.sleep(0.5)
    exit()