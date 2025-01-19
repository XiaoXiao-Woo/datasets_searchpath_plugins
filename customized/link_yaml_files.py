import os
import glob
import subprocess
import click
from pathlib import Path


@click.command()
@click.argument("source_dir", nargs=-1)
def link_yaml_files(source_dir):
    source_dir = source_dir[0]
    target_dir = os.path.dirname(__file__) + "/conf"
    print(f"source_directory: {source_dir}")
    print(f"target_directory: {target_dir}")
    # 遍历源目录
    for file in Path(source_dir).rglob("*.yaml"):
        basename = Path(os.path.basename(file))
        file_dir = Path(os.path.dirname(file).replace(source_dir, ""))
        link_path = target_dir / file_dir.relative_to(file_dir.anchor) / basename
        if os.path.exists(link_path):
            os.remove(link_path)
        os.makedirs(os.path.dirname(link_path), exist_ok=True)
        # 创建符号链接
        subprocess.run(["ln", "-s", file, link_path], check=True)
        print(f"Linked: {file} -> {link_path}")


if __name__ == "__main__":
    link_yaml_files(["/home/dsq/nips/conf"])
