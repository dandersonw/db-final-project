from tkinter import *
from PIL import ImageTk, Image

class ReadingListUI:

    series_list = ["A", "B", "D", "Aa", "Ab"] #Feed series column from database here, else, SQL SELECT statement for sort

    def __init__(self, master):
        self.master = master
        master.title("ManageMe")

        bardImg = "ReadingLogo.png"
        bard = Image.open(bardImg)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(master, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)



        self.label = Label(master, text="Welcome to ManageMe ")
        self.label.config(font = ("Comic Sans", 44))
        self.label.place(x = 300, y = 100)

        self.add_book_button = Button(master, text="Add Book", command=self.addBook)
        self.add_book_button.place(x = 450, y = 150)

        self.series_sort_button = Button(master, text="Sort By Series", command=self.series)
        self.series_sort_button.place(x = 350, y = 200)

        self.reading_sort_button = Button(master, text="Sort By Reading List", command=self.chronological)
        self.reading_sort_button.place(x = 500, y = 200)

        self.rating_sort_button = Button(master, text="Sort By Rating", command=self.rating)
        self.rating_sort_button.place(x = 350, y = 250)

        self.books_button = Button(master, text="Books", command=self.books)
        self.books_button.place(x = 500, y = 250)

        self.reviews_button = Button(master, text="Reviews", command=self.reviews)
        self.reviews_button.place(x = 350, y = 300)

        self.remove_book_button = Button(master, text="Remove Book", command=self.remove)
        self.remove_book_button.place(x = 500, y = 300)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x = 450, y = 350)

        self.book_list = Listbox(root, width = 75, height = 10)
        scroll = Scrollbar(root, command = self.book_list.yview)#----

        self.book_list.configure(yscrollcommand = scroll.set)#----

        self.book_list.place(x = 150, y = 450)
        scroll.pack(side=RIGHT, fill=Y) #----

        table = [["spam", 42, "test", ""], ["eggs", 451, "", "we"], ["bacon", "True", "", ""]]
        headers = ["item", "qty", "sd", "again"] #Test set

        row_format = "{:<8}  {:>8}  {:<8}  {:8}"
        self.book_list.insert(0, row_format.format(*headers, sp=" " * 2))
        for items in table:
            self.book_list.insert(END, row_format.format(*items, sp=" " * 2))

    def addBook(self):
        """
        Connect to backend for adding book
        """
        add_book_window = Toplevel()
        add_book_window.title("Add a Book!")

        bardImg = "ReadingLogo.png"
        bard = Image.open(bardImg)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(add_book_window, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)

        ABlabel = Label(add_book_window, text="Add a Book!")
        ABlabel.config(font = ("Comic Sans", 44))
        ABlabel.place(x = 350, y = 5)

        book_name_label = Label(add_book_window, text = "Book Name *")
        book_name_label.place(x = 400, y = 60)

        book_name_text = Text(add_book_window, width = 30, height = 1)
        book_name_text.place(x = 550, y = 60)

        #Add book to list, text not visible, but, row added
        input = book_name_text.get("1.0", END)
        self.book_list.insert(END, input)

        date_started_label = Label(add_book_window, text    ="Date Started *")
        date_started_label.place(x = 400, y = 100)

        date_started_text = Text(add_book_window, width = 30, height = 1)
        date_started_text.place(x = 550, y = 100)

        data_ended_label = Label(add_book_window, text="Date Completed")
        data_ended_label.place(x = 400, y = 140)

        date_ended_text = Text(add_book_window, width=30, height=1)
        date_ended_text.place(x = 550, y = 140)

        rating_label = Label(add_book_window, text="Rating")
        rating_label.place(x = 400, y = 180)

        rating_text = Text(add_book_window, width=30, height=1)
        rating_text.place(x = 550, y = 180)

        review_label = Label(add_book_window, text="Review")
        review_label.place(x = 400, y = 220)

        review_text = Text(add_book_window, width=30, height=1)
        review_text.place(x = 550, y = 220)

        add_book_button = Button(add_book_window, text = "Add Book", command = add_book_window.destroy)
        #Add book to backend
        add_book_button.place(x = 475, y = 260)

        add_book_window.geometry("1000x1000")

    def series(self):

        self.series_list.sort()

        print("Series Sort!")
        """
        Connect to backend for adding book
        """

    def chronological(self):
        print("Chronological(default) sort!")
        """
        Connect to backend for adding book
        """

    def rating(self):
        print("Rating sort!")
        """
        Connect to backend for adding book
        """

    def books(self):
        print("Books list!")
        """
        Connect to backend for adding book
        """

    def reviews(self):
        print("Books + Reviews List!")
        """
        Connect to backend for adding book
        """
    def remove(self):
        current_selection = self.book_list.curselection()
        self.book_list.delete(current_selection)
        # Connect to Database

root = Tk()
reading_gui = ReadingListUI(root)
root.geometry("1000x1000")
root.mainloop()