"""The Robot Vacuum's Best Excuse — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest one-line excuse a robot vacuum gives for missing a spot, 140 characters or fewer.
"""
import os

LINE = "I didn't miss that spot. I was saving it for later, like a fine wine, or a crumb I plan to visit next Tuesday."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
