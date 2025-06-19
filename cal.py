def add(a,b):
    return a*b

if __name__ == "__main__":
    print(add(1,2))
    print("__main__")
    print(__name__)
elif __name__ == "cal":
    print("ohayou")
    print(__name__)
else:
    print(__name__)