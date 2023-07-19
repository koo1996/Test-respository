def solution(a, b):
    day_ = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_ = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    return day_[(sum(month_[:a-1]) + b) % 7]