
from bracket_service import BracketService

bracket_svc = BracketService()


def fill_1040nrez(w2s):
    w2 = {}
    for form in w2s:
        for key in form:
            if key not in w2:
                w2[key] = form[key]
            else:
                w2[key] += form[key]

    result['1'] = 1  # Single non-resident alien
    result['2'] = 0  # Not married non-resident alien
    result['3'] = w2['1']  # Total wages, etc.
    result['7'] = result['3']
    result['10'] = result['7']
    result['11'] = w2['17']
    result['14'] = max(result['10'] - result['11'], 0)
    result['15'] = bracket_svc.get_tax(result['14'])
    result['17'] = result['15']
    result['18a'] = w2['2']
    result['21'] = result['18a'] + \
        result.get('18b', 0) + result.get('19', 0) + result.get('20', 0)
    if result['21'] > result['17']:
        result['22'] = float(result['21']) - float(result['17'])
    else:
        result['25'] = float(result['17']) - float(result['21'])
    return result


w2 = {
    '1': 35000,
    '2': 3000,
    '17': 2000,
}

federal_return = fill_1040nrez([w2])
for line_num in sorted(federal_return.keys()):
    print('{} {}'.format(line_num, federal_return[line_num]))
