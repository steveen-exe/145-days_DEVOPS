variable "subscription_id" {
  description = "Azure subscription ID used by the AzureRM provider."
  type        = string
  sensitive   = true
}

variable "resource_group_name" {
  description = "Name of the Lab 01 resource group."
  type        = string
  default     = "rg-az104-tf-lab"
}

variable "location" {
  description = "Azure region for the resource group."
  type        = string
  default     = "indiasouthcentral"
}

variable "tags" {
  description = "Tags applied to the resource group."
  type        = map(string)
  default = {
    environment = "learning"
    project     = "145-days-devops"
    managed_by  = "terraform"
    purpose     = "az104-lab"
  }
}