
# Format date like “Monday, 22 June 2025”
import datetime
a = datetime.datetime(2025, 6, 22)
y = a.strftime('%A')
print(a, y)
