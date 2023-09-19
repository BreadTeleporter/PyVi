userMessage = ""
lines = []
while True:
    # Bad screen clearing code. TODO: Dont.
    for i in range(0, 255):
        print("")
    #print(lines)
    for i in range(len(lines)):
        if lines[i] != "":
            print(f"{i} {lines[i]}")
    #if userMessage != "":
    #    print(userMessage)
    command = input("> ")
    userMessage == ""
    if command.split(" ", maxsplit=2)[0] == ":i":
        try:
            lines[int(command.split(" ", maxsplit=2)[1])] = command.split(" ", maxsplit=2)[2]
        except:
            try:
                lines.insert(int(command.split(" ", maxsplit=2)[1]), command.split(" ", maxsplit=2)[2])
            except:
                userMessage = "Failed to insert string. Did you specify a location?"
    elif command.split(" ", maxsplit=2)[0] == ":a":
        try:
            lines.insert(int(command.split(" ", maxsplit=2)[1]), command.split(" ", maxsplit=2)[2])
        except:
            userMessage = "Failed to insert string. Did you specify a location?"
    elif command.split(" ", maxsplit=2)[0] == ":c":
        lines[int(command.split(" ", maxsplit=2)[1])] = ""
    elif command.split(" ", maxsplit=2)[0] == ":o":
        try:
            with open(command.split(" ", maxsplit=2)[1], "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace("\n", "")
        except:
            userMessage = "Failed to open file."
    elif command.split(" ", maxsplit=2)[0] == ":w":
        try:
            with open(command.split(" ", maxsplit=2)[1], "w") as f:
                for i in range(len(lines)):
                    f.write(lines[i] + "\n")
        except:
            userMessage = "Failed to save file. Did you specify a filename?"
    elif command.split(" ", maxsplit=2)[0] == ":n":
        sure = input("Are you sure? (Y/N) ")
        if sure == "y" or sure == "Y":
            lines = []
    elif command.split(" ", maxsplit=2)[0] == ":q":
        exit()
