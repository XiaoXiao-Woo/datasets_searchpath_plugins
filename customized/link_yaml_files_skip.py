import os
import glob
import subprocess
import click


@click.command()
@click.argument("source_dir", nargs=-1)
def link_yaml_files(source_dir):
    source_dir = source_dir[0]
    target_dir = os.path.dirname(__file__) + "/conf"
    print(f"source_directory: {source_dir}")
    print(f"target_directory: {target_dir}")
    dirs = [
        os.path.basename(v) for v in glob.glob(source_dir + "/*") if os.path.isdir(v)
    ]
    # 遍历源目录
    for file in os.listdir(source_dir):
        if file.endswith(".yaml"):
            for dir in dirs:
                source_file_path = os.path.join(source_dir, file)
                if "dataset" in file:
                    link_path = os.path.join(target_dir, dir, file)
                else:
                    link_path = os.path.join(target_dir, dir, "base", file)
                if os.path.exists(link_path):
                    os.remove(link_path)
                os.makedirs(os.path.dirname(link_path), exist_ok=True)
                # 创建符号链接
                subprocess.run(["ln", "-s", source_file_path, link_path], check=True)
                print(f"Linked: {source_file_path} -> {link_path}")


# if __name__ == "__main__":
#     # 示例用法
#     source_directory = os.path.dirname(__file__)  # 替换为源目录路径
#     target_directory = os.path.dirname(__file__)  # 替换为目标目录路径

#     link_yaml_files(source_directory, target_directory)
