module "locust" {
  count         = var.locust ? 1 : 0
  source        = "../modules/k8s-locust"
  image_version = "0.0.1"
}
