import os
import sys


class LineOfMD5DeepFile:
    # this is a line of a md5 deep file
    def __init__(self, line):
        self.file_line = line.strip()
        self.file_hash = line[:32].strip()
        self.file_path = line[33:].strip()


def read_md5deep_file(my_path):
    # load file
    if not os.path.isfile(file_left_path):
        print("Fatal error: Cannot read %s." % my_path)
        print(usage_text)
        exit(1)

    my_file = open(my_path, 'r')
    my_lines = my_file.readlines()
    my_parsed_lines = []
    for a_line in my_lines:
        my_parsed_lines.append(LineOfMD5DeepFile(a_line))
    
    return my_parsed_lines


def md5_deep_compare(left_file_parsed: [LineOfMD5DeepFile], right_file_parsed: [LineOfMD5DeepFile]):

    count_lines = 0
    count_hashes = 0
    count_path = 0

    for left_item in left_file_parsed:
        
        found_line = False
        found_hash = False
        found_path = False
        
        for right_item in right_file_parsed:
            if left_item.file_line == right_item.file_line:
                print("identical line: " + left_item.file_path)
                found_line = True
            elif left_item.file_hash == right_item.file_hash:
                print("identical hash: " + left_item.file_path + " + " + right_item.file_path)
                found_hash = True
            elif left_item.file_path == right_item.file_path:
                print("identical path: " + left_item.file_path + " + " + right_item.file_path)
                found_path = True

        if found_line:
            count_lines += 1

        if found_hash:
            count_hashes += 1
            
        if found_path:
            count_path += 1

    print()
    print("Left file lines:  %s" % (str(len(left_file_parsed))))
    print("Right file lines: %s" % (str(len(right_file_parsed))))
    print()
    print("Left file lines found in right file: %s" % (str(count_lines)))
    print("Left file hashes found in right file (but different name): %s" % (str(count_hashes)))
    print("Left file names found in right file (but different hash):  %s" % (str(count_path)))


if __name__ == '__main__':
    # settings
    # reading arguments
    num_required_args = 3
    usage_text = "Usage: " + str(sys.argv[0]) + " <path to first md5 file> <path to second md5 file>"
    
    if len(sys.argv) != num_required_args:
        print("Fatal error: This program needs exactly " + str(num_required_args) + " arguments")
        print(usage_text)
        exit(1)
    
    file_left_path = str(sys.argv[1])
    file_right_path = str(sys.argv[2])

    print("Left file:   %s" % file_left_path)
    print("Right file:  %s" % file_right_path)
    print()

    left_parsed = read_md5deep_file(file_left_path)
    right_parsed = read_md5deep_file(file_right_path)
    
    md5_deep_compare(left_parsed, right_parsed)
    



