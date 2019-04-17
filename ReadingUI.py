from tkinter import *
from PIL import ImageTk, Image

import readinglist

conn = readinglist.db.engine.connect()

class ReadingListUI:

    series_list = readinglist.series.list_series(conn)

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

        self.list_books()

    def list_books(self):
        self.book_list.delete(0)
        self.books = readinglist.book.list_books(conn)
        for b in self.books:
            b.attach_joined_attributes(conn)
        headers = ["title", "status", "series", "rating"] #Test set

        row_format = "{:<8}  {:>8}  {:<8}  {:8}"
        self.book_list.insert(0, row_format.format(*headers, sp=" " * 2))
        for book in self.books:
            items = (book.title,
                     str(book.status),
                     book.series.series_name if book.series is not None else '',
                     book.review.rating if book.review is not None else '')
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

        add_book_button = Button(add_book_window,
                                 text = "Add Book",
                                 command=self._add_book_hook(add_book_window, book_name_text))
        #Add book to backend
        add_book_button.place(x = 475, y = 260)

        add_book_window.geometry("1000x1000")

    def _add_book_hook(self, window, book_name_text):
        def result():
            title = book_name_text.get("1.0", END).strip()
            readinglist.book.insert_book(conn,
                                         title,
                                         [],
                                         readinglist.reading_status.UNSET)
            window.destroy()
            self.list_books()
        return result

    def series(self):

        self.series_list.sort(key=lambda s: s.series_name)

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
        book = self.books[current_selection[0] - 1]
        readinglist.book.delete_book(conn, book)
        # Connect to Database

root = Tk()
reading_gui = ReadingListUI(root)
root.geometry("1000x1000")
root.mainloop()
