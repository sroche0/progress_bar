import sys
import subprocess


class Bar:
    def __init__(self, total, width=0):
        """
        Creates a progress bar object. Width can be manually defined if desired. Default behavior will use the width of
        the terminal for the progress bar. You instance this outside your loop with the total number of items you expect
        to process in the loop. Inside the loop you would track how many items you've processed and call update().
        # of items processed can be cached and passed every X number, you don't need to call update() on every loop

        :param total: Total number of items expected
        :type total: int
        :param width: Desired width of the progress bar, minimum of 20 chars long. Default is full screen.
        :type width: int
        """
        if width < 20:
            rows, columns = subprocess.check_output(['stty', 'size']).split()
            self.width = int(columns)
        else:
            self.width = width
        self.done = 0
        self.total = total

        q = int((self.width - self.width % 4) / 4)
        leftover = self.width % 4
        marker = '|'.ljust(q - 1)
        print('{}{}{}{}{}'.format('0'.ljust(q), marker, marker, marker, '100'.rjust(3 + leftover)))

    def update(self, current):
        status = int(float(current) / float(self.total) * self.width)
        if status != self.done:
            sys.stdout.write('#' * (status - self.done))
            sys.stdout.flush()
            self.done = status

        if current + 1 == self.total:
            print('{}\n'.format('#' * (self.width - self.done)))
