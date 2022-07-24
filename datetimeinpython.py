from datetime import *
import time
d=datetime.now()
print(d)

print(d.strftime("%H"))

for i in range(10):
    time.sleep(1)
    print(i)