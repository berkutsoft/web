sudo rm /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s ~/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -s ~/web/etc/gunicorn.config   /etc/gunicorn.d/ask
#sudo ln -s ~/web/etc/django.py   /etc/gunicorn.d/django.py
#sudo /etc/init.d/gunicorn restart
#gunicorn -b 0.0.0.0:8080 -D hello:app
#gunicorn -b 0.0.0.0:8080 -D django:app
cd ~/web/ask
gunicorn -D -b 0.0.0.0:8000 ask.wsgi
