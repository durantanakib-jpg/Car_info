import re

units = {
    "quart": ("liter", 0.946353),
    "quarts": ("liter", 0.946353),
    "liter": ("quart", 1 / 0.946353),
    "liters": ("quart", 1 / 0.946353),

    "km": ("meter", 1000),
    "kilometer": ("meter", 1000),
    "kilometers": ("meter", 1000),
    "meter": ("km", 0.001),
    "meters": ("km", 0.001),

    "mile": ("kilometer", 1.60934),
    "miles": ("kilometer", 1.60934),
    "kilometer": ("mile", 1 / 1.60934),
    "kilometers": ("mile", 1 / 1.60934),

    "kg": ("gram", 1000),
    "kilogram": ("gram", 1000),
    "kilograms": ("gram", 1000),
    "gram": ("kg", 0.001),
    "grams": ("kg", 0.001)
}

def solve(question):
    q = question.lower()
    nums = re.findall(r"\d+\.?\d*", q)
    words = re.findall(r"[a-z]+", q)

    if not nums:
        return "No number found"

    value = float(nums[0])

    for w in words:
        if w in units:
            target, factor = units[w]
            result = value * factor
            return f"{value} {w} = {round(result, 3)} {target}s"

    return "Unit not supported"

while True:
    q = input("Ask a question (or exit): ")
    if q.lower() == "exit":
        break
    print(solve(q))
