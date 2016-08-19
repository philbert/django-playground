#!groovy

docker.image('philbert/django1.8:latest').inside {
    stage "check"
    sh "env"
    // surely shouldn't have to do this??
    checkout scm
    sh "ls -la"

    stage "unit tests"
    lists: { sh "python manage.py test lists" }
    blog: { sh "python manage.py test blog" }

    stage "functional tests"
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

