#!/usr/bin/env python3

import os
import sys

def change_wallpaper(wallpaper):

    config_path = os.path.expanduser("~/.config/N1XA-CLI/config/current_wallpaper.conf")
    wallpaper_path = os.path.expanduser(f"~/Pictures/wallpapers/{wallpaper}")

    # Ensure file exists
    if not os.path.isfile(wallpaper_path):
        print(f"Error: wallpaper not found → {wallpaper_path}")
        sys.exit(1)
    current_wallpaper = f"$current_wallpaper = {wallpaper_path}"
     


    with open(config_path, 'w') as f:
        f.write(current_wallpaper)

    # Reload Hyprlock
    os.system("pkill -USR2 hyprlock")
    print(sys.argv[1])

if __name__ == "__main__":
    change_wallpaper(sys.argv[1])

