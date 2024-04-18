# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def digital_signature_sign(p, q, g, x, k, message):
    # Calculate y
    y = pow(g, x, p)
    # Calculate H(M)
    H_M = message
    # Signing
    r1 = pow(g, k, p) % q
    s1 = (mod_inverse(k, q) * (H_M + x * r1)) % q
    return r1, s1

def digital_signature_verify(p, q, g, y, message, r1, s1):
    # Verification
    w = mod_inverse(s1, q)
    u1 = (message * w) % q
    u2 = (r1 * w) % q
    # Calculate v
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
    print("v :",v)
    # Check if v equals r1
    if v == r1:
        return True
    else:
        return False

# Parameters
p = 307
q = 53
g = 70
x = 30
k = 7
message = 51

# Signing
r1, s1 = digital_signature_sign(p, q, g, x, k, message)
print("r1:", r1)
print("s1:", s1)

# Verification
y = pow(g, x, p)
is_verified = digital_signature_verify(p, q, g, y, message, r1, s1)
print("Signature verified:", is_verified)

