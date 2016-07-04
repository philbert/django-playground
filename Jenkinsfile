stage "check"
docker.image('python:3.5-onbuild').inside {
    sh "env"
}

stage "update"
docker.image('python:3.5-onbuild').inside {
    update: { sh "sudo apt-get update -y" }
}

stage "install dependencies"
docker.image('python:3.5-onbuild').inside {
    iceweasel: { sh "sudo apt-get install iceweasel xvfb -y" }
    pip: { sh "sudo pip install -r requirements.txt" }
}

stage "unit tests"
docker.image('python:3.5-onbuild').inside {
    lists: { sh "python manage.py test lists" }
    blog: { sh "python manage.py test blog" }
}

stage "functional tests"
docker.image('python:3.5-onbuild').inside {
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

