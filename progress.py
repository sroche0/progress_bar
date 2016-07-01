import sys


class Bar:
    def __init__(self, total):
        self.done = 0
        self.total = total
        print '\n|0 {} 50 {} 100|'.format('-' * 15, '-' * 15)
        sys.stdout.write('|')

    def update(self, current):
        status = int(float(current) / float(self.total) * 40)
        if status != self.done:
            sys.stdout.write('#' * (status - self.done))
            sys.stdout.flush()
            self.done = status

        if current + 1 == self.total:
            print '{}|\n'.format('#' * (40 - self.done))
