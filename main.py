from functions import lcm, gcd, gen_prime
import random


class RSA:
    def __init__(self, prime_size):
        self.prime_size = prime_size
        self.max_prime = 0
        self.min_prime = 0
        self.q = 0
        self.p = 0
        self.n = 0
        self.lambda_n = 0
        self.e = 65537
        self.d = 0

        self.min_max_prime()
        self.generate_p_and_q()
        self.calculate_n()
        self.calculate_lambda_n()
        # self.generate_e()
        self.calculate_d()

    def min_max_prime(self):
        self.max_prime = pow(2, self.prime_size // 2) - 1
        self.min_prime = (self.max_prime + 1) // 2

    def generate_p_and_q(self):
        self.q = gen_prime(self.min_prime, self.max_prime)
        self.p = gen_prime(self.min_prime, self.max_prime)
        # if abs(self.q - self.p) < self.min_prime // 5:
        #     self.generate_p_and_q()

    def calculate_n(self):
        self.n = self.q * self.p

    def calculate_lambda_n(self):
        self.lambda_n = int(lcm(self.p - 1, self.q - 1))

    def generate_e(self):
        number = 0
        while gcd(number, self.lambda_n) != 1:
            number = random.randrange(2, self.lambda_n + 1)
        self.e = number

    def calculate_d(self):
        self.d = pow(self.e, -1, self.lambda_n)


if __name__ == "__main__":
    new_RSA = RSA(64)
    print(f"range: {new_RSA.min_prime}, {new_RSA.max_prime} "
          f"\nnumbers: {new_RSA.q}, {new_RSA.p} "
          f"\nn: {new_RSA.n}"
          f"\nλ(n): {new_RSA.lambda_n}"
          f"\ne: {new_RSA.e}"
          f"\nd: {new_RSA.d}")
