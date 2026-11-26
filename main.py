"""One-line warning label for humans, for make.fun.

The brief: the safety warning label that should come printed on every human
being, at most 160 characters, funny first and plausible second. It borrows
the register of real warning labels (WARNING, do not shake, do not feed) and
aims every clause at a recognisable human failure mode: too little sleep,
spite as fuel, and the project nobody wants to discuss.
"""

LINE = "WARNING: operates on four hours of sleep and pure spite. Do not shake. Do not feed after midnight. Never ask how the project is going."

# The entry must be exactly one line of 1-160 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, limit is 160"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
