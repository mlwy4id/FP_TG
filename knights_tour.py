import time

N = 8

MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def can_attack(x1, y1, x2, y2):
    return any(x1 + dx == x2 and y1 + dy == y2 for dx, dy in MOVES)

def get_degree(x, y, board):
    return sum(1 for dx, dy in MOVES if is_valid(x + dx, y + dy, board))

def print_board(board, kx, ky, possible_moves):
    print("\n" + "=" * 32)
    for i in range(N):
        for j in range(N):
            if i == kx and j == ky:
                print(" K ", end="")
            elif (i, j) in possible_moves:
                print(" * ", end="")
            elif board[i][j] == -1:
                print(" . ", end="")
            else:
                print("XX ", end="")
        print()
    print("=" * 32)

def knights_tour_visual(start_x, start_y, closed, delay=0.6):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    x, y = start_x, start_y
    board[x][y] = 0

    for step in range(1, N * N):
        possible = []

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, board):
                possible.append((get_degree(nx, ny, board), nx, ny))

        possible.sort()
        possible_positions = [(nx, ny) for _, nx, ny in possible]

        print(f"\nLangkah ke-{step}")
        print(f"Posisi Kuda: ({x}, {y})")
        print("Kemungkinan langkah:", possible_positions)

        print_board(board, x, y, possible_positions)
        time.sleep(delay)

        if not possible:
            print("Tidak ada langkah lanjutan.")
            return False

        # Ambil langkah terbaik (Warnsdorff)
        _, x, y = possible[0]
        board[x][y] = step

        print(f"Kuda berpindah ke: ({x}, {y})")

    # Cek closed tour
    if closed:
        if can_attack(x, y, start_x, start_y):
            print("\nCLOSED TOUR BERHASIL (attacking square)")
            return True
        else:
            print("\nCLOSED TOUR GAGAL (tidak menyerang kotak awal)")
            return False

    print("\n OPEN TOUR BERHASIL")
    return True


if __name__ == "__main__":
    print("KNIGHT'S TOUR")
    print("1. Open Tour (berhenti di sembarang kotak)")
    print("2. Closed Tour (berhenti di attacking square)")

    choice = input("Pilih mode (1 / 2): ").strip()
    closed = choice == "2"

    start_x = int(input("Posisi awal baris (0-7): "))
    start_y = int(input("Posisi awal kolom (0-7): "))

    knights_tour_visual(start_x, start_y, closed)
