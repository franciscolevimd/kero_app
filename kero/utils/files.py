def check_output_file_name(input_path, output_path, extension='.out'):
    """Returns the path of the file where the resulting content will be saved.

    Keyword argumets:
    input_path -- Absolute path of the file to be processed.
    output_path -- Absolute path to save the processed file.
    extension -- Extension of the output file. (default '.out')
    """
    if not output_path:
        return input_path + extension
    return output_path
