import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from app import app
except Exception as e:
    print('Error importing app:', e)
    raise

print('Registered routes:')
for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
    methods = ','.join(sorted(rule.methods - {'HEAD','OPTIONS'}))
    print(f"{rule.rule} -> {rule.endpoint} [{methods}]")
