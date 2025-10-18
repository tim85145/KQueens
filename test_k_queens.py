import random
import time
from KQueens import get_number_conflicts

def generate_random_queens(n: int) -> list[int]:
    """隨機產生一組 N 皇后位置（允許衝突）"""
    return [random.randint(0, n-1) for _ in range(n)]

if __name__ == "__main__":
    max_time = 1  # 秒
    n = 100000    # 皇后數量
    
    test_data = [generate_random_queens(n) for _ in range(10)]  # 測試的組數
    
    start = time.time()
    print(f"\n測試 {n} 皇后：")
    for idx, queens in enumerate(test_data):
        print(f"[{time.time()}] 第 {idx+1} 組開始測試...")
        conflicts = get_number_conflicts(queens)
        print(f"[{time.time()}] 第 {idx+1} 組測試結束。")
        # print(f"第{idx+1}組：{queens} 衝突數={conflicts}")
    end = time.time()
    print(f" {n} 皇后測試結束。")

    avg_time = (end - start) / 10
    print(f"測試 {n} 皇后 10 組平均計算時間：{avg_time:.4f} 秒")
    if avg_time > max_time:
        print(f"\n超過 {max_time} 秒，最大可處理皇后數量為：{n-1}")
            
        