stage "check"
docker.image('philbert/python3.5').inside {
    sh "env"
}

stage "git clone"
docker.image('philbert/python3.5').inside {
    git url: "https://github.com/philbert/django-playground.git"
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

