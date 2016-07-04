stage "check"
docker.image('philbert/django1.8').inside {
    sh "env"
}

stage "unit tests"
docker.image('philbert/django1.8').inside {
    lists: { sh "python manage.py test lists" }
    blog: { sh "python manage.py test blog" }
}

stage "functional tests"
docker.image('philbert/django1.8').inside {
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

