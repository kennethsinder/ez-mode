
from bracket_service import BracketService
from f1040nre import Form1040NrEz
from form_io import FormPdf

bracket_svc = BracketService()


def fill_1040nrez(w2s, f1040nre):
    w2 = {}
    for form in w2s:
        for key in form:
            if key not in w2:
                w2[key] = form[key]
            else:
                w2[key] += form[key]

    result = {}
    result['1'] = True      # Single non-resident alien
    result['2'] = False     # Not married non-resident alien
    result['3'] = w2['1']   # Total wages, etc.
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
    for key in result:
        f1040nre.data[key] = '{}'.format(result[key])
    return result


def input_and_validate(prompt, t=str):
    if t == bool:
        prompt += ' [y/n]'
    prompt += ' '
    while True:
        result = input(prompt)
        try:
            if result in t:
                return result
        except TypeError:
            if t == bool and result in {'Y', 'N', 'y', 'n'}:
                return result in {'Y', 'y'}
            if isinstance(result, t):
                return result
            try:
                return t(result)
            except:
                pass

# w2 = {
#     '1': 35000,
#     '2': 3000,
#     '17': 2000,
# }

data = {}
data['first_name'] = input_and_validate("Hey there! What's your first name?")
data['last_name'] = input_and_validate("What's your last name?")
data['ssn'] = input_and_validate('SSN/ITIN:', int)
data['street_address'] = input_and_validate('(Foreign country) street number and address:')
data['city'] = input_and_validate('(Foreign) city/town name:')
data['fc_province'] = input_and_validate('State/province:')
data['fc_postal_code'] = input_and_validate('Postal/ZIP code:')
data['fc_name'] = input_and_validate('Country name:')
f1040nre = Form1040NrEz('2019')
f1040nre.data = data
num_w2 = input_and_validate('How many W2s do you have?', int)
w2s = []
for i in range(1, 1 + num_w2):
    w2 = {}
    w2['1'] = int(round(input_and_validate('Line 1 on your W-2 #{} please:'.format(i), float)))
    w2['2'] = int(round(input_and_validate('Line 2 on your W-2 #{} please:'.format(i), float)))
    w2['17'] = int(round(input_and_validate('Line 17 on your W-2 #{} please:'.format(i), float)))
    w2s.append(w2)
federal_return = fill_1040nrez(w2s, f1040nre)
for line_num in sorted(federal_return.keys()):
    print('{} {}'.format(line_num, federal_return[line_num]))
f1040nre_pdf = FormPdf(f1040nre.get_template_path(), 'f1040nre-output.pdf')
f1040nre_pdf.write_output(f1040nre.get_values())
