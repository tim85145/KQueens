from KQueens import get_number_conflicts
from KQueens import get_number_conflicts_advanced



if __name__ == "__main__":
    queens = [0, 4, 7, 5, 0, 6, 1, 3]
    number_conflicts = get_number_conflicts(queens)
    print(number_conflicts)
    print(sum(number_conflicts.values()))