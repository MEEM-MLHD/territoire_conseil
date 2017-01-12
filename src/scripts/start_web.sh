#sh /src/scripts/wait.sh

cd /src
export DJANGO_SETTINGS_MODULE=territoire_conseil.settings
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages
uwsgi --socket :8000 --wsgi-file /src/territoire_conseil/wsgi.py --chdir /src/territoire_conseil --master --processes 4 --threads 2 --py-autoreload 3
