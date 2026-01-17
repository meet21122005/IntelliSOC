import requests, re
urls = {
    'root': 'http://127.0.0.1:5000/',
    'dashboard': 'http://127.0.0.1:5000/dashboard',
    'alerts_api': 'http://127.0.0.1:5000/api/alerts',
    'logs_api': 'http://127.0.0.1:5000/api/logs'
}

for k,u in urls.items():
    try:
        r = requests.get(u, timeout=5)
        print(f"{k}: {r.status_code}")
        if k == 'dashboard' and r.status_code == 200:
            html = r.text
            logout_aria = re.search(r'id="logoutBtn"[^>]*aria-label="([^"]+)"', html)
            logout_type = re.search(r'id="logoutBtn"[^>]*type="([^"]+)"', html)
            print('  logout aria:', logout_aria.group(1) if logout_aria else 'MISSING')
            print('  logout type:', logout_type.group(1) if logout_type else 'MISSING')
            notif = re.search(r'aria-label="Notifications"', html)
            print('  notification button present:', bool(notif))
    except Exception as e:
        print(f"{k} error: {e}")

# Test POST to logs API
try:
    r = requests.post(urls['logs_api'], json={'source': 'smoke', 'message': 'smoke test', 'event_type': 'smoke'}, timeout=5)
    print('post_logs', r.status_code, r.text[:200])
except Exception as e:
    print('post_logs error:', e)
