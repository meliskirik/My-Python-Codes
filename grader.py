def grader(hw1, hw2, hw3, midterm, final):
    return (((hw1 + hw2 + hw3) / 3) * 0.2) + (midterm * 0.3) + (final * 0.5)

def letter(g, f):
    if f >= 40:
        if g >= 90:
            return "AA"
        elif g >=85:
            return "BA"
        elif g >= 80:
            return "BB"
        elif g >= 50:
            return "CC"
    else:
        return "FF"
fnl = 55
grade = grader(30, 90, 40, 100, fnl)
print(grade, letter(grade, fnl))