docker-machine start territoire-conseil
eval "$(docker-machine env territoire-conseil)"
export URL='http://'$(docker-machine ip territoire-conseil)
python -mwebbrowser $URL
docker-compose up