import turtle

def main():
    print("\n\tWelcome to Cool Designs!\n")
    print("\t1. Designs")
    print("\t2. Source Codes")
    print("\t3. Exit\n")

    choice = input("\tEnter your choice (1-3): ")

    if choice == "1":
        show_designs()
    elif choice == "2":
        show_source_codes()
    elif choice == "3":
        print("\n\tExiting...\n")
    else:
        print("\n\tInvalid choice. Please try again.\n")

def show_designs():
    turtle.speed(0)
    turtle.bgcolor("black")

    # Design 1: Spiral
    turtle.color("blue")
    for i in range(100):
        turtle.forward(i)
        turtle.right(144)

    # Design 2: Star
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.color("red")
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

    # Design 3: Circle
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.color("green")
    turtle.circle(100)

    # ... (more designs)

    turtle.done()

def show_source_codes():
    print("\n\tSource codes for the designs will be displayed here.\n")
    # ... (display source codes for each design)

if __name__ == "__main__":
    main()