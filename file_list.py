import os


class FileHandler:
    @staticmethod
    def list_files(path):
        files = []
        for dir_path, dir_names, file_names in os.walk(path):
            files += [os.path.join(dir_path, filename) for filename in file_names]
        return files

    @staticmethod
    def filter_files(files, extension):
        filtered_files = []
        for file in files:
            if file[len(extension) * -1:] in extension:
                filtered_files.append(file)
        return filtered_files
