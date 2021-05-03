def volume(side):
    if side < 0:
        raise Exception("NegativeSideLength")
    return(side**3)

def isInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def getSide():
    side = input("Enter the side length: ")
    if (not isInt(side)):
        return getSide()
    return int(side)

def main():
    print(volume(getSide()))

if __name__ == "__main__":
    main()
