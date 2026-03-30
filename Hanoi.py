def hanoi_solver(n):
    # Set up the board
    moves_log = ""
    hanoi_towers = [[], [], []]

    for i in range(n, 0, -1):
        hanoi_towers[0].append(i)

    # Helper functions
    def log_move():
        nonlocal moves_log
        nonlocal hanoi_towers
        for i in range(len(hanoi_towers)):
            moves_log += f"{hanoi_towers[i]} "
        moves_log = moves_log[:-1]
        moves_log += "\n"

    def move_pieces(p, source, target, auxiliary):
        nonlocal n
        nonlocal hanoi_towers
        if p == 1:
            hanoi_towers[target].append(hanoi_towers[source].pop())
            log_move()
            return

        move_pieces(p - 1, source, auxiliary, target)
        hanoi_towers[target].append(hanoi_towers[source].pop())
        log_move()
        move_pieces(p - 1, auxiliary, target, source) 

    log_move()
    move_pieces(n, 0, 2, 1)

    return moves_log[:-1]

print("Hanoi 2")
print(hanoi_solver(2))
print("Hanoi 3")
print(hanoi_solver(3))
print()
print("Hanoi 4")
print(hanoi_solver(4))
print()
print("Hanoi 5")
print(hanoi_solver(5))