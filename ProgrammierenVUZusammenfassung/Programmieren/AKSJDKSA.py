class Geschlecht:
    
    def __init__(self,gender):
        self.gender = gender
    
    def testgender(self):
        if self.gender == "m":
            return "Sehr geehrter Herr"
        else:
            return "Sehr geehrte Frau"

if __name__ == "__main__":
    
    try:
        name = input("Input name: ")
        geschlecht = input("Gender[m/f] ").lower()
        if geschlecht != "m" or geschlecht != "f":
            raise ValueError
    except ValueError:
        print("input correct gender")
        geschlecht = input("Gender[m/f] ").lower()

    print(f"{Geschlecht(geschlecht).testgender()} {name}")
    asd = [["1","2"]]

    asd.remove(asd[0][0])
