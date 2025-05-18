import re
import math

# Simple dictionary words to avoid
common_words = ['password', '123456', 'admin', 'letmein', 'qwerty']

# Function to calculate password entropy
def calculate_entropy(password):
    pool = 0
    if re.search(r'[a-z]', password): pool += 26
    if re.search(r'[A-Z]', password): pool += 26
    if re.search(r'\d', password): pool += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): pool += 32
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 2)

# Main strength check function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short (min 8 characters)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add digits")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters")

    if any(word in password.lower() for word in common_words):
        feedback.append("⚠️ Avoid common words like 'password' or 'admin'")

    entropy = calculate_entropy(password)
    feedback.append(f"🔢 Entropy: {entropy} bits")

    if score <= 2:
        feedback.insert(0, "🔴 Weak password")
    elif score == 3 or score == 4:
        feedback.insert(0, "🟠 Moderate password")
    else:
        feedback.insert(0, "🟢 Strong password")

    return feedback

# Run checker
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)
    print("\n".join(result))
