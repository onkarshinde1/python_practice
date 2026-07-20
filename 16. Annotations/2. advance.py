from typing import List, Dict, Set  # Older version


def max_marks(marks: List[int]) -> int:
    return max(marks)


# def max_marks(marks: list[int]) -> int:
#     return max(marks)


def print_list(lst: list[int | str]):
    print(lst)


ans = max_marks([65, 32, 67, 87, 33])
print(ans)
print_list([43, 54, "Anirudh"])
