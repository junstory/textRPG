import time
import os
import random

hp = 10
attack = 4
var = 0

def monster(level):
    global hp, attack, var
    hp = 10 + var
    attack = 4 + var * 0.6
    monster_hp = random.randrange(6,int(12+var*0.5))
    monster_attack = random.randrange(2,int(6+var*0.5))
    if level == 2:
        monster_hp += random.randrange(1,var)
        monster_attack += random.randrange(1,int(var*0.8))
    print("갱도의 몬스터를 만났다 무엇을 할까?")
    while True:
        command = input("1.도망친다 2.공격한다 3.막는다 >>")
        if command =='1':
            if random.randrange(0,3) == 1:
                print("무사히 도망쳤다.")
                time.sleep(1)
                os.system("cls")
                return
            else:
                print(f"{monster_attack}데미지를 입었다,,")
                if hp < 0:
                    print("게임오버,, 몬스터에게 당하셨습니다..")
                    time.sleep(2)
                    print("게임이 종료됩니다.. 감사합니다.")
                    time.sleep(3)
                    exit(1)
                time.sleep(1)
        elif command == '2':
            monster_hp -= attack
            print(f"{attack}데미지를 주었다,,")
            time.sleep(1)
            if monster_hp <= 0:
                print("몬스터를 처치했다.")
                time.sleep(1)
                print("조금 강해졌디.")
                var += random.randrange(1,3)
                time.sleep(2)
                os.system("cls")
                return
            hp -= monster_attack
            print(f"{monster_attack}데미지를 입었다,,")
            if hp < 0:
                print("게임오버,, 몬스터에게 당하셨습니다..")
                time.sleep(2)
                print("게임이 종료됩니다.. 감사합니다.")
                time.sleep(3)
                exit()
            time.sleep(1)
        elif command == '3':
            print("공격을 막았다.. 체력이 조금 회복된 것 같다.")
            hp += 2
            time.sleep(1)
        else:
            print("숫자 입력후, Enter키를 눌러주세요.")
            
        

def grow():
    global var
    temp = random.randrange(2,7)
    var += temp
    print(f"열심히 탐험을 했더니 한층 강해진 것 같다. 증가략 : 체력{temp}+, 공격력{temp*0.7}+")
    time.sleep(2)
    os.system("cls")
    
    

def success():
    print("탐험을 성공적으로 마쳤다.")
    time.sleep(1)
    os.system("cls")
