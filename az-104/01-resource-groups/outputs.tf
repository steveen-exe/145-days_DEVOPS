output "resource_group_name" {
  description = "Name of the Lab 01 resource group."
  value       = azurerm_resource_group.lab.name
}

output "resource_group_location" {
  description = "Azure region of the Lab 01 resource group."
  value       = azurerm_resource_group.lab.location
}

output "resource_group_id" {
  description = "Resource ID of the Lab 01 resource group."
  value       = azurerm_resource_group.lab.id
}