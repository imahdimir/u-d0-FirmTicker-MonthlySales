"""

    """

from pathlib import Path

from py_modules._3_pat_0 import ColName
from py_modules._3_pat_0 import Dirr


module_n = 9

dirr = Dirr()
c = ColName()

class Pat6 :
    p0 = 'شرح'
    _p1 = 'درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'درآمد محقق شده طی دوره یک ماهه منتهی به'
    p4 = _p4 + '\d{4}/\d{2}/\d{2}'
    _p5 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p5 = _p5 + '\d{4}/\d{2}/\d{2}'

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

    sales_title = 'درآمد محقق شده (میلیون ریال)-لیزینگ'
    sum_row_name = 'جمع'
    sum_col = 4
    sum_row_fr_bottom = None
    modif_col = 2
    asr = 'شرح'

def main() :
    pass

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##
    import pandas as pd


    trc = '930071'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
