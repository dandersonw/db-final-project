class Status():
    def __init__(self, id):
        self.id = id
        assert id in range(1, 5)

    names = {1: '',
             2: 'Want to Read',
             3: 'Reading',
             4: 'Read'}

    def __str__(self):
        return Status.names[self.id]


UNSET = Status(1)
WANT_TO_READ = Status(2)
READING = Status(3)
READ = Status(4)
