variable "image_version" {
  type        = string
  description = "The version of the custom locust image to use"
}

variable "namespace" {
  type        = string
  description = "The namespace to run it"
  default     = "default"
}
