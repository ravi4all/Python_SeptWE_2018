def playerHealth():
    health = 0
    return health

def enemyHealth():
    health = 80
    return health

def game():
    p_h = playerHealth()
    e_h = enemyHealth()
    if p_h == 0:
        # print("Game Over")
        powerUp()
    elif e_h == 0:
        print('You win')
    else:
        print("Game is still running")

def powerUp():
    p_h = playerHealth()
    p_h += 50
    print("Power Up")

game()
# powerUp()