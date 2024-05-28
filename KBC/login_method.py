#login Function/method
def login(log = 1):
    con = input("You are Ready for the game Yes/NO ")
    if ((con == "Yes")or(con == "yes")or(con == "y")or(con == "Y")):
        return True
    elif(log == 3):
        print("retry after long time")
    else:
        print("Retry again")
        log = log + 1
        return login(log)


if __name__ == "__main__":
    login()
