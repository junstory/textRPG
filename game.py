import time
import os
import random
from explore import *

def start():
    print("""
    ▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓
    ░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░
    ░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
    ░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒
    ▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░  ░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓
    ░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░    ░░▒▒▒▒░░░░░░░░░░▒▒░░░░
    ▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒░░  ░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒
    ▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒░░░░      ░░░░▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒
    ▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░          ░░▒▒▓▓▓▓▓▓▓▓▒▒▓▓
    ░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░▒▒░░        ░░▒▒▒▒░░░░░░░░░░
    ░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒░░      ░░▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒
    ░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒
    ▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓
    ░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░████████████░░░░░░░░▒▒░░░░
    ▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒
    ▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓░░░░░░▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▒▒▓▓▒▒▒▒▒▒▓▓░░▒▒
    ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒
    ▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░▒▒░░░░░░░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒
    """)
    print("광산이 무너지면서 완전히 고립된 것 같다..")
    time.sleep(2)
    print("1시간이 다 되도록 입구 벽을 두드려봤지만 아무 반응도 없는걸 봐선,,")
    time.sleep(2)
    print("여기에 아무도 없다고 생각하나..?")
    time.sleep(2)
    print("아무래도 당분간 버텨야겠는데,,")
    time.sleep(2)
    print("일단 뭘 해야하지..?")
    time.sleep(2)
    print("듣기로는 2번 갱도부터는 아직 공사가 끝나지 않았다고 하던데,,")
    time.sleep(2)

def choice(scene, status=0):
    while(True):
        if scene == "start":
            cmd = input("무엇을 할까? 1.쉰다 2.탐험한다. 3.상태 \n>>")
            if cmd == '1' or cmd == '2' or cmd == '3':
                return cmd
            else:
                print("잘못 입력했다. 숫자를 입력하고 Enter")
                time.sleep(1.5)
                os.system("cls")
        elif scene == "explore":
            cmd = input("어디로 갈까? 1.갱도1 2.갱도2  \n>>")
            if cmd == "2" and status < 15:
                print("2번 갱도문이 잠겨있다. 아직은 갈 수 없을 것 같다.")
                time.sleep(2)
                continue
            elif cmd == "2" and status >= 15:
                print("열쇠로 갱도문을 열었다.")
                time.sleep(1)
                return cmd
            elif cmd == '1' or cmd == '2' or cmd == '3':
                return cmd
            else:
                print("잘못 입력했다. 숫자를 입력하고 Enter")
                time.sleep(1.5)
                os.system("cls")

def explore(status = 0,score = 0):
    command = choice("explore",status)
    if command == '1':
        percent = random.randrange(1,11)
        if percent>7:
            monster(1)
        elif percent > 6:
            grow()
        else:
            success()
    elif command == "2":
        percent = random.randrange(1,11)
        if percent>6:
            monster(2)
        elif percent > 2:
            grow()
        else:
            success()
        score += 1



def run():
    status = 0 #갱도나 다른 장소에 들어갈 수 있는 지 없는 지 판단을 위한 변수
    turn = 0 #지나간 일 수
    tired = 0 #힘듦 수치
    score = 0 #갱도2를 탐험한 횟수
    while True:
        command = choice("start")
        print(command)
        if command == '1':
            tired -=2
            if tired <0:
                tired = 0
            turn += 1
            print("몸이 좀 가벼워진 것 같다.")
            time.sleep(1)
            os.system("cls")
        elif command == '2':
            if tired > 10:
                turn +=3
                print("너무 지친다,, 잠시 쉬어야 할 것 같아...")
                time.sleep(2)
                print("힘듦 수치가 10을 넘으면 플레이어가 쓰러진 상태로 3일이 지나갑니다.")
                time.sleep(2)
                os.system("cls")
                tired -=3
            else:
                tired += 1
                turn += 1
                os.system("cls")
                explore(status, score)
                status += 1
                if status == 15:
                    print("열쇠를 찾았다. 2번 갱도문 열쇠같은데,,")
        elif command == '3':
            os.system('cls')
            print(f"동굴에 들어온 지 {turn}일, 힘듦 수치: {tired}")
        if turn > 30:
            total = status*2 + score*4
            os.system('cls')
            time.sleep(2)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print(f"동굴에 들어온 지 {turn}일이 되는 날이다.. 드디어 입구에서 빛이 들어온다,,")
            time.sleep(4)
            print(f"생존에 성공하셨습니다!\n")
            time.sleep(1)
            print(f"탐험횟수 : {status}")
            time.sleep(1)
            print(f"2번갱도 탐험 횟수 : {score}")
            time.sleep(1)
            print(f"종합 플레이 점수 : ", total)
            time.sleep(1)
            if status <3:
                print("\n한 줄 평 : 너무 안전하게 하신건 아닌가요?? :( ")
                time.sleep(3)
                
            print("게임이 종료됩니다. 플레이 해주셔서 감사합니다.")
            time.sleep(3)
            break
            
            


if __name__ == "__main__":
    run()