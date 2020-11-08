locals {
  app_name   = "${var.app}-${var.framework}"
  repo_image = "arthurgrava/${var.image}"
}

resource "kubernetes_deployment" "api" {
  metadata {
    name      = local.app_name
    namespace = var.namespace
    labels = {
      application = local.app_name
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        application = local.app_name
      }
    }

    template {
      metadata {
        labels = {
          application = local.app_name
        }
      }

      spec {
        container {
          name              = local.app_name
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
            value = 80
          }

          env {
            name  = "FRAMEWORK"
            value = var.framework
          }

          port {
            container_port = 80
          }

          liveness_probe {
            http_get {
              path = "/api/live"
              port = 80
            }

            initial_delay_seconds = 3
            period_seconds        = 3
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "api" {
  metadata {
    name      = local.app_name
    namespace = var.namespace
  }

  spec {
    selector = {
      application = kubernetes_deployment.api.metadata.0.labels.application
    }

    port {
      port        = 80
      target_port = 80
    }

    type = "ClusterIP"
  }
}
