# Testing template for PyTEAL
This repository contains docker configuration as well as some testing setup that can be used to easily
make a new testing suite for Algorand programs written in PyTEAL.

## Starting nodes

`docker compose up`

## Running tests

`pytest` (after docker compose up)

or

`docker compose run test poetry run pytest`
