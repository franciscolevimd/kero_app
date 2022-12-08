from kero.utils import files
from kero.crypto import keys

from cryptography.fernet import Fernet


def decrypt_file_content(file_path, key):
    """Returns decrypted content of a file.

    Keyword argumets:
    file_path -- Absolute path of the file to be decrypted.
    key -- Value key to decrypted the file.
    """
    with open(file_path, 'rb') as crypted_file:
        crypted_content = crypted_file.read()
        fernet_algorithm = Fernet(key)
        return fernet_algorithm.decrypt(crypted_content).decode('utf-8')


def decrypt_file(file_path, key_path, ofile_path=''):
    """Decrypts a file with a key file.

    Keyword argumets:
    file_path -- Absolute path of the file to be decrypted.
    key_path -- Absolute path where the key is located.
    ofile_path -- Path of the output file. (default is a empty string)
    """
    ofile_path = files.check_output_file_name(file_path, ofile_path)
    key = keys.load_key(key_path)
    decrypted_content = decrypt_file_content(file_path, key)
    with open(ofile_path, 'w') as file_decrypted:
        file_decrypted.write(decrypted_content)
