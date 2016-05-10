stage "update"
docker.image('python:3.5-onbuild').inside {
    sh "env"
}

node {
    update: { sh "env" }
    update: { sh "sudo apt-get update -y" }
}

stage "install dependencies"
node {
    iceweasel: { sh "sudo apt-get install iceweasel xvfb -y" }
    pip: { sh "sudo pip install -r requirements.txt" }
}

stage "unit tests"
node {
    lists: { sh "python manage.py test lists" }
    blog: { sh "python manage.py test blog" }
}

stage "functional tests"
node {
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

