"""
This file demonstrates an algorithm finding a target number.
The program will exponentially increase until it overshoots,
which effectively finds the minimum and maximum.
From there, it binary searches until it finds the number
to the given tolerance.
"""
# Decimal package for arbitrary-precision arithmetic.
from decimal import Decimal, getcontext

class Detector:
    # Target is the number wanted to find
    # Guess is teh starting guess
    # Tolerance is the stopping point
    # Precision is the number of significant difits Decimal should track
    def detect(self, target, guess=1.0, tolerance='1e-1000', precision=100):
        getcontext().prec = precision # Sets arithmetic precision for all Decimal operations

        # Converts inputs to Decimal and turns them into strings to ensure digits aren't lost
        target = Decimal(str(target))
        guess = Decimal(str(guess))
        tolerance = Decimal(str(tolerance))

        # Tracks tries
        tries = 0

        # PHASE 1: Exponential search to find the bracket
        minimum, maximum = None, None

        # If target is negative, move down
        if target < 0:
            guess = -abs(guess)
            direction = -1
        else:
            direction = 1

        while True:
            tries += 1

            # If the correct number was overshot, the bracket has been found
            if (direction == 1 and guess >= target) or \
                (direction == -1 and guess <= target):
                if direction == 1:
                    minimum = guess / 2
                    maximum = guess
                else:
                    minimum = guess
                    maximum = guess / 2
                break

            guess *= 2  # Grow exponentially


        # PHASE 2: Binary search
        while abs(guess - target) > tolerance: # This will loop until it finds the number withing the tolerance
            tries += 1
            guess = (minimum + maximum) / 2 # Binary searches
            if guess < target:
                minimum = guess
            else:
                maximum = guess
        return guess

if __name__ == "__main__":
    detector = Detector()
    precise_number = detector.detect('-1234567890.0987654321')
    print(precise_number)
