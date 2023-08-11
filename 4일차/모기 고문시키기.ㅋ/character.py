import pygame # pygame 모듈
import random

pygame.init() # 초기화 (필수)

# 화면 크기 설정
screen_width = 480# 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("귀여운 모기 살리기") # 게임 이름 설정

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\저스트필\\Desktop\\모기 고문시키기.ㅋ\\배배경.png")

# 캐릭터 불러오기

character = pygame.image.load("C:\\Users\\저스트필\\Desktop\\모기 고문시키기.ㅋ\\모기실사.png")
character_size = character.get_rect().size # 이미지 크기 구하기 (rect = rectangle)
character_width = character_size[0] # 가로 크기
character_height = character_size[1] # 세로 크기
character_x_pos = (screen_width/2) - (character_width/2) # 화면 가로 중간에 위치
character_y_pos = screen_height - character_height # 화면 맨 아래에 위치

# 장애물 불러오기

enemy = pygame.image.load("C:\\Users\\저스트필\\Desktop\\모기 고문시키기.ㅋ\\종이컵.png")
enemy_size = enemy.get_rect().size #이미지 크기 구하기
enemy_width = enemy_size[0] #가로 크기
enemy_height = enemy_size[1] # 세로 크기
enemy_x_pos = random.randint(0,screen_width - enemy_width)

# 화면 가로의 절반에 위치
enemy_y_pos = 0
enemy_speed = 5 # 이동 속도

# 이벤트 루프
running = True #게임이 실행 중인가?
while running:
    for event in pygame.event.get():# 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가? (창의 x버튼을 눌렀는가?)
          running = False# 게임이 더 이상 실행 중이 아님

    screen.blit(background,(0,0))# 맨 왼쪽 맨 위 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos ))
    pygame.display.update()# 게임화면을 다시 그리기

# pygame 종료
pygame.quit()