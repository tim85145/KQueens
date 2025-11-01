def get_number_conflicts(queens: list[int]) -> dict[tuple[int, int], int]:
    """
    ☆★ 計算皇后衝突的數量 ★☆
    
    但凡有衝突的皇后，必定在同一列上、正對角線上或反對角線上：
    1. 同一行: col 相同
    2. 正對角線: row - cal 相同
        Ex: 以5x5為例，「↘」的方向的值會相同
            ┌ 0 -1 -2 -3 -4 ┐
            │ 1  0 -1 -2 -3 │
            │ 2  1  0 -1 -2 │
            │ 3  2  1  0 -1 │
            └ 4  3  2  1  0 ┘
    3. 反對角線: row + cal 相同
        Ex: 以5x5為例，「↙」的方向的值會相同
            ┌ 0  1  2  3  4 ┐
            │ 1  2  3  4  5 │
            │ 2  3  4  5  6 │
            │ 3  4  5  6  7 │
            └ 4  5  6  7  8 ┘
    因此，此函式架構如下，
    第一步，分別建立了三個集合以及三個字典來追蹤皇后的位置和衝突情況。
                      ┌ queens_col: 用於追蹤已放置皇后的行位置。
    1. 皇后位置(集合)  │ queens_diag: 用於追蹤已放置皇后的正對角線位置。
                      └ queens_anti_diag: 用於追蹤已放置皇后的反對角線位置。
                      ┌ conflicts_col: 用於追蹤行衝突的位置及數量。
    2. 衝突軸(字典)    │ conflicts_diag: 用於追蹤正對角線衝突的位置及數量。
                      └ conflicts_anti_diag: 用於追蹤反對角線衝突的位置及數量。

    第二步，透過第一個for迴圈，遍歷一次每個皇后，並將其位置以及衝突狀況記錄在上述六個集合中。
    1. 取得皇后行、正對角線以及反對角線的值。
    2. 將行、正對角線以及反對角線的值作為key值，初始化衝突軸字典的value為0(表一開始皆無衝突)。
    3. 檢查該行、正對角線和反對角線是否已有皇后存在，若有則將該位置的衝突數+1。
    Hint: 關於2.及3.的衝突軸字典，如果該軸(key)的值(value)大於0，表示該軸上有衝突，但值不等於皇后數量，因為衝突數是從0開始計算的，所以如果value = N，表示該軸上有N+1個皇后存在(無論是行、正對角線或是反對角線都一樣)。
    4. 將當前皇后的行、正對角線和反對角線位置加入對應的皇后集合中。

    第三部，再透過第二個for迴圈，再遍歷一次每個皇后的位置，將其行、正對角線和反對角線的衝突數加總。
    1. 建立一個conflicts_positions集合以及conflicts_count字典，分別紀錄衝突皇后的座標以及次數。
    2. 取得皇后行、正對角線以及反對角線的值。
    3. 初始化該皇后的衝突次數(0)。
    4. 計算該皇后的衝突次數(行、正對角線、反對角線的衝突次數總和)。
    5. 如果該皇后的衝突數大於0，則將該皇后的座標加入conflicts_positions集合中。

    第四步，回傳衝突的數量。


    傳入參數：
        queens -> list[int]: 皇后的位置列表，每個元素為 (row, col)。

    回傳值：
        dict[tuple[int, int], int]: 每個皇后的位置及其衝突數。

    """

    # 第一步，建立六個主要集合來追蹤皇后的位置和衝突情況  ex:[2, 0, 7, 3, 6, 4, 5, 1]
    # 1. 皇后的位置
    queens_col: set[int] = set()          # 行  ex: {2, 0, 7, 3, 6, 4, 5, 1}
    queens_diag: set[int] = set()         # 正對角線  ex: {-2, 1, -5, 0, -2, 1, 1, 6}
    queens_anti_diag: set[int] = set()    # 反對角線  ex: {2, 1, 9, 6, 10, 9, 11, 8}

    # 2. 衝突的位置
    conflicts_col: dict[int, int] = {}            # 行衝突  ex: {}
    conflicts_diag: dict[int, int] = {}           # 正對角線衝突  ex: {-2: 1, 1: 3}
    conflicts_anti_diag: dict[int, int] = {}      # 反對角線衝突  ex: {9: 2}

    # 第二步，取得皇后衝突的狀況並記錄
    for row, col in enumerate(queens):
        # 1. 取得皇后正對角線以及反對角線的值
        diagonal = row - col        # 正對角線
        anti_diagonal = row + col   # 反對角線

        # 2. 初始化衝突軸的位置
        conflicts_col.setdefault(col, 0)
        conflicts_diag.setdefault(diagonal, 0)
        conflicts_anti_diag.setdefault(anti_diagonal, 0)

        # 3. 如果該行、正對角線和反對角線已有皇后存在，則將該位置的衝突數+1
        if col in queens_col:
            conflicts_col[col] += 1
        if diagonal in queens_diag:
            conflicts_diag[diagonal] += 1
        if anti_diagonal in queens_anti_diag:
            conflicts_anti_diag[anti_diagonal] += 1

        # 4. 將當前皇后的行、正對角線和反對角線位置加入對應的皇后集合中
        queens_col.add(col)
        queens_diag.add(diagonal)
        queens_anti_diag.add(anti_diagonal)


    # 第三步，取得衝突的皇后座標及數量
    # 1. 建立紀錄衝突皇后的座標以及次數的容器
    conflicts_positions: set[tuple[int, int]] = set()   # 紀錄衝突的皇后位置
    conflicts_count: dict[tuple[int, int], int] = {}    # 紀錄每個皇后的衝突次數  key:皇后座標 value:衝突次數 if value = 0 則表示該皇后不衝突
    for row, col in enumerate(queens):
        # 2. 取得皇后正對角線以及反對角線的值
        diagonal = row - col        # 正對角線
        anti_diagonal = row + col   # 反對角線

        # 3. 初始化該皇后的衝突次數(0)，少了這一行則只記錄有衝突的皇后
        conflicts_count.setdefault((row, col), 0)

        # 4. 計算該皇后的衝突次數(行、正對角線、反對角線的衝突次數總和)
        conflicts_count[(row, col)] = conflicts_col[col] + conflicts_diag[diagonal] + conflicts_anti_diag[anti_diagonal]

        # 如果該皇后的衝突數大於0，則將該皇后的座標加入conflicts_positions集合中(老師題目未要求，但我覺得有用)
        if conflicts_count[(row, col)] > 0:
            conflicts_positions.add((row, col))


    # print(f"衝突的皇后位置: {conflicts_positions}")

    # 第四步，回傳衝突的數量
    return conflicts_count

