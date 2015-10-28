import sys


class Bar:
    def __init__(self, total):
        self.last = 0
        self.total = total
        print '{}    Progress    {}'.format('*' * 30, '*' * 30)
        print ' 0% {} 25% {} 50% {} 75% {} 100%\n['.format('-' * 13, '-' * 14, '-' * 14, '-' * 11),

    def update(self, current):
        status = int(float(current) / float(self.total) * 100 * .75)
        # print status
        # if status % 100 == 0:
        if status != self.last:
            sys.stdout.write('#')
            sys.stdout.flush()
            self.last = int(status)

        if current + 1 == self.total:
            print '#]'
