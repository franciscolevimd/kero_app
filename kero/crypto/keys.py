from cryptography.fernet import Fernet


def build_key(file_path='secret.key'):
    """Generates a key and save into a binary file.

    Keyword argumets:
    file_path -- Absolute path where the file is saved. (default secret.key)
    """
    with open(file_path, 'wb') as secret_file:
        secret_file.write(Fernet.generate_key())


def load_key(key_path):
    """Returns the value of a key from a binary file.

    Keyword argumets:
    file_path -- Absolute path where the file is located.
    """
    with open(key_path, 'rb') as key_file:
        return key_file.read()
