variable "app" {
  type        = string
  description = "The app name"
}

variable "image" {
  type        = string
  description = "The image that will be used by the containers"
}

variable "framework" {
  type        = string
  description = "Which container to run the API"
  default     = "gunicorn"
}

variable "namespace" {
  type        = string
  description = "The namespace to run it"
  default     = "default"
}
