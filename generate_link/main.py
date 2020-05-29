from pathlib import Path
from fire import Fire
from subprocess import Popen, run
from datetime import datetime

desktop_dir = Path.home().joinpath("Desktop")

now_date = "%s年%s月" % tuple(datetime.now().strftime("%Y|%m").split("|"))


def mkdir_and_link(path=Path(r"E:\data")):
    if type(path) is str:
        path = Path(path)
    data_dir_path = path.joinpath(now_date)
    data_dir_path.mkdir(exist_ok=True)
    cammand = ['mklink', '/J',
               str(desktop_dir.joinpath(now_date)), str(data_dir_path)]
    print(f"exec cammand {' '.join(cammand)}")
    run(cammand, shell=True)


def main():
    Fire(mkdir_and_link)
