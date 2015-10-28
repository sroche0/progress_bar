import sys


class Bar:
    def __init__(self, total):
        self.last = 0
        self.done = 0
        self.total = total
        print '\n{}{}    Progress    {}{}'.format(' ' * 10, '*' * 20, '*' * 20, ' ' * 10)
        print
        print ' 0% {} 25% {} 50% {} 75% {} 100%'.format(' ' * 13, ' ' * 14, ' ' * 14, ' ' * 11)
        print '-' * 77, '\n[',

    def update(self, current):
        status = float(current) / float(self.total) * 100 * .75
        if int(status) != self.last:
            if self.total >= 100:
                sys.stdout.write('#')
                sys.stdout.flush()
            else:
                progress = int(75 * (float(current) / float(self.total)))
                sys.stdout.write('#' * (progress - self.done))
                sys.stdout.flush()
                self.done = progress
                
            self.last = int(status)

        if current + 1 == self.total:
            print '#' * (75 - self.done), ']'
