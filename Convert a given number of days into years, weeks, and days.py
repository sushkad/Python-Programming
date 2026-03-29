

total_days = int(input("Enter total days: "))

years = total_days // 365

remaining_days = total_days % 365

weeks = remaining_days // 7

days = remaining_days % 7

print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")

