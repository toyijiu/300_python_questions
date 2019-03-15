#print all of the files' path under a directory
import os
def print_directory_contents(sPath):
    for dir_child in os.listdir(sPath):
        dir_child_path = os.path.join(sPath,dir_child)
        if os.path.isdir(dir_child_path):
            print_directory_contents(dir_child_path)
        else:
            print(dir_child_path)

if __name__ == '__main__':
    print_directory_contents('C:\\Users\\wuuuxxia\\PycharmProjects')