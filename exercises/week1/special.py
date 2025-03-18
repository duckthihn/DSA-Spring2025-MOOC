def check_year(year):
    x = year // 100 # first 2 digits
    y = year % 100 # last 2 digits

    return (x+y)**2 == year

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False