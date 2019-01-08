import logging
import logging.config
import sys

from multiprocessing.pool import ThreadPool
from os import path
from urllib.parse import urlparse, unquote

import requests
import yaml

from .curse import get_mod_link
from .logging import config_logger

logger = logging.getLogger()


def download(mod_name, mod_version, link):
    if link is None:
        logger.error(f'Cannot download {mod_name} {mod_version}')
        return

    logger.info(f'Downloading {mod_name} - {mod_version}')

    resp = requests.get(link)
    filename = resp.headers.get('Content-Disposition')
    if filename is None:
        filename = unquote(path.basename(urlparse(resp.url).path))

    with open(path.join('mods', filename), 'wb') as fp:
        fp.write(resp.content)


def main():
    config_logger()
    config_file = sys.argv[1]

    pool = ThreadPool(4)

    if not path.isdir('mods'):
        logger.error('Cannot find "mods" directory')
        exit(1)

    with open(config_file) as fp:
        config = yaml.load(fp)

    link_map = pool.map(
        lambda x: get_mod_link(config['mc_version'], *x),
        config['mod_list'].items()
    )

    pool.map(
        lambda x: download(*x),
        link_map
    )

    pool.close()
