docker-machine start territoire-conseil
eval "$(docker-machine env territoire-conseil)"
docker-compose run -e DJANGO_SETTINGS_MODULE=territoire_conseil.settings -w /src web bash