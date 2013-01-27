import base
from category import GetCategory
from rand import GetRandom
from protection import GetProtections
from links import GetBacklinks, GetLanguageLinks, GetInterwikiLinks
from feedback import GetFeedbackV4, GetFeedbackV5
from revisions import GetRevisionInfos

PDB_ALL = False
PDB_ERROR = False

def call_and_ret(func):
    try:
        ret = func()
    except Exception as e:
        if PDB_ERROR:
            import pdb;pdb.post_mortem()
        raise
    if PDB_ALL:
        import pdb;pdb.set_trace()
    return ret


def test_category_basic():
    get_2k_featured = GetCategory('Featured_articles', 2000)
    pages = call_and_ret(get_2k_featured)
    return len(pages) == 2000


def test_single_prot():
    get_coffee_prot = GetProtections('Coffee')
    prots = call_and_ret(get_coffee_prot)
    return len(prots) == 1


def test_multi_prots_list():
    get_prots = GetProtections(['Coffee', 'House'])
    prots = call_and_ret(get_prots)
    return len(prots) == 2


def test_multi_prots_str():
    get_prots = GetProtections('Coffee|House')
    prots = call_and_ret(get_prots)
    return len(prots) == 2


def test_backlinks():
    get_bls = GetBacklinks('Coffee', 10)
    bls = call_and_ret(get_bls)
    return len(bls) == 10


def test_random():
    get_fifty_random = GetRandom(50)
    pages = call_and_ret(get_fifty_random)
    return len(pages) == 50


def test_lang_links():
    get_coffee_langs = GetLanguageLinks('Coffee', 5)
    lang_list = call_and_ret(get_coffee_langs)
    return len(lang_list) == 5


def test_interwiki_links():
    get_coffee_iwlinks = GetInterwikiLinks('Coffee', 5)
    iw_list = call_and_ret(get_coffee_iwlinks)
    return len(iw_list) == 5


def test_feedback_v4():
    get_v4 = GetFeedbackV4(604727)
    v4_list = call_and_ret(get_v4)
    return len(v4_list) > 1


def test_feedback_v5():
    get_v5 = GetFeedbackV5(604727)
    v5_list = call_and_ret(get_v5)
    return isinstance(v5_list, list)


def test_revisions():
    get_revs = GetRevisionInfos('Coffee', 10)
    rev_list = call_and_ret(get_revs)
    return len(rev_list) == 10


def test_missing_revisions():
    get_revs = GetRevisionInfos('Coffee_lololololol')
    rev_list = call_and_ret(get_revs)
    return len(rev_list) == 0


def main():
    tests = dict([(k, v) for k, v in globals().items()
                  if callable(v) and k.startswith('test_')])
    results = dict([(k, v()) for k, v in tests.items()])
    return results


if __name__ == '__main__':
    PDB_ALL = False
    PDB_ERROR = True
    test_revisions()
    from pprint import pprint
    pprint(main())
