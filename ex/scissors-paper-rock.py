# じゃんけんゲーム
import random
ur_points = 0
en_points = 0
print("Scissors-Paper-Rock!!")
while ur_points < 5 and en_points < 5:
    # 1: scissors, 2: paper, 3: rock
    ur_hand = int(input("What's ur hand?\n"
                    "(1: scissors, 2: paper, 3: rock 4: quit) > "))
    en_hand = random.randint(0, 2) + 1
    if ur_hand == 1:    # ur hand is "scissors"
        if en_hand == 1:    # en hand is "scissors"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: scissors\n"
                  f"    en hand: scissors\n"
                  f"    draw!")
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 2:  # en hand is "paper"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: scissors\n"
                  f"    en hand: paper\n"
                  f"    u won!")
            ur_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 3: # en hand is "rock"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: scissors\n"
                  f"    en hand: rock\n"
                  f"    u lost!")
            en_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
    elif ur_hand == 2:  # ur hand is "paper"
        if en_hand == 1:    # en hand is "scissors"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: paper\n"
                  f"    en hand: scissors\n"
                  f"    u lost!")
            en_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 2:  # en hand is "paper"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: paper\n"
                  f"    en hand: paper\n"
                  f"    draw!")
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 3: # en hand is "rock"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: paper\n"
                  f"    en hand: rock\n"
                  f"    u won!")
            ur_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
    elif ur_hand == 3: # ur hand is "rock"
        if en_hand == 1:    # en hand is "scissors"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: rock\n"
                  f"    en hand: scissors\n"
                  f"    u won!")
            ur_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 2:  # en hand is "paper"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: rock\n"
                  f"    en hand: paper\n"
                  f"    u lost!")
            en_points += 1
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
        elif en_hand == 3: # en hand is "rock"
            print("Scissors-Paper-Rock!!")
            print(f"    ur hand: rock\n"
                  f"    en hand: rock\n"
                  f"    draw!")
            print(f"    u:{ur_points} en:{en_points}\n")
            continue
    elif ur_hand == 4:
        quit = input("Quit this game? (y/n) > ")
        if quit == "y":
            break
        else:
            print("")
            continue
    else:
        print("Choose ur hand!")

if ur_points == 5:
    print("Congrats! u won the game!")
elif en_points == 5:
    print("Sorry, u lost the game...")
