# TeslaPy

A Python implementation based on [unofficial documentation](https://tesla-api.timdorr.com/) of the client side interface to the Tesla Motors Owner API, which provides functionality to monitor and control Tesla vehicles remotely.

## Dockerfile
By building an image with the supplied Dockerfile, you are able to run all the original TeslaPy scripts from a Docker container.

## Build
`docker build . -t teslapy`

## Run
`docker run -it --rm teslapy`
