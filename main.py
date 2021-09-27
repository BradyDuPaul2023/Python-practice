def define(word):
    word = word.lower()
    if word == "plane":
        return "a vehicle that can fly"
    elif word == "car":
        return "a vehicle which moves on 3-4 wheels"
    elif word == "boat":
        return "a vehicle that goes on water"
    elif word == "knife":
        return "a sharp utensil commonly used to cut stuff"
    elif word == "fork":
        return "a multi-pronged utensil commonly used to eat"
    elif word == "spoon":
        return "a utensil with a bowl shaped end commonly used for soup"
    elif word == "plate":
        return "a commonly circular flat item used to hold food"
    elif word == "bowl":
        return "an object used to commonly hold fluids"
    elif word == "spork":
        return "a groundbreaking utensil which is the combination of both a fork and a spoon"
    elif word == "keyboard":
        return "an electronic device used to input information into a computer"
    else:
        return "this word is not recognized in this dictionary"
print(define("SpoRk"))