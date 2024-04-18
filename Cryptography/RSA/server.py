import socket
import pickle
import rsa

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server listening on", PORT)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                received_data = pickle.loads(data)
                public_key = received_data['public_key']
                ciphertext = received_data['ciphertext']
                plaintext = rsa.decrypt(public_key, ciphertext)
                print(f"Encrypted message received: {ciphertext}")
                print(f"Decrypted message: {plaintext}")
                conn.sendall(b"Message received and decrypted successfully!")

if __name__ == "__main__":
    main()
