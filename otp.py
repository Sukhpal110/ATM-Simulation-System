import random

otp = random.randint(1000, 9999)

print(otp)


def generate_otp(length=4):
    otp = ''
    for _ in range(length):
        otp += str(random.randint(0, 9))  # Generates random digits from 0 to 9
    return otp

otp = generate_otp()
print("Your OTP is:", otp)