import random
import time
from KQueens import number_conficts

def generate_random_queens(n):
    """隨機產生一組 N 皇后位置（允許衝突）"""
    return [random.randint(0, n-1) for _ in range(n)]

if __name__ == "__main__":
    max_time = 10  # 秒
    n = 8000
    while True:
        test_data = [generate_random_queens(n) for _ in range(10)]
        start = time.time()
        # print(f"\n測試 {n} 皇后：")
        for idx, queens in enumerate(test_data):
            conflicts = number_conficts(queens)
            # print(f"第{idx+1}組：{queens} 衝突數={conflicts}")
        end = time.time()
        avg_time = (end - start) / 10
        print(f"測試{n} 皇后 10 組平均計算時間：{avg_time:.4f} 秒")
        if avg_time > max_time:
            print(f"\n超過 {max_time} 秒，最大可處理皇后數量為：{n-1}")
            break
        n += 1