from tkinter import *

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("Application Name")

        self.label = Label(master, text="Welcome to \" Application Name \" ")
        self.label.pack()

        self.add_book_button = Button(master, text="Add Book", command=self.addBook)
        self.add_book_button.pack()

        self.series_sort_button = Button(master, text="Sort By Series", command=self.series)
        self.series_sort_button.pack()

        self.reading_sort_button = Button(master, text="Sort By Reading List", command=self.chronological)
        self.reading_sort_button.pack()

        self.rating_sort_button = Button(master, text="Sort By Rating", command=self.rating)
        self.rating_sort_button.pack()

        self.books_button = Button(master, text="Books", command=self.books)
        self.books_button.pack()

        self.reviews_button = Button(master, text="Reviews", command=self.reviews)
        self.reviews_button.pack()

        self.remove_book_button = Button(master, text="Remove Book", command=self.remove)
        self.remove_book_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.book_list = Listbox(root)
        # self.book_list.insert(...)
        self.book_list.pack()

    def addBook(self):
        """
        Connect to backend for adding book
        """
        add_book_window = Toplevel()
        add_book_window.title("Add a Book!")

        book_name_label = Label(add_book_window, text = "Book Name *")
        book_name_label.pack()

        book_name_text = Text(add_book_window, width = 30, height = 1)
        book_name_text.pack()

        date_started_label = Label(add_book_window, text="Date Started *")
        date_started_label.pack()

        date_started_text = Text(add_book_window, width = 30, height = 1)
        date_started_text.pack()

        data_ended_label = Label(add_book_window, text="Date Completed")
        data_ended_label.pack()

        date_ended_text = Text(add_book_window, width=30, height=1)
        date_ended_text.pack()

        rating_label = Label(add_book_window, text="Rating")
        rating_label.pack()

        rating_text = Text(add_book_window, width=30, height=1)
        rating_text.pack()

        review_label = Label(add_book_window, text="Review")
        review_label.pack()

        review_text = Text(add_book_window, width=30, height=1)
        review_text.pack()

        add_book_button = Button(add_book_window, text = "Add Book")
        add_book_button.pack()

        add_book_window.geometry("750x750")

    def series(self):
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
        print("Book Removed")
        """
        Connect to backend for adding book
        """

root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("750x750")
root.mainloop()