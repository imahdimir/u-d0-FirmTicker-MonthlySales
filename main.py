"""

    """

import importlib
from pathlib import Path


def main() :
    pass

    ##
    pys = cf.load_pns_of_all_modules_in_the_same_dir_except(dirs.UpdateData)
    print(pys)
    ##
    dct = {}
    for mod in pys :
        dct[str(mod)] = importlib.import_module(mod , package = None)
    print(dct)
    ##
    for v in dct.values() :
        v.main()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
