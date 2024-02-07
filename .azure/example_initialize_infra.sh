RG_NAME="dev-flask-app"

az group create --name $RG_NAME --location "westeurope" \
&& az deployment group create --resource-group $RG_NAME --template-file .azure/bicep/main.bicep
