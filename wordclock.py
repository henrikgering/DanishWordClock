from ClockSimple import ClockSimple
from datetime import datetime
import time

print("Starting clock")
c = ClockSimple()
c.turn_all_off()

while True:

    now = datetime.now()
    c.UpdateClock(hour= now.hour,minute=now.minute)

    time.sleep(0.05)
