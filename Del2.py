
def main():
    running = True
    while running:
        print("Skriv [1] för att lägga till en bok \n [2] för att få alla böcker och deras information")
        userInput = input()

        if userInput == "1":
            Addbook()

def Addbook():
    print("Skriv namnet på boken du vill lägga till, eller inget ifall du vill gå tillbaka")
    Title = input()

    newBook = Book(Title)
    
    print("Skriv namnet på författarn nu, Eller inget ifall du inte vet")
    Author = input()
    ConfirmChoice(Author)
    if Author != "":
        newBook.SetAuthor(Author)
    
    print("Skriv antal sidor på boken, Eller inget ifall du inte vet")
    pageCount = input()
    print("Skriv priset på boken, Eller inget ifall du inte vet")
    Price = input()
def ConfirmChoice(choice):
    print(f"{choice}")
def ChoiceIsEmpty():
    pass
def CheckIfCanPassToNumber(thingtotrytoparse):
    try:
        int(thingtotrytoparse)
        return True
    except:
        print("WAAAAAAAH")
        return False




#class

class Book:    
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