
def vacuum_agent(location, status_A, status_B):
    if location == "A" and status_A == "Dirty":
        return "SUCK"
    elif location == "B" and status_B == "Dirty":
        return "SUCK"
    elif status_A == "Dirty":
        return "LEFT"
    elif status_B == "Dirty":
        return "RIGHT"
    else:
        return "NO-OP"


def vacuum_simulation(location, status_A, status_B):
    while True:
        action = vacuum_agent(location, status_A, status_B)

        if action == "NO-OP":
            break

        print(action)

        if action == "SUCK" and location == "A":
            status_A = "Clean"
        elif action == "SUCK" and location == "B":
            status_B = "Clean"
        elif action == "LEFT":
            location = "A"
        elif action == "RIGHT":
            location = "B"

    print("Final Location:", location)
    print("Room A:", status_A)
    print("Room B:", status_B)


location = input("Initial Location: ").strip().upper()
status_A = input("Room A: ").strip().capitalize()
status_B = input("Room B: ").strip().capitalize()

vacuum_simulation(location, status_A, status_B)
