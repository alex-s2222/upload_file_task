from upload_file.utils.choices import FileType

def choise_type_file(file_name):
    if file_name.endswith(FileType.IMAGE_FILE):
        return {'type': 'image'}
    elif file_name.endswith(FileType.JSON_FILE):
        return {'type': 'json'}
    elif file_name.endswith(FileType.TEXT_FILE):
        return {'type': 'text'}