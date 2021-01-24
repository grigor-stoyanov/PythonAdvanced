from collections import deque

bullet_cost = int(input())
gun_barrel = int(input())
bullets = list((map(int, input().split())))
locks = deque(map(int, input().split()))
safe_value = int(input())
current_bullet = 0
while bullets and locks and gun_barrel > 0:
    for bullet in range(1, gun_barrel+1):
        current_bullet = bullet
        shot = bullets.pop()
        safe_value -= bullet_cost
        if shot <= locks[0]:
            print('Bang!')
            locks.popleft()
            if not locks or not bullets:
                break
        else:
            print('Ping!')
            if not bullets:
                break
    if bullets and current_bullet == gun_barrel:
        current_bullet = 0
        print('Reloading!')
if not locks:
    print(f'{len(bullets)} bullets left. Earned ${safe_value}')
elif not bullets:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
