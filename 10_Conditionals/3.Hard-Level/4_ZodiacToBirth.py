# Determine zodiac sign based on birth date
# Expectational & does not have interest in it

month = int(input("Enter birth month (1-12): "))
day = int(input("Enter birth day: "))

zodiac = [
    ("Capricorn", 20),
    ("Aquarius", 19),
    ("Pisces", 20),
    ("Aries", 20),
    ("Taurus", 21),
    ("Gemini", 21),
    ("Cancer", 22),
    ("Leo", 22),
    ("virgo", 22),
    ("Libra", 23),
    ("Scorpio", 23),
    ("Sagittarius", 22),
    ("Capricorn", 31)
]

sign = zodiac[month - 1][0] if day <= zodiac[month - 1][1] else zodiac[month][0]

print("Zodiac Sign: ", sign)