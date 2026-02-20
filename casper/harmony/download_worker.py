"""A utility for downloading multiple granules simultaneously"""

import re
from pathlib import Path
from urllib.parse import urlparse

from harmony_service_lib.logging import build_logger
from harmony_service_lib.util import download


def download_file(
    url: str,
    destination_dir: str,
    access_token: str,
    cfg: dict,
) -> str:
    """
    A method to be executed in a separate process which processes the url_queue
    and places paths to completed downloads into the path_list. Downloads are
    handled by harmony.util.download

    Parameters
    ----------
    url_queue : queue.Queue
        URLs to process - should be filled from start and only decreases
    path_list : list
        paths to completed file downloads
    destination_dir : str
        output path for downloaded files
    access_token : str
        access token as provided in Harmony input
    cfg : dict
        Harmony configuration information
    """

    logger = build_logger(cfg)

    path = Path(download(url, destination_dir, logger=logger, access_token=access_token, cfg=cfg))
    filename_match = re.match(r".*\/(.+\..+)", urlparse(url).path)

    if filename_match is not None:
        filename = filename_match.group(1)
        dest_path = path.parent.joinpath(filename)
        path = path.rename(dest_path)
    else:
        logger.warning("Origin filename could not be ascertained - %s", url)

    return str(path)
