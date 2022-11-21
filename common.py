"""

    """

import re

import ns


c = ns.Col()

jdPAT = '1[34]\d{2}/\d{2}/\d{2}'
acC_DIGITS = '(\((\d+,)*\d+\))|(\d+,)*\d+'

def make_sub_name(*lst , sub_splice = '.') :
    return sub_splice.join([x for x in lst])

class ProductionsCols :
    _pq = 'ProductionQty'
    _sq = 'SalesQty'
    _sp = 'SalesPrice(Rial)'
    _sv = 'SalesValue(MRial)'
    _fyc = 'FiscalYearCumulative'
    _fyculm = _fyc + 'UntilLastMonth'
    _rv = 'Revision'
    _rvd = 'Revised'
    _rfyculm = _rvd + _fyculm

    pn = 'Name'
    un = 'Unit'

    mpq = make_sub_name(c.jm , _pq)
    msq = make_sub_name(c.jm , _sq)
    msp = make_sub_name(c.jm , _sp)
    msv = make_sub_name(c.jm , _sv)

    fpq = make_sub_name(_fyc , _pq)
    fsq = make_sub_name(_fyc , _sq)
    fsp = make_sub_name(_fyc , _sp)
    fsv = make_sub_name(_fyc , _sv)

    fyupq = make_sub_name(_fyculm , _pq)
    fyusq = make_sub_name(_fyculm , _sq)
    fyusp = make_sub_name(_fyculm , _sp)
    fyusv = make_sub_name(_fyculm , _sv)

    rpq = make_sub_name(_rv , _pq)
    rsq = make_sub_name(_rv , _sq)
    rsv = make_sub_name(_rv , _sv)

    rfyupq = make_sub_name(_rfyculm , _pq)
    rfyusq = make_sub_name(_rfyculm , _sq)
    rfyusp = make_sub_name(_rfyculm , _sp)
    rfyusv = make_sub_name(_rfyculm , _sv)

    psun = 'ProductStatus' + '-' + un

class ServiceCols :
    _cntrct = 'Contracts'
    _cjd = 'ContractJDate'
    _cnd = 'ContractDuration'
    _rev = 'Revenue'
    _fyc = 'FiscalYearCumulative'
    _fyculm = _fyc + 'UntilLastMonth'
    _rv = 'Revision'
    _rvd = 'Revised'
    _rfyculm = _rvd + _fyculm
    _lfyc = 'LastFiscalYearCumulative'

    name = 'Name'

    cjd = make_sub_name(_cntrct , _cjd)
    cnd = make_sub_name(_cntrct , _cnd)

    rulm = make_sub_name(_rev , _fyculm)
    rrv = make_sub_name(_rev , _rv)
    rrvd = make_sub_name(_rev , _rfyculm)
    rjm = make_sub_name(_rev , c.jm)
    rfc = make_sub_name(_rev , _fyc)
    rlfyc = make_sub_name(_rev , _lfyc)

    cmnt = 'Comments'

def rm_sapces(obj) :
    if not isinstance(obj , str) :
        return obj
    return re.sub(r'\s+' , '' , obj)
