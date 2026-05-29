# Simple Health Risk Prediction

import random

age = random.randint(20, 70)
heart_rate = random.randint(60, 120)

print("👤 Age:", age)
print("❤️ Heart Rate:", heart_rate)

if age > 50 and heart_rate > 100:
    print("⚠️ High Health Risk Detected")
else:
    print("✅ Health Status Normal")
