import snake_class as scl
import time as tm
check = False
pole = scl.Field()
#pole.play()
snake = [scl.Snake('black', 'white', 'turtle', i*30, i*50, 5) for i in range(1)]
food = scl.Food('green', 'circle')
food.food_pos()
pole.listen_p(snake)
print(snake)
while True:
    for i in snake:
        if i.dtp():
            i.move()
        else:
            check = True
            pole.end_game()
        if i.check_food(food):
            food.food_pos()
            i.more('black', 'turtle')
    pole.reload()
    tm.sleep(0.2)
    if check:
        break
        
    
