import score_calc
def scordboard(array):
    turn=12
    menu=int(input("Where do you want to put your score?"
        +"1.Ones 2.Twos 3.Threes 4.Fours 5.Fives 6.Sixes\n "
        +"7.Choices 8.small_straight 9. large_straight\n"
        +"10. Four_kinds 11. Full_house 12. Yacht\n"))
    if menu==1:
        turn -= 1
        return score_calc.ones(array), 1
    elif menu==2:
        turn -= 1
        return score_calc.twos(array), 2
    elif menu==3:
        turn -= 1
        return score_calc.threes(array), 3
    elif menu==4:
        turn -= 1
        return score_calc.fours(array), 4
    elif menu==5:
        turn -= 1
        return score_calc.fives(array), 5
    elif menu==6:
        turn -= 1
        return score_calc.sixes(array), 6
    elif menu==7:
        turn -= 1
        return score_calc.choice(array), 7
    elif menu==8:
        turn -= 1
        return score_calc.small_straight(array), 8
    elif menu==9:
        turn -= 1
        return score_calc.large_straight(array), 9
    elif menu==10:
        turn -= 1
        return score_calc.four_kind(array), 10
    elif menu==11:
        turn -= 1
        return score_calc.full_house(array), 11
    elif menu==12:
        turn -= 1
        return score_calc.yacht(array), 12
    else:
        print("Invalid number")
