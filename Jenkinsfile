#!groovy

docker.image('philbert/django1.8:latest').inside {
    stage "checkout"
    // if this is necessary then I should just run a test container
    checkout scm

    stage "unit test lists"
    // until cobertura is fix to work with a jenkins pipeline, this looks
    // like the best option to get xunit test reports
    // https://github.com/xmlrunner/unittest-xml-reporting/tree/master/
    lists: { sh "coverage run --source='.' manage.py test lists" }
    report: { sh "coverage xml -o reports/lists_cov.xml" }
    report: { sh "coverage report" }
    //step([$class: 'JUnitResultArchiver', testResults: '**/reports/coverage.xml'])

    stage "unit test blog"
    blog: { sh "coverage run --source='.' manage.py test blog" }
    report: { sh "coverage xml -o reports/blog_cov.xml" }
    report: { sh "coverage report" }

    stage "functional tests"
    selenium: { sh "xvfb-run python manage.py test functional_tests" }
}

