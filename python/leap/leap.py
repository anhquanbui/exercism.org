def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True      # thế kỷ chia hết cho 400 -> nhuận
    if year % 100 == 0:
        return False     # thế kỷ không chia hết cho 400 -> không nhuận
    return year % 4 == 0 # các năm còn lại: chia hết cho 4 -> nhuận
