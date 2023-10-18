# Classes and Definition excercise 2
first_name = "John"
last_name = "Doe"
birthday_date = "3"
birthday_year = "2019"

class Organzation:
    def names(self, fname, lname):
        first_name = fname
        last_name = lname
        self.names = fname + lname
        return self.names
    
    def birthday(self, date, year):
        birthday_date = date
        birthday_year = year
        self.birthday = date + year
        return self.birthday

# Tie class to a variable
org = Organzation()
# Tie clsss.function to a variable
full_name = org.names(first_name, last_name)
birthday = org.birthday(birthday_date, birthday_year)

print(f"Hello my name is: {full_name} and my birthday is on: {birthday}")