def get_number_conflicts_advanced(queens: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    """
    ☆★ 計算皇后衝突的數量（進階版）★☆

    (請先了解基礎版在還看進階版，基本上進階版差異就是多處理row)

    此函式處理每個皇后隨機放置的情況，並考慮列衝突。
    皇后可能位於同一列、同一行、正對角線或反對角線上。

    傳入參數：
        queens -> (list[tuple[int, int]]): 皇后的位置列表，每個元素為 (row, col)。

    回傳值：
        dict[tuple[int, int], int]: 每個皇后的位置及其衝突數。
    """
    # 初始化追蹤衝突的資料結構
    # 1.皇后的位置
    queens_row: set[int] = set()          # 列
    queens_col: set[int] = set()          # 行
    queens_diag: set[int] = set()         # 正對角線
    queens_anti_diag: set[int] = set()    # 反對角線

    # 2. 衝突的位置
    conflicts_row: dict[int, int] = {}            # 列衝突
    conflicts_col: dict[int, int] = {}            # 行衝突
    conflicts_diag: dict[int, int] = {}           # 正對角線衝突
    conflicts_anti_diag: dict[int, int] = {}      # 反對角線衝突

    # 第一輪：記錄所有皇后的位置及衝突情況
    for row, col in queens:
        diagonal = row - col        # 正對角線
        anti_diagonal = row + col   # 反對角線

        # 初始化衝突軸的位置
        conflicts_row.setdefault(row, 0)
        conflicts_col.setdefault(col, 0)
        conflicts_diag.setdefault(diagonal, 0)
        conflicts_anti_diag.setdefault(anti_diagonal, 0)

        # 檢查並記錄衝突
        if row in queens_row:
            conflicts_row[row] += 1
        if col in queens_col:
            conflicts_col[col] += 1
        if diagonal in queens_diag:
            conflicts_diag[diagonal] += 1
        if anti_diagonal in queens_anti_diag:
            conflicts_anti_diag[anti_diagonal] += 1

        # 將當前皇后的位置加入對應的集合中
        queens_row.add(row)
        queens_col.add(col)
        queens_diag.add(diagonal)
        queens_anti_diag.add(anti_diagonal)

    # 第二輪：計算每個皇后的衝突數
    conflicts_count: dict[tuple[int, int], int] = {}
    for row, col in queens:
        diagonal = row - col
        anti_diagonal = row + col

        # 初始每個皇后的衝突數
        conflicts_count.setdefault((row, col), 0)

        # 計算該皇后的衝突次數
        conflicts_count[(row, col)] = (
            conflicts_row[row] +
            conflicts_col[col] +
            conflicts_diag[diagonal] +
            conflicts_anti_diag[anti_diagonal]
        )

    return conflicts_count


    
if __name__ == "__main__":
    print("☆★ N 皇后衝突數計算器 ★☆")
    print("輸入格式範例: 0 4 7 5 2 6 1 3 (不須輸入N值，系統會依照輸入的座標數量自動判斷N值)")
    
    while True:
        input_queens = input("請輸入皇后位置(或輸入 'exit' 離開)：")
        if input_queens.lower() == 'exit':
            break
        try:
            queens = list(map(int, input_queens.split(' ')))
            
            if len(queens) == 1 and queens[0] != 0:
                print("好吧~如果你堅持輸入棋盤數量...")
                continue

            if not all(x >= 0 for x in queens):
                raise ValueError("輸入僅限非負整數，請重新輸入。")
            
            queens_conflicts = get_number_conflicts(queens)
            print(queens_conflicts)
            for queen in queens_conflicts:
                print(f"皇后 {queen} 衝突數 = {queens_conflicts[queen]}")
        except ValueError as ve:
            if "invalid literal for int()" in str(ve):
                print("輸入不接受文字，請重新輸入。")
            else:
                print(ve)
        except Exception as e:
            print(f"輸入錯誤: {e}，請重新輸入。")
