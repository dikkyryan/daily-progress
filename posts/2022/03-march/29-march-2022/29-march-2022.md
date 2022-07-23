# terraform-azurerm-cognitive

Terraform Module for deploying a Azure Cognitive Service (QNA)

[![Terraform](https://github.com/imjoseangel/terraform-azurerm-cognitive/actions/workflows/terraform.yml/badge.svg)](https://github.com/imjoseangel/terraform-azurerm-cognitive/actions/workflows/terraform.yml)

## Deploys an Azure Cognitive Service with QNAMaker. Insights and Search are installed as part of the solution

This Terraform module deploys a Bot Services on Azure using Cognitive Services and QNAMAker

### NOTES

* A SystemAssigned identity will be created by default.
* LUIS, Search and Application Insights are installed by default.
* Application Identity are installed by default.

## Usage in Terraform 1.0

```terraform
module "cognitive" {
  source                = "github.com/imjoseangel/terraform-azurerm-cognitive"
  name                  = "cognitiveservice"
  location              = local.location
  resource_group_name   = "rsg-cognitive"
  location              = "westeurope"
  create_resource_group = true
}
```

## Authors

Originally created by [imjoseangel](http://github.com/imjoseangel)

## License

[MIT](LICENSE)
