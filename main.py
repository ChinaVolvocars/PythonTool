import os
import chardet

"""
使用的版本 python3.7.0
"""

# 以下路径是在windows系统，mac和Linux不是这样的。

target_file_dir_lib = "C:\\Users\\Tiger\\Desktop\\pythonProject\\lib"
target_file_dir_docs = "C:\\Users\\Tiger\\Desktop\\pythonProject\\docs"


def modify_folder_name(file_path, old_str, new_str):
    """
    修改文件夹名字
    :param new_str:
    :param old_str:
    :param file_path:
    :return:
    """
    for filepath, dirnames, filenames in os.walk(file_path):
        print(filepath)
        if old_str in filepath:
            os.rename(filepath, filepath.replace(old_str, new_str))
            print('### 文件夹名字修改完成 ###', old_str, new_str)
    print('### 文件夹名字修改完成 ###')


def modify_file_name(file_path, old_str, new_str):
    """
    修改文件名字
    :param new_str:
    :param old_str:
    :param file_path:
    :return:
    """
    for filepath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            join = os.path.join(filepath, filename)
            # 修改文件的名字
            if old_str in join:
                os.rename(join, join.replace(old_str, new_str))
                print('文件名字修改完成', old_str, new_str)
            else:
                print("没有要修改的文件名字", old_str)
    print('### 所有文件名字修改完成 ###')


def modify_content(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:

    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def modify_lib_files_contents(target_path):
    """
    替换文件内容
    :param target_path:
    :return:
    """
    for filepath, dirnames, filenames in os.walk(target_path):
        for filename in filenames:
            join = os.path.join(filepath, filename)
            print('### 开始修改文件内容 ###', filename)
            modify_content(join, 'bruno', 'owl')
            modify_content(join, 'Brn', 'Owl')
            modify_content(join, 'brn_', 'owl_')
            modify_content(join, 'package:bruno', 'package:owl')
            modify_content(join, 'Brn', 'Owl')
            print('### 修改文件内容结束 ###', filename)


def modify_docs_files_contents(target_path):
    """
    替换文件内容
    :param target_path:
    :return:
    """
    for filepath, dirnames, filenames in os.walk(target_path):
        for filename in filenames:
            join = os.path.join(filepath, filename)

            b = open(join, 'rb')
            read = b.read()
            print('文件编码格式', chardet.detect(read), filename)
            if '.md' in filename:
                print('### 开始修改文件内容 ###', filename)
                modify_content(join, 'bruno', 'owl')
                modify_content(join, 'Bruno', 'Owl')
                modify_content(join, 'Brn', 'Owl')
                print('### 修改文件内容结束 ###', filename)
            else:
                print('其他文件', filename)
    print('所有文件内容修改完成')


def executeLib():
    modify_folder_name(target_file_dir_lib, 'brn', 'owl')
    modify_file_name(target_file_dir_lib, 'brn', 'owl')
    modify_file_name(target_file_dir_lib, 'bruno', 'owl')
    modify_file_name(target_file_dir_lib, 'Brn', 'Owl')
    modify_lib_files_contents(target_file_dir_lib)
    print('### 执行完毕 ###')


def executeDocs():
    modify_folder_name(target_file_dir_docs, 'Brn', 'Owl')
    modify_file_name(target_file_dir_docs, 'bruno', 'owl')
    modify_file_name(target_file_dir_docs, 'Brn', 'Owl')
    modify_docs_files_contents(target_file_dir_docs)
    print('### 执行完毕 ###')


if __name__ == '__main__':
    executeLib()
    executeDocs()
