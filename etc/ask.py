CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/ask/',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        'app.module',
    ),
}
