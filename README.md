# meraki-automate
Meraki tools using Meraki Dashboard API

Do you have a large number of Meraki MX or Z3 Teleworkor Gateways to deploy?

Use this to rapidly deploy templated Z3 Teleworker Gateways or MX appliances
This script:
    1. Provisions networks
    2. Adds security appliance to networks
    3. Names security appliance
    4. Applies a configuration template
Use included devicelist.csv file or create a CSV file containing:
*header names in ()
    Serial Number(sn),
    Hostname(hostname),
    Network(network),
    Config Template(config template)
Edit meraki.json to configure your api key, org name, and source csv file
Works on a single Organization
