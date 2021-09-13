variable "rg_name" {
  type    = string
  default = "NOTEJAM-DEMO-RG2"
}

variable "location" {
  type    = string
  default = "westeurope"
}

variable "db_server" {
  type    = string
  default = "kknotejamappdb"
}
variable "admin_login" {
  type    = string
  default = "sqladmin"
}
variable "admin_pwd" {
  type    = string
  default = "Microsoft2020"
}
variable "db_name" {
  type    = string
  default = "notejam"
}
variable "app_plan" {
  type    = string
  default = "notejamappplan"
}
variable "app_name" {
  type    = string
  default = "kknotejamapp"
}
