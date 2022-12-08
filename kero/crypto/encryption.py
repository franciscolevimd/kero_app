from kero.utils import files
from kero.crypto import keys

from cryptography.fernet import Fernet


def encrypt_file_content(file_path, key):
    """Returns encrypted content of a file.

    Keyword argumets:
    file_path -- Absolute path of the file to be encrypted.
    key -- Value key to encrypted the file.
    """
    with open(file_path, 'rb') as original_file:
        fernet_algorithm = Fernet(key)
        file_content = original_file.read()
        return fernet_algorithm.encrypt(file_content)


def encrypt_file(file_path, key_path, ofile_path=''):
    """Encrypts a file with a key file.

    Keyword argumets:
    file_path -- Absolute path of the file to be encrypted.
    key_path -- Absolute path where the key is located.
    ofile_path -- Path of the output file. (default is a empty string)
    """
    ofile_path = files.check_output_file_name(file_path, ofile_path, '.ker')
    key = keys.load_key(key_path)
    encrypted_content = encrypt_file_content(file_path, key)
    with open(ofile_path, 'wb') as file_encrypted:
        file_encrypted.write(encrypted_content)
