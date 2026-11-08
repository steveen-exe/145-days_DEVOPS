# AZ-104 Terraform Lab 01: Resource Groups

This lab manages the existing `rg-az104-tf-lab` resource group in the
`indiasouthcentral` Azure region. Lab 02, Virtual Machines, is intentionally
not included.

## Prerequisites

- Terraform 1.5 or later
- Azure CLI
- An authenticated Azure CLI session
- Access to the target Azure subscription

Authenticate and select the subscription:

```bash
az login
az account set --subscription "8463e900-c331-4c06-9ce4-c52a5257bbcc"
az account show --output table
export ARM_SUBSCRIPTION_ID="$(az account show --query id -o tsv)"
export TF_VAR_subscription_id="$ARM_SUBSCRIPTION_ID"
```

Before deployment, verify the current subscription policy for allowed
regions. The previously allowed region was `indiasouthcentral`:

```bash
az policy assignment list \
  --query "[?displayName=='Allowed resource deployment regions'].parameters.listOfAllowedLocations.value" \
  -o json
```

## Initialize and validate

Run these commands from this directory:

```bash
terraform init
terraform fmt -recursive
terraform validate
```

Commit `.terraform.lock.hcl` after `terraform init`. It records provider
selections and checksums for repeatable initialization.

## Recover the existing resource group

The original local Terraform state may have been lost with the Codespace.
Check Azure before planning or applying:

```bash
az group show \
  --name rg-az104-tf-lab \
  --query "{name:name,location:location,tags:tags}" \
  -o jsonc
```

If the resource group exists, do not apply it as a new resource. Import it
into the new local state:

```bash
terraform import azurerm_resource_group.lab \
  "/subscriptions/8463e900-c331-4c06-9ce4-c52a5257bbcc/resourceGroups/rg-az104-tf-lab"
terraform state list
terraform plan
```

The expected result is no infrastructure changes. If the plan proposes
location or tag changes, inspect the plan and resolve the difference before
any apply. Never delete `rg-az104-tf-lab`, and do not modify the older
CLI-created resource group `az104-day1-rg`.

If the resource group does not exist, stop and review a normal
`terraform plan` before creating anything.

## Plan, apply, and cleanup

Always save and review an exact plan before an apply:

```bash
terraform plan -out=lab01.tfplan
terraform show lab01.tfplan
```

Only after explicit approval should an apply be considered:

```bash
terraform apply lab01.tfplan
```

This recovery guide does not authorize `terraform apply`,
`terraform destroy`, or destructive Azure CLI commands. Do not run them
without reviewing the exact plan first. Since this lab manages a shared
resource group, do not run `terraform destroy` as routine cleanup.

Verify the resource group and Terraform outputs with:

```bash
az group show --name rg-az104-tf-lab -o jsonc
terraform output
```

## State and sensitive files

Terraform state can contain infrastructure details and must remain local or
be stored in an approved remote backend. Never commit state files, plan
files, credentials, service-principal secrets, certificates, or private
keys. The provider uses Azure CLI authentication and does not create or
store service-principal credentials.