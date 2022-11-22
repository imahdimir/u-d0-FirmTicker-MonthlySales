"""

    """

import re

import ns


c = ns.Col()

jdPAT = '1[34]\d{2}/\d{2}/\d{2}'
numpat = '\d{1,3}(,\d{3})*(\.\d+)?'
acC_DIGITS = f'({numpat})|(\({numpat}\))'

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

    name = 'Name'
    unit = 'Unit'

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

    psun = 'ProductStatus' + '-' + unit

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

class InsuranceCols :
    _fyc = 'FiscalYearCumulative'
    _fyculm = _fyc + 'UntilLastMonth'
    _ipi = 'InsurancePremiumIssued(IncludingReliableAccpetance)'
    _val = 'Value(MRial)'
    _pct = 'SharePercentage'
    _dp = 'DamagesPaid'
    _rv = 'Revision'
    _rvd = 'Revised'
    _rfyculm = _rvd + _fyculm

    name = 'Name'

    fiv = make_sub_name(_fyculm , _ipi , _val)
    fip = make_sub_name(_fyculm , _ipi , _pct)
    fdv = make_sub_name(_fyculm , _dp , _val)
    fdp = make_sub_name(_fyculm , _dp , _pct)

    riv = make_sub_name(_rv , _ipi , _val)
    rdv = make_sub_name(_rv , _dp , _val)

    rfiv = make_sub_name(_rfyculm , _ipi , _val)
    rfip = make_sub_name(_rfyculm , _ipi , _pct)
    rfdv = make_sub_name(_rfyculm , _dp , _val)
    rfdp = make_sub_name(_rfyculm , _dp , _pct)

    civ = make_sub_name(c.jm , _ipi , _val)
    cip = make_sub_name(c.jm , _ipi , _pct)
    cdv = make_sub_name(c.jm , _dp , _val)
    cdp = make_sub_name(c.jm , _dp , _pct)

    fyiv = make_sub_name(_fyc , _ipi , _val)
    fyip = make_sub_name(_fyc , _ipi , _pct)
    fydv = make_sub_name(_fyc , _dp , _val)
    fydp = make_sub_name(_fyc , _dp , _pct)

class LeasingCols :
    _fyc = 'FiscalYearCumulative'
    _fyculm = _fyc + 'UntilLastMonth'
    _rev = 'Revenue'
    _val = 'Value(MRial)'
    _rv = 'Revision'
    _rvd = 'Revised'
    _rfyculm = _rvd + _fyculm

    name = 'Name'
    rulm = make_sub_name(_rev , _fyculm , _val)
    riv = make_sub_name(_rv , _val)
    rrv = make_sub_name(_rev , _rfyculm , _val)
    rjmv = make_sub_name(_rev , c.jm , _val)
    rfv = make_sub_name(_rev , _fyc , _val)

class RealEstateCols :

    name = 'Name'

def rm_sapces(obj) :
    if not isinstance(obj , str) :
        return obj
    return re.sub(r'\s+' , '' , obj)
