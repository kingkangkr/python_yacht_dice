import score_calc
import reroll
import scoreboard
import score_sort
from rollroll import rollroll

if __name__ == "__main__":
    score_list = [0,0,0]
    total = 0  #최종 점수
    bonus=0
    remain_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 12개를 하고, 한 번 점수를 저장할 때마다 해당하는
    # 번호를 지워서 중복 방지
    while True:
        print("To start yacht dice enter 1")
        print("To see high score, enter 2")
        print("To exit, enter 3")
        score=0#각 턴에 얻은 점수
        player_turn=12
        menu = int(input("Enter a number\n"))
        if menu == 1:
            print("start yacht game")
            while player_turn>0:
                player = reroll.reroll(rollroll())
                score, x= scoreboard.scordboard(player)
                if x not in remain_scores:
                    print("Invalid number. Please select other slot.")
                    score, x= scoreboard.scordboard(player)
                if x>0 and x<7:
                    bonus+=score
                total+=int(score)
                player_turn-=1
                remain_scores.remove(x)
                if bonus>=63:
                    print("You earned a bonus point!")
                    total+=35
                print("You earned " + str(score))
                print("Total score is"+str(total))
                print(str(player_turn)+" turns left")
            print("Your total score is " + str(total))
            score_list.append(total)
        elif menu == 2:
            best_scores=score_sort.score_sort(score_list)
            best_scores=score_list[0:3]
            print("Best score:\t"+str(best_scores[0]))
            print("2nd score:\t" + str(best_scores[1]))
            print("3rd score:\t" + str(best_scores[2]))
        else:
            break