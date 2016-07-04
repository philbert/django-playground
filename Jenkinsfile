stage "check"
docker.image('philbert/python3.5').inside {
    sh "env"
}

stage "install dependencies"
docker.image('philbert/python3.5').inside {
    iceweasel: { sh "sudo apt-get install iceweasel xvfb -y" }
    pip: { sh "sudo pip install -r requirements.txt" }
}

stage "unit tests"
docker.image('philbert/python3.5').inside {
    lists: { sh "python manage.py test lists" }
    blog: { sh "python manage.py test blog" }
}

stage "functional tests"
docker.image('philbert/python3.5').inside {
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

