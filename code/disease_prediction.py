# AI-Based Disease Prediction Simulation

import random

print("AI Disease Prediction System Started")

age = random.randint(18, 80)
fever = random.choice([0, 1])
cough = random.choice([0, 1])
fatigue = random.choice([0, 1])

print("Age:", age)
print("Fever:", "Yes" if fever else "No")
print("Cough:", "Yes" if cough else "No")
print("Fatigue:", "Yes" if fatigue else "No")

risk_score = 0

if age > 60:
    risk_score += 2

if fever:
    risk_score += 2

if cough:
    risk_score += 1

if fatigue:
    risk_score += 1

print("Risk Score:", risk_score)

if risk_score >= 4:
    print("Prediction: High Disease Risk")
elif risk_score >= 2:
    print("Prediction: Moderate Disease Risk")
else:
    print("Prediction: Low Disease Risk")
