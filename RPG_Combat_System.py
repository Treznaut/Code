import random
#player stats
hp = 10
st = random.randint(2,5)
sp = random.randint(1,5)
sm = random.randint(1,5)

#prints player stats
print("Your stats")
stats = (hp,st,sp,sm)
print(stats)

#creates easy enemy stats
ez_en_hp = random.randint(4,8)
ez_en_st = random.randint(1,4)
ez_en_sp = random.randint(1,4)
ez_en_sm = random.randint(1,4)
ez_en_stats = (ez_en_hp,ez_en_st,ez_en_sp,ez_en_sm)

#easy battle function so i can use whenever
def ez_btl():
    global ez_en_hp, ez_en_st, ez_en_sp, ez_en_sm
    global hp, st, sp, sm
    print("Enemy stats")
    print(ez_en_stats)
    pl_dmg = random.randint(0,st)
    ez_en_dmg = random.randint(0,ez_en_st)
    while hp >= 1 and ez_en_hp >= 0:
        if sp > ez_en_sp:
            pl_turn_btl = input("It is your turn do you \"Attack\" or \"Skip\" your turn? ")
            if pl_turn_btl == "Attack":
                print("You dealt {} Damage".format(pl_dmg))
                ez_en_hp -= pl_dmg
                if pl_dmg == 0:
                    print("You missed!")
                print("The enemy is on {} hp!".format(ez_en_hp))
            else:
                print("You skipped you turn the enemy is still on {} hp!".format(ez_en_hp))
            hp -= ez_en_dmg
            if ez_en_dmg == 0:
                print("The enemy missed!")
            print("The enemy dealt {} to you".format(ez_en_dmg))
            print("You are on {} hp".format(hp))
        elif sp < ez_en_sp:
            hp -= ez_en_dmg
            if ez_en_dmg == 0:
                print("The enemy missed!")
            print("The enemy dealt {} to you".format(ez_en_dmg))
            print("You are on {} hp".format(hp))
            pl_turn_btl = input("It is your turn do you \"Attack\" or \"Skip\" your turn? ")
            if pl_turn_btl == "Attack":
                print("You dealt {} Damage".format(pl_dmg))
                ez_en_hp -= pl_dmg
                if pl_dmg == 0:
                    print("You missed!")
                print("The enemy is on {} hp!".format(ez_en_hp))
            else:
                print("You skipped you turn the enemy is still on {} hp!".format(ez_en_hp))
    if hp <= 0:
        print("You lost") 
    elif ez_en_hp <= 0:
        print("You won")
ez_btl()
no = input("yes")

