content = open('services/gee_service.py').read()

# Find the broken function and replace entirely
start = content.index('def initialize_gee')
end = content.index('\ndef ', start + 1)

broken = content[start:end]
fixed = '''def initialize_gee(project="algae-bloom-ee"):
    """Authenticate and initialize Google Earth Engine."""
    ee.Initialize(project=project)'''

content = content[:start] + fixed + content[end:]
open('services/gee_service.py', 'w').write(content)

# Verify
c = open('services/gee_service.py').read()
i = c.index('def initialize_gee')
print('FIXED FUNCTION:')
print(c[i:i+150])
print('\nSUCCESS!')
