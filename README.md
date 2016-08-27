# django-playground

This is a Dockerised app for testing my deployment pipeline infrastructure. 
Unit tests and functional tests are separated in a Jenkins pipeline as well as the building and pushing of the docker image.
A push to this repo, will run all the way through to deployment in production if all stages in the pipeline are successful.
