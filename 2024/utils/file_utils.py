
class FileUtils:

    @staticmethod
    def read_file_as_lines(filename):

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file]
                return lines
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found")
            raise

        except IOError as e:
            print(f"Error reading the file: '{e}'")
            raise
