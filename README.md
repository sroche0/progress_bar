# progress_bar

Creates a progress bar object. Width can be manually defined if desired. Default behavior will use the full width of the terminal for the progress bar. You instance this outside your loop with the total number of items you expect to process in the loop. Inside the loop you would track how many items you've processed and call update(). The # of items processed can be cached and passed every X iterations, you don't need to call update() on every loop
```
:param total: Total number of items expected
:type total: int
:param width: Desired width of the progress bar, minimum of 20 chars long. Default is full screen.
:type width: int
```
## Samples
### Basic usage
```
from progress import Bar
import time


total = 22
progress_bar = Bar(total, 45)
for i in range(total):
    progress_bar.update(i)
    time.sleep(1)
```

### With iteration caching
```
from progress import Bar
import time


total = 2137
progress_bar = Bar(total, 45)
for i in range(total):
    if i % 100 == 0 or i == total: 
        # Some tasks will have hundreds of thousands or even millions of iterations. 
        # Even at its widest a single iteration of the loop is unlikely to add any visible progress. 
        # In those cases only calling .update() every 100 or 1000 iterations can save a lot of 
        # cpu time and improve the script runtime
        progress_bar.update(i)
    time.sleep(1)
progress_bar.update(total)

# If you're caching results, be sure to check if the number iteration you're on is the last one 
# or call a final update() outside the loop. It's most likely that the number of items you need 
# to process is not a nice round number like 2000 and the final update call will leave off the 
# last X number of iterations, potentially leaving you with an incomplete progress bar
```

### Output
```
0 --------|---------|---------|---------- 100
##########################
```
