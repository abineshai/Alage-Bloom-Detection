lines = open('services/gee_service.py').readlines()
new_lines = lines[:21] + [
    'def initialize_gee(project="algae-bloom-ee"):\n',
    '    ee.Initialize(project=project)\n',
    '\n',
] + lines[39:]
open('services/gee_service.py', 'w').writelines(new_lines)
print('Done!')
lines2 = open('services/gee_service.py').readlines()
for i, l in enumerate(lines2[19:28], start=20):
    print(i, repr(l))
