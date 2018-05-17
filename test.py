import progress
import time


total = 22
bar = progress.Bar(total, 45)

for i in range(total):
    bar.update(i)
    time.sleep(1)
