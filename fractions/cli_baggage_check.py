import fraction
import fraction_game_model as fgame

print("Welcome to Baggage Check!\n")
model = fgame.FractionGameModel()
print("Your goal is to find all of the fractions that are over the weight limit!")
model.start_game()

while (model.num_over > 0):
    print("---------------------------------------------------------------------------")
    print("Weight Limit:", model.base_frac)
    print("Bags:", model.frac_list)
    print("There are " + str(model.num_over) + " bag(s) left!")
    bag = input("Pick a bag you think is over the weight limit:")
    if bag == "" or int(bag) > len(model.frac_list) - 1:
        print("Please type in the index of the bag you want to pick!")
    else:
        check = model.check_bag(int(bag))
        if (check == 0):
            print("Nice one! " + "Bag " + bag + " is over the set weight limit")
        if (check == -1):
            print("Try again, that bag isn't over the weight limit")
        if (check == 1):
            print("CONGRATULATIONS! You found all of the bags!")