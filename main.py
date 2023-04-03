# Challenge 1 : write a python function to find all prime factors 
# Input ==> Integer value , Output: list of prime factors 
# Example : get_prime_factors(630) ==> [2, 3, 3, 5, 7]


def get_prime_factors(number): 
    # Function definition to get all prime factors
    factors = [] 
    divider = 2 
    while divider <= number: 
        if number % divider == 0 : 
            factors.append(divider)
            number //= divider
        else: 
            divider += 1 
    return factors 

# print(get_prime_factors(630))