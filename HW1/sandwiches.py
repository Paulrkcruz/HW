# TEST CASE #1
# bread = 100, cheese = 109, ham = 105 =>
# 20 sandwiches, leftover bread = 66, leftover cheese = 58, leftover ham = 3
# TEST CASE #2
# bread = 4000, cheese = 5000, ham = 6000 =>
# 1000 sandwiches, leftover bread = 2064, 
# leftover cheese = 2096, leftover ham = 193
# TEST CASE #3
# bread = 40, cheese = 50, ham = 80 =>
# 0 sandwiches, leftover bread = 14, leftover cheese = 11, leftover ham = 2


def main():
    print("Welcome to the Robo Sandwhich Maker!")
    bread_sw = int(input("How many slices of bread do you have?"))
    bread_swstotal = bread_sw / 2
    print(("Great! I can make", int(bread_swstotal), "sandwhiche(s) with",
    bread_sw, "slices of bread!"))
    bread_swcheese = int(input("How many slices of cheese do you have?"))
    bread_cheesetotal = bread_swcheese  / 3
    print(("Wonderful! I can make", int(bread_cheesetotal), "sandwhiche(s) with", 
    bread_swcheese, "slices of cheese!"))
    bread_swham = int(input("How many slices of ham do you have?"))
    bread_fullswtotal = bread_swham / 6.2
    print("I can make", int(bread_fullswtotal), "sandwhiche(s) with these ingredients!")
    print("You`ve got", int(bread_fullswtotal), "sandwhiche(s) coming right up!")
    bread_slices_lo = int(bread_sw - (bread_fullswtotal * 2))
    cheese_slices_lo = int((bread_swcheese - bread_fullswtotal * 3)) 
    ham_slices_lo = int(bread_swham - bread_fullswtotal * 6)
    print("Leftover ingredients: bread slices:", bread_slices_lo, ", Cheese slices:", cheese_slices_lo, ", ham slices:", ham_slices_lo)


main()