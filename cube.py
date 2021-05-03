def volume(side):
    return(side**3)

def getSide():
    side = input("Enter the side length: ")
    if (not side.isdigit()):
        return getSide()
    return int(side)

def main():
    print(volume(getSide()))

if __name__ == "__main__":
    main()
