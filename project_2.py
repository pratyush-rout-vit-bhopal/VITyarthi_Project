import numpy as np
import matplotlib.pyplot as plt
print("\nWeekly Savings Tracker\n")
name = input("name: ").strip()
if name == "":
    name = "User"
while True:
    s = input("savings target: ").strip()
    try:
        target = float(s)
        break
    except:
        print("enter number")
while True:
    s = input("starting money: ").strip()
    try:
        start = float(s)
        break
    except:
        print("enter number")
print("\nenter amounts for each week:")
print("positive = income")
print("negative = expense\n")
while True:
    n_in = input("how many weeks? [4]: ").strip()
    if n_in == "":
        n = 4
        break
    try:
        n = int(n_in)
        if n > 0:
            break
    except:
        print("enter whole number")
vals = []
for i in range(1, n+1):
    while True:
        v = input("week " + str(i) + " amount: ").strip()
        try:
            vals.append(float(v))
            break
        except:
            print("enter number")
arr = np.array(vals, float)
exp = np.where(arr < 0, -arr, 0)
cum = np.cumsum(exp)
rem = start - cum
print("\nstarting money =", start)
for i in range(len(rem)):
    r = rem[i]
    if i == 0:
        note = ""
    else:
        if rem[i] > rem[i-1]:
            note = " (more saved)"
        elif rem[i] < rem[i-1]:
            note = " (less saved)"
        else:
            note = " (same)"
    print("week", i+1, "remaining =", r, note)
if rem[-1] < target:
    print("\nWARNING: remaining", rem[-1], "below target", target)
    for i in range(len(rem)):
        if rem[i] < target:
            print("first below target at week", i+1)
            break
else:
    print("\nOK: remaining", rem[-1], ">= target", target)
x = np.arange(1, n+1)
plt.figure(figsize=(8,4))
plt.plot(x, arr, "-o")
plt.xticks(x, ["W"+str(i) for i in x], rotation=30)
plt.title("Weekly Net Amount (income +, expense -)")
plt.xlabel("week")
plt.ylabel("net amount")
plt.grid(alpha=0.3)
plt.plot(x, rem, "-s")
plt.axhline(y=target, color="green", linestyle="--")
plt.legend(["net", "remaining", "target"])
print("\nclose graph window to finish")
plt.tight_layout()
plt.show()