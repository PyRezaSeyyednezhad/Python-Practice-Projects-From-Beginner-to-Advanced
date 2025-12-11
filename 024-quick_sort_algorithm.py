def quick_sort_algorithm(user_list):
    # اگر طول لیست ۰ یا ۱ باشد، نیازی به مرتب‌سازی نیست
    if len(user_list) <= 1:
        return user_list

    # مرحله ۱: انتخاب pivot (اینجا عنصر وسط لیست)
    pivot = user_list[len(user_list) // 2]

    # مرحله ۲: تقسیم لیست به سه بخش
    left = [x for x in user_list if x < pivot]      # عناصر کوچکتر از pivot
    middle = [x for x in user_list if x == pivot]   # عناصر برابر با pivot
    right = [x for x in user_list if x > pivot]     # عناصر بزرگتر از pivot

    # مرحله ۳: مرتب‌سازی بازگشتی بخش‌های چپ و راست
    return quick_sort_algorithm(left) + middle + quick_sort_algorithm(right)



print(quick_sort_algorithm([5,10,5,6,7,9,8,1,9, 1, 2, 3, 4, 7, 6, 4]))
print(quick_sort_algorithm([5,10,5,6,7,9,8,1,9, 1, 2, 3, 4, 7, 6]))
print(quick_sort_algorithm([5,10,5,6,7,9,8,1,9, 1, 2, 3, 4, 7, 6, 4, 3]))