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

    @staticmethod
    def from_id(id):
        return {1: UNSET,
                2: WANT_TO_READ,
                3: READING,
                4: READ}[id]

    @staticmethod
    def from_str(string):
        if string.lower() == 'read':
            return READ
        elif string.lower() == 'want to read':
            return WANT_TO_READ
        elif string.lower() == 'reading':
            return READING
        return UNSET


UNSET = Status(1)
WANT_TO_READ = Status(2)
READING = Status(3)
READ = Status(4)
