import math
import string

def password_crack_time(password, guesses_per_second=1e10):
    length = len(password)
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    
    if pool == 0:
        return 0
    
    entropy = length * math.log2(pool)
    total_combinations = 2 ** entropy
    avg_attempts = total_combinations / 2
    seconds = avg_attempts / guesses_per_second

    def format_time(seconds):
        units = [
            ("years", 60 * 60 * 24 * 365),
            ("days", 60 * 60 * 24),
            ("hours", 60 * 60),
            ("minutes", 60),
            ("seconds", 1)
        ]
        result = []
        for name, count in units:
            value = int(seconds // count)
            if value:
                result.append(f"{value} {name}")
                seconds %= count
        return ", ".join(result) if result else "less than 1 second"
    
    return format_time(seconds)
