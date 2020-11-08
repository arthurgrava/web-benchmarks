terraform {
  backend "local" {}

  required_version = "0.13.5"
}

provider "kubernetes" {
  config_context = "minikube"
  version = "1.13.3"
}
