def problem():
    try:
        solutions = open("solutions_list.txt","r").readlines()
        while True:
            question=input("\nWhat is your device problem?:").lower()
            if "smashed" in question or "broke" in question or "screen" in question:
                print("\n"+solutions[0])
                break
            elif "water" in question or "wet" in question or "drenched" in question:
                print("\n"+solutions[1])
                break
            elif "wi-fi" in question or "weak signal" in question or "connection" in question:
                print("\n"+solutions[2])
                break
            elif "storage" in question or "full" in question or "Space" in question:
                print("\n"+solutions[3])
                break
            elif "charging" in question or "dead" in question or "broken pin" in question:
                print("\n"+solutions[4])
                break
            else:
                print("No solution found!")
                pass
    finally:
        solutions.close()  # We need to close the file :) its on finally so it will close it every time the program stops
problem()
