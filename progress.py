import sys


class Bar:
    def __init__(self, total):
        self.last = 0
        self.total = total
        print '\n{}{}    Progress    {}{}'.format(' ' * 10, '*' * 20, '*' * 20, ' ' * 10)
        print
        print ' 0% {} 25% {} 50% {} 75% {} 100%'.format(' ' * 13, ' ' * 14, ' ' * 14, ' ' * 11)
        print '-' * 77, '\n[',

    def update(self, current):
        status = int(float(current) / float(self.total) * 100 * .75)
        # print status
        # if status % 100 == 0:
        if status != self.last:
            progress = status - self.last
            if progress > 1:
                progress = int(progress / 75 * 100)
            sys.stdout.write('#' * progress)
            sys.stdout.flush()
            self.last = int(status)

        if current + 1 == self.total:
            print '#]'
