import requests

from lxml import html

GAME_VERSION_MAP = {
    '1.12.2': '2020709689:6756',
    '1.12.1': '2020709689:6711',
    '1.12': '2020709689:6580',
    '1.11.2': '2020709689:6452',
    '1.11': '2020709689:6317',
    '1.10.2': '2020709689:6170',
    '1.10': '2020709689:6144',
    '1.9.4': '2020709689:6084',
    '1.9': '2020709689:5946',
    '1.8.9': '2020709689:5806',
    '1.8.8': '2020709689:5703',
    '1.8': '2020709689:4455',
    '1.7.10': '2020709689:4449',
    '1.7.2': '2020709689:361',
    '1.6.4': '2020709689:326',
    '1.6.2': '2020709689:320',
    '1.6.1': '2020709689:318',
    '1.5.2': '2020709689:312',
    '1.5.1': '2020709689:280',
    '1.5.0': '2020709689:279',
}


def get_phase(td_elem):
    div = td_elem.find('div')
    classes = div.get('class').split()
    return next(filter(lambda x: x.endswith('-phase'), classes)).replace('-phase', '')


def get_mod_link(mc_version, mod_name, release_type):
    if mc_version not in GAME_VERSION_MAP:
        raise ValueError(f'Versino {mc_version} is currently not supported')

    # TODO: Fetch next page
    URL = f'https://minecraft.curseforge.com/projects/{mod_name}/files'
    resp = requests.get(URL, {
        'filter-game-version': GAME_VERSION_MAP[mc_version]
    })
    doc = html.fromstring(resp.text)
    doc.make_links_absolute(URL)

    for tr in doc.cssselect('table.listing tbody tr'):
        phase = get_phase(
            tr.cssselect('td.project-file-release-type')[0])
        mod_version = tr.cssselect('td.project-file-name a[data-name]')[0].get('data-name')
        download_link = tr.cssselect('td:nth-child(2) a')[0].get('href')
        # TODO: parse additional versions

        if phase == release_type:
            link = download_link
            break
    else:
        mod_version = None
        link = None

    return (mod_name, mod_version, link)
