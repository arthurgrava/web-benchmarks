module "gunicorn" {
  count     = var.flask ? 1 : 0
  source    = "../modules/k8s"
  app       = "flask"
  image     = "web-benchmarks:flask-0.0.2"
  framework = "gunicorn"
}

module "meinheld" {
  count     = var.flask ? 1 : 0
  source    = "../modules/k8s"
  app       = "flask"
  image     = "web-benchmarks:flask-0.0.2"
  framework = "meinheld"
}

module "uwsgi" {
  count     = var.flask ? 1 : 0
  source    = "../modules/k8s"
  app       = "flask"
  image     = "web-benchmarks:flask-0.0.2"
  framework = "uwsgi"
}
