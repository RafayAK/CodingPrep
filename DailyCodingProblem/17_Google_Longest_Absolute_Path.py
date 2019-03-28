'''
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a
file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''


import os

def rics_version(path_str):
    if not path_str:
        return 0

    dirs, max_len = [None], 0
    for token in path_str.split('\n'):

        tabs = token.count('\t')
        # while token[tabs] == '\t':
        #     tabs += 1

        if tabs > len(dirs):
            raise RuntimeError('Malformed path string: nesting more than one level at a time.')

        if tabs == len(dirs):  # go one level deeper

            if '.' in dirs[-1]:  # container is a file
                raise RuntimeError('Malformed path string: a file cannot contain something else.')

            dirs.append(None)  # make room for the new path item

        else:  # tabs < level, ascend

            dirs = dirs[:tabs + 1]

        dirs[-1] = str.strip(token)
        if '.' in dirs[-1]:  # path ends with a file
            max_len = max(max_len, len('/'.join(dirs)))

    return max_len


def find_longest_abs_path(filesys):
    longest_fs = []  # array to hold all calculated lengths
    longest = 0
    base = None
    current_file = None
    current_path = None
    current_level = None
    for f in filesys.split('\n'):
        if base is None:
            base = f
            current_path = base
            current_file = base
            current_level = 0
            if '.' in current_file:
                # found a data file
                longest_fs.append(len(os.path.join(current_path)))
                base = None
                current_file = None
                current_path = None
                current_level = None
            continue


        count_level = f.count('\t')
        current_file = f.lstrip('\t')



        if current_level < count_level:
            # go deeper in directory
            if '.' in current_file:
                # found a data file
                longest_fs.append(len(os.path.join(current_path,current_file)))
            else:
                current_path = os.path.join(current_path,current_file)
                current_level = count_level
        elif count_level < current_level or current_level == count_level:
            # directory ended
            # longest_fs.append(current_path)  # append path uptill now
            # came out directory
            current_path = os.path.join(base, current_file)
            current_level = count_level

    return max(longest_fs)


def lengthLongestPath(input_path):
        """
        :type input_path: str
        :rtype: int
        """
        max_length = 0
        level_length = {-1: 0}

        for line in input_path.split('\n'):
            current_path = line.lstrip('\t')
            current_level = line.count('\t')

            if '.' in line:
                # No need to store level_length as we are at a leaf node
                current_level_length = level_length[current_level - 1] + len(current_path)
                max_length = max(max_length, current_level_length)

            else:
                # Store the total length of the path to the current level
                level_length[current_level] = level_length[current_level - 1] + len('/') + len(current_path)

        return max_length


def longest_abs_path(filesys):
    max_length = 0
    dict_level_to_path_lengths = {-1:0}  # initially  level(-1)->path_len(0) for the first path in directory
                                         # main paths start from level 0

    for dir in filesys.split('\n'):
        current_level = dir.count('\t')
        current_path = dir.lstrip('\t')

        if '.' in current_path:
            # no need to store directory path length
            current_level_length = dict_level_to_path_lengths[current_level -1] + len(current_path)
            max_length = max(max_length, current_level_length)

        else:
            # store the length of the directory on the current level
            dict_level_to_path_lengths[current_level] = dict_level_to_path_lengths[current_level -1] + len('/') + len(current_path)

    return max_length


if __name__ == '__main__':
    # fs = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    fs2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    #fs3 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\t\t\thello.pew"
    #fs4 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\t\tsubsubsubdir1\n\t\t\t\tyo.txt\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\t\t\thello.pew"
    test = "dir\n    file.txt"
    print(fs2)
    l = longest_abs_path(fs2)#lengthLongestPath(fs2)#rics_version(fs)
    print(l)
