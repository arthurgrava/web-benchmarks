module "locust" {
  source        = "../modules/k8s-locust"
  image_version = "0.0.1"
}
