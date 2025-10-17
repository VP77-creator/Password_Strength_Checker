import re
from tkinter import *
from tkinter import ttk

# Function to check password strength using induction steps
def check_strength_induction(password):
    steps = []
    score = 0

    # Base Case
    if len(password) >= 1:
        steps.append("✅ Base Case: Password exists.")
    else:
        steps.append("❌ Base Case Failed: Empty password.")
        return "Weak", "red", steps, 0

    # Inductive Steps
    # Step 1: Length
    if len(password) >= 8:
        score += 1
        steps.append("✅ Step 1: Length ≥ 8 proven.")
    else:
        steps.append("❌ Step 1: Length < 8. Induction fails here.")

    # Step 2: Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
        steps.append("✅ Step 2: Contains uppercase letter.")
    else:
        steps.append("❌ Step 2: Missing uppercase letter.")

    # Step 3: Lowercase
    if re.search(r"[a-z]", password):
        score += 1
        steps.append("✅ Step 3: Contains lowercase letter.")
    else:
        steps.append("❌ Step 3: Missing lowercase letter.")

    # Step 4: Digit
    if re.search(r"\d", password):
        score += 1
        steps.append("✅ Step 4: Contains digit.")
    else:
        steps.append("❌ Step 4: Missing digit.")

    # Step 5: Special character
    if re.search(r"[@$!%*#?&]", password):
        score += 1
        steps.append("✅ Step 5: Contains special character.")
    else:
        steps.append("❌ Step 5: Missing special character.")

    # Conclusion
    if score <= 2:
        strength = "Weak"
        color = "red"
        progress_value = 33
        steps.append("❌ Conclusion: Induction fails — weak password.")
    elif score == 3 or score == 4:
        strength = "Moderate"
        color = "orange"
        progress_value = 66
        steps.append("⚠ Conclusion: Partial induction — moderately strong password.")
    else:
        strength = "Strong"
        color = "green"
        progress_value = 100
        steps.append("✅ Conclusion: Proven by induction — strong password!")

    return strength, color, steps, progress_value


# Function for button click
def on_submit():
    pwd = entry.get()
    strength, color, steps, progress_value = check_strength_induction(pwd)

    result_label.config(text=f"Strength: {strength}", fg=color)
    strength_bar["value"] = progress_value
    style.configure("TProgressbar", foreground=color, background=color)

    # Display induction steps
    feedback_text.delete(1.0, END)
    feedback_text.insert(END, "\n".join(steps))


# GUI setup
root = Tk()
root.title("🔐 Password Strength Checker (Mathematical Induction Concept)")
root.geometry("480x480")
root.config(bg="#f5f5f5")

# Title
Label(root, text="Password Strength Checker (Mathematical Induction)", font=("Arial", 13, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

# Password Entry
Label(root, text="Enter your password:", bg="#f5f5f5", fg="#333", font=("Arial", 10)).pack()
entry = Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

# Button
Button(root, text="Check Strength", command=on_submit, bg="#0078D7", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=10)

# Result Label
result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f5f5f5")
result_label.pack(pady=5)

# Strength Bar
style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", thickness=20, troughcolor="#ddd", background="green")

strength_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=350, mode='determinate', style="TProgressbar")
strength_bar.pack(pady=10)

# Feedback Text Box
feedback_text = Text(root, height=10, width=55, wrap=WORD, font=("Arial", 9))
feedback_text.pack(padx=10, pady=10)

root.mainloop()