
def problem():
    while True:
        question=input("What is your device problem?:").lower()
        if "smashed" in question or "broke" in question or "screen" in question:
            print("")
            file=open("solutions_list.txt","r")
            print(file.readlines()[0])
            break
        elif "water" in question or "wet" in question or "drenched" in question:
            print("")
            file=open("solutions_list.txt","r")
            print(file.readlines()[1])
            break
        elif "wi-fi" in question or "weak signal" in question or "connection" in question:
            print("")
            file=open("solutions_list.txt","r")
            print(file.readlines()[2])
            break
        elif "storage" in question or "full" in question or "Space" in question:
            print("")
            file=open("solutions_list.txt","r")
            print(file.readlines()[3])
            break
        elif "charging" in question or "dead" in question or "broken pin" in question:
            print("")
            file=open("solutions_list.txt","r")
            print(file.readlines()[4])
            break
problem()

