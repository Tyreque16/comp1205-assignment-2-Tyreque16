
def get_input():
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    return++ numerator, denominator
def is_proper_fraction(numerator, denominator):
   
    return numerator < denominator

def convert_to_mixed_fraction(numerator, denominator):
    
    integer_part = numerator // denominator
    remainder = numerator %
    if remainder == 0:
        return str(integer_part)  # No fractional part, just an integer
    else:
        return f"{integer_part} + {remainder}/{denominator}"

def display_fraction_type(numerator, denominator):
    if is_proper_fraction(numerator, denominator):
        print(f"{numerator}/{denominator} is a proper fraction.")
    else:
        mixed_fraction = convert_to_mixed_fraction(numerator, denominator)
        print(f"{numerator}/{denominator} is an improper fraction and it can be written as {mixed_fraction}.")

def main():
    numerator, denominator = get_input()
    display_fraction_type(numerator, denominator)

if __name__ == "__main__":

