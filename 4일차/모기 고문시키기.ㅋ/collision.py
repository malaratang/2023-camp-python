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
to_x = 0 # 이동할 좌표 (x축 방향으로만 움직임)
character_speed = 5 # 이동 속도

# 장애물 불러오기

enemy = pygame.image.load("C:\\Users\\저스트필\\Desktop\\모기 고문시키기.ㅋ\\종이컵.png")
enemy_size = enemy.get_rect().size #이미지 크기 구하기
enemy_width = enemy_size[0] #가로 크기
enemy_height = enemy_size[1] # 세로 크기
enemy_x_pos = random.randint(0,screen_width - enemy_width)

# 화면 가로의 절반에 위치
enemy_y_pos = 0
enemy_speed = 5 # 이동 속도

clock = pygame.time.Clock() # FPS

# 이벤트 루프
running = True #게임이 실행 중인가?
while running:
    dt = clock.tick(10) # FPS 설정
    # 타이머 집어 넣기
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어 초 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    for event in pygame.event.get():# 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가? (창의 x버튼을 눌렀는가?)
          running = False# 게임이 더 이상 실행 중이 아님
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # rectangle 기준으로 충돌 여부 확인.
        print("충돌했어요")
    running = False

    screen.blit(background,(0,0))# 맨 왼쪽 맨 위 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(timer,(10, 10))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos ))
    pygame.display.update()# 게임화면을 다시 그리기
    if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인한다.
        if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동한다.
            to_x -= character_speed # to_x = to_x - chacter_speed
        elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동한다.
            to_x += character_speed # to_x = to_x + chacter_speed

    if event.type == pygame.KEYUP: # 키에서 손을 뗐는지 확인한다.
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
    character_x_pos += to_x

    # 가로의 경계값 설정 (캐릭터)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

# 세로의 경계값 설정 (캐릭터)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

#  경계값 설정 (장애물)
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)

# pygame 종료
pygame.quit()