import shutil
import os
import sys


def delFolder(folder_path):
    # DELETE FOLDER, fname - FOLDER NAME
    shutil.rmtree(folder_path)
    print(f'Folder deleted {folder_path}')

def check_subfolders(folder_path):
    dirs = os.listdir(folder_path)
    for d in dirs:
        if d == 'env' or d == 'venv' or d == 'myvenv':
            shutil.rmtree(os.path.join(folder_path,d))
            print(f'Folder delted {os.path.join(folder_path, d)}')
        else:
            d_path = os.path.join(folder_path, d)
            if os.path.isdir(d_path):
                sub_dirs = os.listdir(d_path)
                for s_dir in sub_dirs:
                    sd_path = os.path.join(d_path, s_dir)
                    if s_dir == 'env' or s_dir == 'venv' or s_dir == 'myvenv':
                        shutil.rmtree(sd_path)
                        print(f'DELETE {sd_path}')
                    else:
                        sub_sub_dirs = os.listdir(os.path.join(sd_path, s_dir))
                        for ss_dir in sub_sub_dirs:
                            ss_path = os.path.join(sd_path, s_dir, ss_dir)
                            if ss_dir == 'env' or ss_dir == 'venv' or ss_dir == 'myvenv':
                                shutil.rmtree(os.path.join(ss_path))
                                print(f'Deleted {ss_path}')

def sub_check(folder_path):
    dirs = os.listdir(folder_path)
    for d in dirs:
        #while True:
       
        if d == 'env' or d == 'venv' or d == 'myvenv':
            shutil.rmtree(os.path.join(folder_path,d))
            print(f'Folder delted {os.path.join(folder_path, d)}')
        else:
            d_path = os.path.join(folder_path, d)


def main():
    folder_to_check = sys.argv[-1]
    print(f'Checking folder {folder_to_check}')
    dirs = os.listdir(folder_to_check)
    print(dirs)
    # check currnet folder
    for d in dirs:
        if os.path.isdir(d):
            check_subfolders(os.path.join(folder_to_check, d))
        if d == 'env' or d == 'venv' or d == 'myvenv':
            shutil.rmtree(os.path.join(folder_to_check, d))
            print(f'Folder Delted {d}')
main()
