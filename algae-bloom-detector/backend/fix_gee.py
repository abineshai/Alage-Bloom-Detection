import re

content = open('services/gee_service.py').read()

new_func = (
    'def initialize_gee(project="algae-bloom-ee"):\n'
    '    ee.Initialize(project=project)\n'
    '\n'
)

content = re.sub(r'def initialize_gee[\s\S]*?(?=\ndef )', new_func, content)
open('services/gee_service.py', 'w').write(content)
print('Done! New function:')

content2 = open('services/gee_service.py').read()
start = content2.index('def initialize_gee')
print(content2[start:start+150])
