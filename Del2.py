
def main():
    running = True
    while running:
        print("Skriv [1] för att lägga till en bok \n [2] för att få alla böcker och deras information")
        userInput = input()

        if userInput == "1":
            print("Skriv namnet på boken du vill lägga till")
            name = input()
            print("Skriv namnet på författarn nu")
            print("Skriv antal sidor på boken")
            print("Skriv priset på boken")









#class

class Bok:    
    def __init__(self, title):
        self.Title = title
        self.Author = "N/A"
        self.pageCount = "N/A"
        self.Price = "N/A"
    
    def SetAuthor(self, author):
        self.Author = author
    def SetPageCount(self, pageCount):
        self.pageCount = pageCount
    def SetPrice(self, price):
        self.Price = price

main()