DAYS_PER_YEAR:int = 365
HOURS_PER_DAY:int=24
MIN_PER_HOUR:int=60
SEC_PER_MIN:int=60

second_in_a_year= (DAYS_PER_YEAR*HOURS_PER_DAY*MIN_PER_HOUR*SEC_PER_MIN)

print(f"There are {second_in_a_year}seconds in a year")