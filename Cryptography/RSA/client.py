import socket
import pickle
import rsa

HOST = '127.0.0.1'
PORT = 65432

def main():
    p = 61
    q = 53
    public_key, private_key = rsa.generate_keypair(p, q)
    message = "Hello, RSA!"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = {'public_key': public_key, 'ciphertext': rsa.encrypt(public_key, message)}
        s.sendall(pickle.dumps(data))
        print(f"Encrypted message sent: {data['ciphertext']}")
        response = s.recv(1024)
        print(response.decode())

if __name__ == "__main__":
    main()
