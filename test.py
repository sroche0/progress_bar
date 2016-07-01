import progress
import time


total = 10
bar = progress.Bar(total)

for i in range(total):
    bar.update(i)
    time.sleep(1)
