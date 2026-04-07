import re

content = open('services/gee_service.py').read()

# Replace the entire broken initialize_gee function
new_func = '''def initialize_gee(project="algae-bloom-ee"):
    """Authenticate and initialize Google Earth Engine."""
    ee.Initialize(project=project)

'''

content = re.sub(
    r'def initialize_gee[\s\S]*?(?=\ndef [a-z])',
    new_func,
    content
)

open('services/gee_service.py', 'w').write(content)
print('Done! Verifying...')

content2 = open('services/gee_service.py').read()
idx = content2.index('def initialize_gee')
print(content2[idx:idx+200])
print('\n--- Testing import ---')
import ee
ee.Initialize(project='algae-bloom-ee')
print('GEE OK!')
