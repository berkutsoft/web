sudo killall gunicorn
sudo /etc/init.d/nginx restart
cd ~/web/ask
gunicorn -D -b 0.0.0.0:8000 ask.wsgi


