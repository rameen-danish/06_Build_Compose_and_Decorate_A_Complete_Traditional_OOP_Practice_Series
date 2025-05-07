class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    # __iter__ method returns the iterator object itself
    def __iter__(self):
        return self

    # __next__ method defines the iteration behavior
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when we reach 0 or below
        else:
            self.current -= 1
            return self.current

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)
