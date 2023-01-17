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
            if cmd == "2" and status <= 15:
                print("2번 갱도문이 잠겨있다. 아직은 갈 수 없을 것 같다.")
                time.sleep(2)
                continue
            elif cmd == "2" and status > 15:
                print("열쇠로 갱도문을 열었다.")
                time.sleep(1)
                return cmd
            elif cmd == '1' or cmd == '2' or cmd == '3':
                return cmd
            else:
                print("잘못 입력했다. 숫자를 입력하고 Enter")
                time.sleep(1.5)
                os.system("cls")

def explore(status = 0):
    command = choice("explore")
    if command == '1':
        percent = random.randrange(1,11)
        if percent>7:
            monster()
        elif percent > 6:
            grow()
        else:
            success()


def run():
    status = 0 #갱도나 다른 장소에 들어갈 수 있는 지 없는 지 판단을 위한 변수
    turn = 0 #지나간 일 수
    tired = 0 #힘듦 수치
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
                explore(status)
                status += 1
                if status == 16:
                    print("열쇠를 찾았다. 2번 갱도문 열쇠같은데,,")
        elif command == '3':
            os.system('cls')
            print(f"동굴에 들어온 지 {turn}일, 힘듦 수치: {tired}")


if __name__ == "__main__":
    run()