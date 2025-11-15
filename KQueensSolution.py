from KQueens import get_number_conflicts
from KQueens import get_number_conflicts_advanced

import numpy as np


def get_total_conflicts(queens: list[int]) -> int:
    conflicts = get_number_conflicts(queens)
    return sum(conflicts.values())


def HillClimbing(queens: list[int], steps: int = 2) -> list[int]:
    """
    ☆★ 使用爬山演算法解決K皇后問題 ★☆

    傳入參數：
        queens -> (list[int]): 皇后的位置列表，每個元素為該列皇后所在的行索引。
    """

    # 棋盤大小
    size_of_board = len(queens)

    # 初始化第一步
    current_queens = queens.copy()
    current_conflicts = get_total_conflicts(current_queens)
    # next_conflicts = size_of_board * (size_of_board - 1)   # 一個K皇后問題最大的衝突數一定是 k乘k-1

    # (核心演算法)
    while True:
        if current_conflicts == 0:
            print("找到解決方案！")
            return current_queens

        # 把每一種下一步透過矩陣處裡
        current_queens_1xn = np.array(current_queens)
        current_queens_nxn = current_queens_1xn * np.ones((size_of_board, size_of_board), dtype=current_queens_1xn.dtype)
        next_possible_queens_nxsteps = []
        # 考慮到可能的下一步並非只有「一步」
        for step in range(steps):
            every_step = current_queens_nxn.copy() + (step+1) * np.eye(size_of_board, dtype=current_queens_1xn.dtype)
            next_possible_queens_nxsteps.append(np.mod(every_step, size_of_board))
        # 所有的下一步或下N步都在這
        next_possible_queens = np.vstack(next_possible_queens_nxsteps)
        # print(next_possible_queens)

        # 評估所有可能的下一步
        next_possible_conflicts = np.apply_along_axis(get_total_conflicts, 1, next_possible_queens)
        # print(next_possible_conflicts)
        # 最小衝突數及最小衝突數的索引
        min_conflict, min_conflict_index = np.min(next_possible_conflicts), np.argmin(next_possible_conflicts)
        print(min_conflict, min_conflict_index)

        # 最小衝突數的皇后組合及其衝突數
        next_queens = next_possible_queens[min_conflict_index].tolist()
        next_conflicts = min_conflict

        if next_conflicts > current_conflicts:
            print("無法找到更好的解決方案，停止搜尋。(Local Optimum)")
            # 這裡其實還要一段陷入局部解得時候的作法，但我想寫在其函式
            return current_queens
        
        current_queens = next_queens
        current_conflicts = next_conflicts
        print(f"目前衝突數: {current_conflicts}, 目前皇后位置: {current_queens}")


if __name__ == "__main__":
    queens = [1, 4, 0, 2, 4]
    HillClimbing(queens)