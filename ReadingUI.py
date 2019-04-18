from tkinter import *
from PIL import ImageTk, Image

import readinglist

conn = readinglist.db.engine.connect()

class ReadingListUI:

    series_list = readinglist.series.list_series(conn)
    books_list = readinglist.book.list_books(conn)
    authors_list = readinglist.author.list_authors(conn)

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
        self.add_book_button.place(x=300, y=150)

        self.edit_book_button = Button(master, text="Edit Book", command=self.editBook)
        self.edit_book_button.place(x=400, y=150)

        self.add_series_button = Button(master, text="Add Series", command=self.addSeries)
        self.add_series_button.place(x=500, y=150)

        self.add_author_button = Button(master, text="Add Author", command=self.addAuthor)
        self.add_author_button.place(x=600, y=150)

        self.series_sort_button = Button(master, text="Sort By Series", command=self.series)
        self.series_sort_button.place(x = 350, y = 200)

        self.reading_sort_button = Button(master, text="Sort By Reading List", command=self.chronological)
        self.reading_sort_button.place(x = 500, y = 200)

        self.rating_sort_button = Button(master, text="Sort By Rating", command=self.rating)
        self.rating_sort_button.place(x = 350, y = 250)

        self.author_sort_button = Button(master, text="Sort By Author", command=self.author)
        self.author_sort_button.place(x = 500, y = 250)

        self.books_button = Button(master, text="Books", command=self.books)
        self.books_button.place(x = 350, y = 300)

        self.reviews_button = Button(master, text="Reviews", command=self.reviews)
        self.reviews_button.place(x = 500, y = 300)

        self.remove_book_button = Button(master, text="Remove Book", command=self.remove)
        self.remove_book_button.place(x = 420, y = 350)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x = 450, y = 400)

        self.book_list = Listbox(root, width = 75, height = 10)
        scroll = Scrollbar(root, command = self.book_list.yview)#----

        self.book_list.configure(yscrollcommand = scroll.set)#----

        self.book_list.place(x = 150, y = 450)
        scroll.pack(side=RIGHT, fill=Y) #----

        self.list_books()

    def list_books(self):
        self.book_list.delete(0, END)
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
        book_name_label.place(x = 400, y = 100)

        book_name_text = Text(add_book_window, width = 30, height = 1)
        book_name_text.place(x = 550, y = 100)

        input = book_name_text.get("1.0", END)
        self.book_list.insert(END, input)

        author_label = Label(add_book_window, text="Author*")
        author_label.place(x = 400, y = 140)

        author_text = Text(add_book_window, width = 30, height = 1)
        author_text.place(x = 550, y = 140)

        series_label = Label(add_book_window, text="Series")
        series_label.place(x = 400, y = 180)

        series_text = Text(add_book_window, width = 30, height = 1)
        series_text.place(x = 550, y = 180)

        date_started_label = Label(add_book_window, text="Date Started *")
        date_started_label.place(x = 400, y = 220)

        date_started_text = Text(add_book_window, width = 30, height = 1)
        date_started_text.place(x = 550, y = 220)

        data_ended_label = Label(add_book_window, text="Date Completed")
        data_ended_label.place(x = 400, y = 260)

        date_ended_text = Text(add_book_window, width=30, height=1)
        date_ended_text.place(x = 550, y = 260)

        rating_label = Label(add_book_window, text="Rating")
        rating_label.place(x = 400, y = 300)

        rating_text = Text(add_book_window, width=30, height=1)
        rating_text.place(x = 550, y = 300)

        review_label = Label(add_book_window, text="Review")
        review_label.place(x = 400, y = 340)

        review_text = Text(add_book_window, width=30, height=1)
        review_text.place(x = 550, y = 340)

        reading_status_label = Label(add_book_window, text="Reading Status")
        reading_status_label.place(x = 400, y = 380)

        reading_status_text = Text(add_book_window, width = 30, height = 1)
        reading_status_text.place(x = 550, y = 380)

        add_book_button = Button(add_book_window,
                                 text = "Add Book",
                                 command=self._add_book_hook(add_book_window,
                                                             book_name_text,
                                                             author_text,
                                                             series_text,
                                                             rating_text,
                                                             review_text,
                                                             reading_status_text))

        add_book_button.place(x = 475, y = 420)

        add_book_window.geometry("1000x1000")

    def addSeries(self):
        add_series_window = Toplevel()
        add_series_window.title("Add a Series!")

        bardImg = "ReadingLogo.png"
        bard = Image.open(bardImg)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(add_series_window, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)

        ABlabel = Label(add_series_window, text="Add a Series!")
        ABlabel.config(font=("Comic Sans", 44))
        ABlabel.place(x=350, y=5)

        series_name_label = Label(add_series_window, text="Series Name *")
        series_name_label.place(x=400, y=100)

        series_name_text = Text(add_series_window, width=30, height=1)
        series_name_text.place(x=550, y=100)

        input = series_name_text.get("1.0", END)
        self.book_list.insert(END, input)

        author_label = Label(add_series_window, text="Author*")
        author_label.place(x=400, y=140)

        author_text = Text(add_series_window, width=30, height=1)
        author_text.place(x=550, y=140)

        date_started_label = Label(add_series_window, text="Date Started *")
        date_started_label.place(x=400, y=220)

        date_started_text = Text(add_series_window, width=30, height=1)
        date_started_text.place(x=550, y=220)

        data_ended_label = Label(add_series_window, text="Date Completed")
        data_ended_label.place(x=400, y=260)

        date_ended_text = Text(add_series_window, width=30, height=1)
        date_ended_text.place(x=550, y=260)

        rating_label = Label(add_series_window, text="Rating")
        rating_label.place(x=400, y=300)

        rating_text = Text(add_series_window, width=30, height=1)
        rating_text.place(x=550, y=300)

        review_label = Label(add_series_window, text="Review")
        review_label.place(x=400, y=340)

        review_text = Text(add_series_window, width=30, height=1)
        review_text.place(x=550, y=340)

        reading_status_label = Label(add_series_window, text="Reading Status")
        reading_status_label.place(x=400, y=380)

        reading_status_text = Text(add_series_window, width=30, height=1)
        reading_status_text.place(x=550, y=380)

        add_series_button = Button(add_series_window,
                                 text="Add Series", command = self.add_series_hook(add_series_window, series_name_text,
                                                                                   author_text, rating_text, review_text,
                                                                                   reading_status_text))


        add_series_button.place(x=475, y=420)

        add_series_window.geometry("1000x1000")

    def addAuthor(self):
        add_author_window = Toplevel()
        add_author_window.title("Add a Series!")

        bardImg = "ReadingLogo.png"
        bard = Image.open(bardImg)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(add_author_window, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)

        ABlabel = Label(add_author_window, text="Add a Series!")
        ABlabel.config(font=("Comic Sans", 44))
        ABlabel.place(x=350, y=5)

        author_label = Label(add_author_window, text="Author*")
        author_label.place(x=400, y=140)

        author_text = Text(add_author_window, width=30, height=1)
        author_text.place(x=550, y=140)

        date_started_label = Label(add_author_window, text="Date Started *")
        date_started_label.place(x=400, y=220)

        date_started_text = Text(add_author_window, width=30, height=1)
        date_started_text.place(x=550, y=220)

        data_ended_label = Label(add_author_window, text="Date Completed")
        data_ended_label.place(x=400, y=260)

        date_ended_text = Text(add_author_window, width=30, height=1)
        date_ended_text.place(x=550, y=260)

        rating_label = Label(add_author_window, text="Rating")
        rating_label.place(x=400, y=300)

        rating_text = Text(add_author_window, width=30, height=1)
        rating_text.place(x=550, y=300)

        review_label = Label(add_author_window, text="Review")
        review_label.place(x=400, y=340)

        review_text = Text(add_author_window, width=30, height=1)
        review_text.place(x=550, y=340)

        reading_status_label = Label(add_author_window, text="Reading Status")
        reading_status_label.place(x=400, y=380)

        reading_status_text = Text(add_author_window, width=30, height=1)
        reading_status_text.place(x=550, y=380)

        add_author_button = Button(add_author_window,
                                 text="Add Author",
                                 command=self.add_author_hook(add_author_window, author_text, rating_text, review_text, reading_status_text))

        add_author_button.place(x=475, y=420)

        add_author_window.geometry("1000x1000")

    def _add_book_hook(self,
                       window,
                       book_name_text,
                       author_text,
                       series_text,
                       rating_text,
                       review_text,
                       reading_status_text):
        def result():
            title = book_name_text.get("1.0", END).strip()
            author_name = author_text.get("1.0", END).strip()
            if author_name:
                authors = [readinglist.author.get_author_by_name(conn, author_name)]
            else:
                authors = []
            book = readinglist.book.insert_book(conn,
                                                title,
                                                authors,
                                                readinglist.reading_status.UNSET)
            series_name = series_text.get("1.0", END).strip()
            if series_name:
                series = readinglist.series.get_series_by_name(conn, series_name)
                readinglist.book.insert_book_into_series(conn,
                                                         book,
                                                         series)
            rating = rating_text.get("1.0", END).strip()
            if rating:
                rating = float(rating_text.get("1.0", END).strip())
                review = review_text.get("1.0", END).strip()
                readinglist.book.review.insert_review(conn, book, review, rating)

            status = reading_status_text.get("1.0", END).strip()
            if status:
                status = readinglist.reading_status.Status.from_str(status)
                readinglist.book.set_book_status(conn, book, status)
            window.destroy()
            self.list_books()
        return result


    def add_series_hook(self, window, series_text, author_text, rating_text,
                       review_text,
                       reading_status_text):
        def result():
            series_name = series_text.get("1.0", END).strip()
            author_name = author_text.get("1.0", END).strip()
            readinglist.series.insert_series(conn, series_name, author_name, "")
            #####------------------
                # readinglist.series.insert_series(conn, series_name, author_text)

            # rating = rating_text.get("1.0", END).strip()
            # if rating:
            #     rating = float(rating_text.get("1.0", END).strip())
            #     review = review_text.get("1.0", END).strip()
            # status = reading_status_text.get("1.0", END).strip()
            # if status:
            #     status = readinglist.reading_status.Status.from_str(status)
            window.destroy()
            self.list_books()
        return result
    def add_author_hook(self, window, author_text, rating_text, review_text, reading_status_text):
        def result():
            author_name = author_text.get("1.0", END).strip()
            author_name = author_text.get("1.0", END).strip()
            readinglist.author.insert_author(conn, author_name)
            #####------------------

            window.destroy()
            self.list_books()

        return result

    def editBook(self):
        """
        Connect to backend for adding book
        """
        edit_book_window = Toplevel()
        edit_book_window.title("Edit a Book!")

        bardImg = "ReadingLogo.png"
        bard = Image.open(bardImg)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(edit_book_window, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=0)

        ABlabel = Label(edit_book_window, text="Edit a Book!")
        ABlabel.config(font=("Comic Sans", 44))
        ABlabel.place(x=350, y=5)

        book_name_label = Label(edit_book_window, text="Book Name *")
        book_name_label.place(x=400, y=100)

        book_name_text = Text(edit_book_window, width=30, height=1)
        book_name_text.place(x=550, y=100)

        data_ended_label = Label(edit_book_window, text="Date Completed")
        data_ended_label.place(x=400, y=140)

        date_ended_text = Text(edit_book_window, width=30, height=1)
        date_ended_text.place(x=550, y=140)

        rating_label = Label(edit_book_window, text="Rating")
        rating_label.place(x=400, y=180)

        rating_text = Text(edit_book_window, width=30, height=1)
        rating_text.place(x=550, y=180)

        review_label = Label(edit_book_window, text="Review")
        review_label.place(x=400, y=220)

        review_text = Text(edit_book_window, width=30, height=1)
        review_text.place(x=550, y=220)

        reading_status_label = Label(edit_book_window, text="Reading Status")
        reading_status_label.place(x=400, y=260)

        reading_status_text = Text(edit_book_window, width=30, height=1)
        reading_status_text.place(x=550, y=260)

        edit_book_button = Button(edit_book_window, text="Edit Book", command=edit_book_window.destroy)
        # Add book to backend
        edit_book_button.place(x=475, y=420)

        edit_book_window.geometry("1000x1000")


    def edit_book_hook(self, window, book_name_text, author_text, series_text, rating_text, review_text, reading_status_text):
        def result():
            # title = book_name_text.get("1.0", END).strip()
            # author_name = author_text.get("1.0", END).strip()
            # if author_name:
            #     authors = [readinglist.author.get_author_by_name(conn, author_name)]
            # else:
            #     authors = []
            # book = readinglist.book.set_book(conn, title, authors, readinglist.reading_status.UNSET) #Backend functionality missing - TODO DERICK
            # series_name = series_text.get("1.0", END).strip()
            # if series_name:
            # rating = rating_text.get("1.0", END).strip()
            # if rating:
            #
            # status = reading_status_text.get("1.0", END).strip()
            # if status:

            window.destroy()
            self.list_books()

        return result

    def series(self):

        self.series_list.sort(key=lambda s: s.series_name)

        print("Series Sort!")


    def chronological(self):

        self.books_list.sort(key=lambda b: b.id)

        print("Chronological(default) sort!")


    def rating(self):

        # self.books_list.sort(key=lambda r: )


        print("Rating sort!")


    def books(self):

        self.book_list.delete(0, END)
        self.books = readinglist.book.list_books(conn)
        for b in self.books:
            b.attach_joined_attributes(conn)
        headers = ["title", "status", "series", "rating"]  # Test set

        row_format = "{:<8}  {:>8}  {:<8}  {:8}"
        self.book_list.insert(0, row_format.format(*headers, sp=" " * 2))

        print("Books list!")


    def reviews(self):

        self.book_list.delete(0, END)
        self.books = readinglist.book.list_books(conn)
        for b in self.books:
            b.attach_joined_attributes(conn)
        headers = ["title", "review"] #Test set

        row_format = "{:<8} {:8}"
        self.book_list.insert(0, row_format.format(*headers, sp=" " * 2))
        for book in self.books:
            items = (book.title,
                     book.review.rating if book.review is not None else '')
            self.book_list.insert(END, row_format.format(*items, sp=" " * 2))

        print("Books + Reviews List!")

    def remove(self):
        current_selection = self.book_list.curselection()
        self.book_list.delete(current_selection)
        idx = current_selection[0] - 1
        print(idx)
        book = self.books[idx]
        # readinglist.book.delete_book(conn, book)
        readinglist.book.delete_book(conn, book)
        # Connect to Database
        
    def author(self):

        self.authors_list.sort(key=lambda a: a.author_name)

root = Tk()
reading_gui = ReadingListUI(root)
root.geometry("1000x1000")
root.mainloop()
