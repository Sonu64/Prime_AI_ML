class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews
        
    def addReview(self, review):
        self.reviews.append(review)
        
    def countReviews(self):
        return str(len(self.reviews)) + f"\n----------------------------------------------------------------------------------------"
    
    def displayAllReviews(self):
        reviewString = ""
        for review in self.reviews:
            reviewString += f"\n{review}"
        return reviewString # To avoid NoneType return
    
    def showBookDetails(self):
        print(f"Book Name: {self.title}\nBook Author: {self.author}\nBook Reviews are ---> {self.displayAllReviews()}")

myBook = Book("Byomkesh-Somogro, Part 1", "Shorodindu Bandopadhyaya", ["Sottyaneshi is probably the best Bengali Detective"])
myBook.showBookDetails()
print(f"\nTotal Reviews for {myBook.title} are {myBook.countReviews()}\n", end = "\n\n")

myBook.addReview("The best for mature readers !")
myBook.addReview("Byomkesh and Sottyoboti share a sweet Love story !")
myBook.addReview("Go for the Part-2 as well !")

myBook.showBookDetails()
print(f"\nTotal Reviews for {myBook.title} are {myBook.countReviews()}", end = "\n\n")