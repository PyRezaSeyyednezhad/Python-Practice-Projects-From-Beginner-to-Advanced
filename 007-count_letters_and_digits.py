# count_letters_and_digits
def count_letters_and_digits(s):
    letters = 0
    digits = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return f"Character: {letters}, Digits: {digits}"

# توضیحات
# این تابع تعداد حروف و اعداد موجود در یک رشته را شمارش می‌کند.
# ورودی: یک رشته (s)
# خروجی: تعداد حروف و اعداد به صورت یک تاپل (تعداد حروف، تعداد اعداد)

print(f'Sentences:\n Hello1234World567 \n {count_letters_and_digits("Hello1234World567")}')
