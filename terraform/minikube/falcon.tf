module "falcon-meinheld" {
  count     = var.falcon ? 1 : 0
  source    = "../modules/k8s-python-app"
  app       = "falcon"
  image     = "web-benchmarks:falcon-0.0.1"
  framework = "meinheld"
}

module "falcon-uwsgi" {
  count     = var.falcon ? 1 : 0
  source    = "../modules/k8s-python-app"
  app       = "falcon"
  image     = "web-benchmarks:falcon-0.0.1"
  framework = "uwsgi"
}
