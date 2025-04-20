
def main():
    running = True
    Booklist = []
    while running:
        print("Skriv [1] för att lägga till en bok \n [2] för att få alla böcker och deras information")
        userInput = input()
        if userInput == "1":
            Booklist.append(Addbook())
            print(Booklist)

def Addbook():
    print("Skriv namnet på boken du vill lägga till, eller inget ifall du vill gå tillbaka")
    Title = input()
    if not ChoiceIsEmpty(Title):
        newBook = Book(Title)
    else:
        return
    
    success = False #Det känns som jag kan göra detta bättre på något sätt
    while success == False:
        print("Skriv namnet på författarn nu, Eller inget ifall du inte vet")
        Author = input()
        if ConfirmChoice("författarn",Author) == False:
            continue
        if not ChoiceIsEmpty(Author):
            newBook.SetAuthor(Author) 
            success = True
        else:
            success = True
            
    success = False
    while success == False:
        print("Skriv antal sidor på boken, Eller inget ifall du inte vet")
        pageCount = input()
        if ConfirmChoice("sid antalet",pageCount) == False:
            continue
        if not ChoiceIsEmpty(pageCount) and CanPassToNumber(pageCount):
            newBook.SetPageCount(pageCount) 
            success = True
        else:
            success = True
    
    success = False
    while success == False:
        print("Skriv priset på boken, Eller inget ifall du inte vet")
        Price = input()
        if ConfirmChoice("priset",Price) == False:
            continue
        if CanPassToNumber(Price) and not ChoiceIsEmpty(Price):
            newBook.SetPageCount(Price) 
            success = True
        else:
            success = True
    return newBook

def ConfirmChoice(question, choice):
    selecting = True
    while selecting == True:
        print(f"är du säker att {question} ska vara : {choice} \n Skriv [J] för ja och [N] för Nej")
        Choice = input()
        if Choice == "J":
            return True
        if Choice == "N":
            return False
        
def ChoiceIsEmpty(choice):
    return choice == ""
def CanPassToNumber(thingtotrytoparse):
    try:
        int(thingtotrytoparse)
        return True
    except:
        print("Det du skrev är ej ett nummer")
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