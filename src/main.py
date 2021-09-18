# coding: utf-8

import configparser
import os
import sys


def main():
    workpath = os.getcwd()
    genshinpath = os.path.join(workpath, "Genshin Impact")
    inipath = os.path.join(genshinpath, "config.ini")

    config = configparser.ConfigParser()
    config.read(inipath)
    path_without_drive = os.path.splitdrive(config["launcher"]["game_install_path"])[1]
    config["launcher"]["game_install_path"] =  os.path.join(os.path.splitdrive(workpath)[0], path_without_drive)
    with open(inipath, "w", encoding="utf-8") as f:
        config.write(f, space_around_delimiters=False)

    os.startfile(os.path.join(genshinpath, "launcher.exe"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
