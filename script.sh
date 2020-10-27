docker build . --rm -f Dockerfile.test -t tests
docker run tests
docker rmi tests -f

docker build . -t bot
docker run bot
