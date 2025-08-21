import random
import string

def generate_fake_mirror():
    base = "kraken-darknet"
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"https://{base}-{suffix}.top"

print("🔗 Генератор зеркал Kraken Darknet (фейк):")
for _ in range(5):
    print(generate_fake_mirror())
