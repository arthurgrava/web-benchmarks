locals {
  app        = "locust-load"
  repo_image = "arthurgrava/web-benchmarks:locust-${var.image_version}"
}

resource "kubernetes_deployment" "locust" {
  metadata {
    name      = local.app
    namespace = var.namespace
    labels = {
      application = local.app
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        application = local.app
      }
    }

    template {
      metadata {
        labels = {
          application = local.app
        }
      }

      spec {
        container {
          name              = local.app
          image             = local.repo_image
          image_pull_policy = "Always"

          resources {
            limits {
              cpu    = "500m"
              memory = "256Mi"
            }
            requests {
              cpu    = "250m"
              memory = "128Mi"
            }
          }

          env {
            name  = "PORT"
            value = 8089
          }

          port {
            container_port = 8089
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "locust" {
  metadata {
    name      = local.app
    namespace = var.namespace
  }

  spec {
    selector = {
      application = kubernetes_deployment.locust.metadata.0.labels.application
    }

    port {
      port        = 80
      target_port = 8089
    }

    type = "ClusterIP"
  }
}
