"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

import math

age = int(input("Please enter your age: "))
heart_rate = 220 - age
highest = heart_rate * 85/100
minimun = heart_rate * 65/100

print(f"""When you exercise to strengthen your heart, you should
keep your heart rate between {minimun} and {highest} beats per minute. """)
