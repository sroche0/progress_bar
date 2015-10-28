import sys


class Bar:
    def __init__(self, total):
        self.done = 0
        self.total = total
        print '\n{}{}    Deleting    {}{}'.format(' ' * 25, '*' * 5, '*' * 5, ' ' * 25)
        print '-' * 79
        print '| 0% {} 25% {} 50% {} 75% {} 100% |'.format(' ' * 13, ' ' * 14, ' ' * 14, ' ' * 11)
        print '-' * 79, '\n[',

    def update(self, current):
        status = int(float(current) / float(self.total) * 75)
        if status != self.done:
            sys.stdout.write('#' * (status - self.done))
            sys.stdout.flush()
            self.done = status

        if current + 1 == self.total:
            print '{}{}'.format('#' * (75 - self.done), ']')
