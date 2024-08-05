def find_second_lowest_score(students):
    # Tạo danh sách các điểm số
    scores = [score for name, score in students]
    
    # Tìm điểm thấp nhất và điểm thấp nhì
    unique_scores = list(set(scores))
    unique_scores.sort()
    
    if len(unique_scores) < 2:
        return "Không có điểm thấp nhì"
    
    second_lowest_score = unique_scores[1]
    
    # Tìm tên của thành viên có điểm thấp nhì
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    
    return second_lowest_students

# Ví dụ sử dụng
students = [
    ("Nguyễn Văn A", 85),
    ("Trần Thị B", 90),
    ("Lê Văn C", 75),
    ("Phạm Thị D", 85),
    ("Hoàng Văn E", 75),
    ("Đỗ Thị F", 95)
]

print(find_second_lowest_score(students))
