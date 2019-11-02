import os
import csv
import requests
import datetime
import progressbar
import configparser
from colorama import Fore
from colorama import Style

config = configparser.ConfigParser()
module_dir = os.path.dirname(__file__)
config_path = os.path.join(module_dir, 'config.ini')
config.read(config_path)

api_key = config.get('keys', 'api')
path = config.get('params', 'path')
playlist = config.get('params', 'playlist')

def fetch_playlist_name(playlist_id):
    url = "https://www.googleapis.com/youtube/v3/playlists"
    params = {
        "key": api_key,
        "id": playlist_id,
        "part": "snippet",
        "maxResults": "1"
    }
    res = requests.get(url, params=params).json()

    return res["items"][0]["snippet"]["title"]

def fetch_playlist_page(playlist_id, page_token=None):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "key": api_key,
        "pageToken": page_token,
        "playlistId": playlist_id,
        "part": "snippet",
        "maxResults": "50"
    }
    res = requests.get(url, params=params).json()

    items = { i["snippet"]["resourceId"]["videoId"]: i["snippet"]["title"] for i in res["items"] }
    next_page = res["nextPageToken"] if "nextPageToken" in res else None
    count = res["pageInfo"]["totalResults"]

    return (items, next_page, count)

def fetch_playlist(playlist_id):
    THRESHOLD = 100
    (fetched, next, count) = fetch_playlist_page(playlist_id)

    if count > THRESHOLD:
        progress = progressbar.ProgressBar(max_value=count)

    while next != None:
        if count > THRESHOLD:
            progress.update(len(fetched))

        (items, next, count) = fetch_playlist_page(playlist_id, next)
        fetched.update(items)

    if count > THRESHOLD:
        progress.update(len(fetched))
        progress.finish()

    return fetched

def print_head_fetching(id, title):
    p0 = f"{Style.RESET_ALL}{Fore.RED}▶{Style.RESET_ALL}"
    p1 = "{:60}".format(f"{Style.RESET_ALL}Fetching {Fore.RED}{title}{Style.RESET_ALL} playlist...")
    p2 = f"{Style.RESET_ALL}{Style.DIM}[{id}]{Style.RESET_ALL}"
    print(p0, p1, p2)

def print_err_plnotfound(id):
    p0 = f"{Style.RESET_ALL}{Fore.RED}▶{Style.RESET_ALL}"
    p1 = "{:60}".format(f"{Style.RESET_ALL}Could not access {Fore.RED}Unknown{Style.RESET_ALL} playlist.")
    p2 = f"{Style.RESET_ALL}{Style.DIM}[{id}]{Style.RESET_ALL}"
    print(p0, p1, p2)

def print_info_added(id, title):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}+{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}New song {Fore.GREEN}{title}{Style.RESET_ALL} found"
    p2 = f"{Style.RESET_ALL}{Style.DIM}[{id}]{Style.RESET_ALL}"
    print("  ", p0, p1, p2)

def print_info_rename(id, old, new):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}i{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}Song was renamed from {Fore.BLUE}{old}{Style.RESET_ALL} to {Fore.BLUE}{new}{Style.RESET_ALL}"
    p2 = f"{Style.RESET_ALL}{Style.DIM}[{id}]{Style.RESET_ALL}"
    print("  ", p0, p1, p2)

def print_info_missing(id, title):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.RED}×{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}{Fore.RED}{title}{Style.RESET_ALL} is missing from the playlist{Style.RESET_ALL}"
    p2 = f"{Style.RESET_ALL}{Style.DIM}[{id}]{Style.RESET_ALL}"
    print("  ", p0, p1, p2)

def print_info_nochanges():
    print("  (no changes)")

def print_warn_filenotfound(file):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}!{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}Could not find file {Fore.YELLOW}{file}{Style.RESET_ALL}"
    print("  ", p0, p1)

def print_warn_createfile(file):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}!{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}Creating new file {Fore.YELLOW}{file}{Style.RESET_ALL}"
    print("  ", p0, p1)

def print_warn_writingfile(file):
    p0 = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.YELLOW}!{Style.RESET_ALL}"
    p1 = f"{Style.RESET_ALL}Writing to file {Fore.YELLOW}{file}{Style.RESET_ALL}"
    print("  ", p0, p1)

def is_empty(list):
    return len(list) == 0

def read_playlist_file(playlist_id):
    """Reads in a csv file of playlist information.

    If there is no file, or the file is empty, the function
    will return an empty list.The header of the file is 
    always the first row and formatted as:
    #file_type, version_id, playlist_origin, count, playlist_id

    Parameters
    ----------
    playlist_id : str
        The playlist id, used to find the csv file on disk.

    Returns
    -------
    list
        a list of all the song items, formatted as [flag, video_id, title]
    """

def write_playlist_file(rows, playlist_id):
    """Writes in a csv file the playlist information and songs.

    If there is no file, the function will create a new file. The
    header of the file is always the first row and formatted as:
    #file_type, version_id, playlist_origin, count, playlist_id

    Parameters
    ----------
    rows : list
        The songs to write to the file, formatted as: [flag, video_id, title]
    playlist_id : str
        The playlist id, used to find the csv file on disk.
    """

def find_added_items(master, new_items):
    """Compares the items from the new_items list and master list,
    and finds all the added items.

    Parameters
    ----------
    master: list
        list of all items, formatted as [flag, video_id, title]
    new_items : dict
        list of new items, formatted as { video_id : [flag, video_id, title] }

    Returns
    -------
    list
        a list of all the added songs, formatted as (video_id, title)
    """

def find_missing_items(master, new_items):
    """Compares the items from the new_items list and master list,
    and finds all the missing items.

    Parameters
    ----------
    master: list
        list of all items, formatted as [flag, video_id, title]
    new_items : dict
        list of new items, formatted as { video_id : [flag, video_id, title] }

    Returns
    -------
    list
        a list of all the missing songs, formatted as (video_id, title)
    """

def find_renamed_items(master, new_items):
    """Compares the items from the new_items list and master list,
    and finds all the renamed items.

    Parameters
    ----------
    master: list
        list of all items, formatted as [flag, video_id, title]
    new_items : dict
        list of new items, formatted as { video_id : [flag, video_id, title] }

    Returns
    -------
    list
        a list of all the renamed songs, formatted as (video_id, old_title, new_title)
    """

def main():
    try:
        name = fetch_playlist_name(playlist)
        print_head_fetching(playlist, name)
    except:
        print_err_plnotfound(playlist)
        continue

    master = read_playlist_file(playlist)
    new = fetch_playlist(playlist)

    fname = f"{playlist}.ipl"
    fpath = os.path.join(path, fname)
    if not os.path.exists(fpath):
        print_warn_filenotfound(fname)

    added = find_added_items(master, new)
    removed = find_missing_items(master, new)
    renamed = find_renamed_items(master, new)

    for item in added:
        id = item[0]
        title = item[1]
        print_info_added(id, title)

    for item in removed:
        id = item[0]
        title = item[1]
        print_info_missing(id, title)

    for item in renamed:
        id = item[0]
        old_title = item[1]
        new_title = item[2]
        print_info_rename(id, old_title, new_title)

    if not is_empty(added) or not is_empty(removed):
        if not os.path.exists(fpath):
            print_warn_createfile(fname)
        print_warn_writingfile(fname)
        write_playlist_file(master, playlist)

    elif is_empty(renamed):
        print_info_nochanges()

if __name__ == "__main__":
    main()
