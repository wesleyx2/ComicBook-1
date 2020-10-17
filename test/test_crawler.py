import logging

from onepiece.comicbook import ComicBook

logger = logging.getLogger()

DEFAULT_PROXY = 'socks5://127.0.0.1:1082'


def _test_crawl_comicbook(site, comicid=None, chapter_number=1, proxy=None):
    comicbook = ComicBook.create_comicbook(site=site, comicid=comicid)
    if proxy:
        comicbook.crawler.get_session().set_proxy(proxy)

    comicbook.start_crawler()
    chapter = comicbook.Chapter(chapter_number=chapter_number)
    assert len(chapter.image_urls) > 0

    logger.info(chapter.to_dict())
    logger.info(comicbook.to_dict())

    result = comicbook.search(name=comicbook.crawler.DEFAULT_SEARCH_NAME)
    assert len(result.to_dict()) > 0
    return comicbook, chapter


def test_qq():
    # 海贼王  URL: https://ac.qq.com/Comic/ComicInfo/id/505430
    _test_crawl_comicbook(site='qq')


def test_u17():
    # 雏蜂 URL: http://www.u17.com/comic/195.html
    _test_crawl_comicbook(site='u17')


def test_bilibili():
    # 航海王 URL: https://manga.bilibili.com/detail/mc24742
    _test_crawl_comicbook(site='bilibili')


def test_kuaikan():
    # 航海王 URL: https://www.kuaikanmanhua.com/web/topic/1338/
    _test_crawl_comicbook(site='kuaikan')


def test_manhuagui():
    # 鬼灭之刃 URL: https://www.manhuagui.com/comic/19430
    _test_crawl_comicbook(site='manhuagui', proxy=DEFAULT_PROXY)


def test_18comic():
    _test_crawl_comicbook(site='18comic', proxy=DEFAULT_PROXY)


def test_nhentai():
    _test_crawl_comicbook(site='nhentai', proxy=DEFAULT_PROXY)


def test_wnacg():
    _test_crawl_comicbook(site='wnacg', proxy=DEFAULT_PROXY)
