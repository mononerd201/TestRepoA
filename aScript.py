import math

def is_prime(num):
    for i in range(2,ceil(math.sqrt(num))):
        if num%i==0:
            return False
    return True

if __name__ == "__main__":
    print("is 987654321 prime?, Answer is:",is_prime(987654321))


