import random
def reroll(array):
    turn=2
    while turn>0:
        print("Which dice do you want to reroll?\t"+str(turn)+"chances left")
        print("Submit a dice number you want to reroll. To end a turn, submit 0")
        roll_dice=[]
        while True:
            number = int(input())
            if(number)==0:
                break
            roll_dice.append(number)
            for i in roll_dice:
                array[i-1]= random.randint(1, 6)#선택한 주사위만 다시 굴리기
        if (number) == 0 and roll_dice==[]:#그냥 number가 0이면 바로 break 되니,
            #number가 0이고 roll_dice가 비어있을 때 break
            break
        dice_art = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
        }
        for line in range(5):
            for x in array:
                print(dice_art.get(x)[line], end="")
            print()
        turn-=1
    print("Select from scoreboard.")
    return array
