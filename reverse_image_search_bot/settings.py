TELEGRAM_API_TOKEN = '1809674230:AAGkHLLPtq_ikQ1457Rt1IcWWrRlkBYe1GE'

UPLOADER = {
    'uploader': 'reverse_image_search_bot.uploaders.ssh.SSHUploader',
    'url': 'Host Domain Name',
    'configuration': {
        'host': 'Host IP (PUBLIC)',
        'user': 'Yourname',
        'password': 'Password',
        'upload_dir': '/path/to/ReVot/',
        'key_filename': '/path/to/.ssh/rsakey.pub (Public key)',
    }
}
