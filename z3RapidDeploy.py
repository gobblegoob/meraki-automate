"""
Use this to rapidly deploy templated Z3 Teleworker Gateways or MX appliances

This script:
    1. Provisions networks
    2. Adds security appliance to networks
    3. Names security appliance
    4. Applies a configuration template

Get a CSV file containing:

*header names in ()
    Serial Number(sn),
    Hostname(hostname),
    Network(network),
    Config Template(config template)

Edit meraki.json to configure your api key, org name, and source csv file

Works on a single Organization

"""
import json
from datetime import datetime
import meraki
import pandas as pd

api_key = '' # Set here, or edit the meraki.json file
org_name = '' # Set here, or edit the meraki.json file
src_csv = '' # Set here, or edit the meraki.json file
js_source = 'meraki.json' # json file contains api key, org name, and source csv


def get_source_json(js_file):
    """
    Set global variables from accompanying json file
    :param js_file:  source json file
    :return:
    """
    global api_key
    global org_name
    global src_csv
    try:
        with open(js_file) as f:
            api_dict = json.load(f)
            api_key = api_dict['meraki_api_key']
            org_name = api_dict['organization_name']
            src_csv = api_dict['source_file']
            return
    except FileNotFoundError as e:
        print(f'Source file not found! \n --- {e}')
        quit()


def get_src_dataframe():
    try:
        global src_csv
        df = pd.read_csv(src_csv)
        return df
    except FileNotFoundError:
        print(f'Source csv file {src_csv} not found.  Exiting.')
        quit()


def create_net(db, orgid, name):
    """
    Create the network on the Meraki Controller
    :param db: Meraki Dashboard Object
    :param orgid: organization Id
    :param name: Network Name
    :return:
    """
    try:
        output = db.organizations.createOrganizationNetwork(orgid, name, productTypes=['appliance'])
        network_id = output['id']
        # The 201 response will have the networkId we can use to complete device configuration
        return network_id
    except meraki.APIError as e:
        print(f'API Error: {e}')


def claim_dev(db, netid, sn):
    """
    Claim a device to a network on the Meraki Controller
    :param db: Meraki dashboard object
    :param netid: newtworkId
    :param sn: Serial Number
    :return:
    """
    try:
        db.networks.claimNetworkDevices(netid,sn)
        return
    except meraki.APIError as e:
        print(f'\nError Claiming Device \n---{e}')
        quit()


def name_dev(db, name, sn):
    """
    Set Device Hostname
    :param db: Meraki dashboard object
    :param name: Hostame str
    :param sn: Serial Number
    :return:
    """
    try:
        db.devices.updateDevice(sn, name=name)
    except meraki.APIError as e:
        print(f'Error naming device\n--- {e}')



def get_shard(org):
    """
     Gets the org shard to build and return the API URL
    :param org: organization dictionary
    :return: base url with correct shard
    """
    urlLength = org['url'].find('com') + 3
    orgShard = org['url'][8:urlLength]
    base_url = 'https://' + orgShard + '/api/v1'
    return base_url


def get_template_id(db, orgid, cfgtemplate):
    """
    Gets template id number
    :param db: Meraki dashboard object
    :param orgid: orgainziationId
    :param cfgtemplate: Template string as identified in source csv
    :return:
    """
    try:
        template_list = db.organizations.getOrganizationConfigTemplates(orgid)
        for t in template_list:
            if t['name'] == cfgtemplate:
                selected_template = t['id']
                return selected_template
            else:
                continue
        print('\n\n**** Selected Template Not Found ****\n\n')
        quit()
    except meraki.APIError as e:
        print(f'\n Error Getting Template IDs\n--- {e}')
    return


def dev_cfg_template(db, cfgtempid, netid):
    """
    Apply config template to network
    :param db: meraki dashboard object
    :param cfgtempid: config template id
    :param netid: network id
    :return:
    """
    try:
        db.networks.bindNetwork(cfgtempid, netid)
        return
    except meraki.APIError as e:
        print(f'Error configuring template \n---{e}')

def main():
    """
    Instantiate the Meraki Dashboard API session
    :return:
    """
    global api_key
    global org_name
    global js_source

    #set globals from json file
    get_source_json(js_source)

    dashboard = meraki.DashboardAPI(
        api_key = api_key,
        base_url = 'https://api.meraki.com/api/v1',
        output_log = False, # set to True to save API logs
        log_file_prefix = '',
        log_path = 'logs',
        print_console = True
    )

    # Get organization data and build base url with correct shard
    organizations = dashboard.organizations.getOrganizations()
    for org in organizations:
        if org["name"] == org_name:
            org_id = org['id']
            print(f'\nOrganization {org_name} id: {org_id}')
            base_url = get_shard(org)
            print(base_url)


    #destroy initial object
    del dashboard

    # Create new dashboard object with correct shard id
    dashboard = meraki.DashboardAPI(
        api_key=api_key,
        base_url=base_url,
        output_log=True,  # set to True to save API logs
        log_file_prefix='',
        log_path='logs',
        print_console=True
    )

    # Source file is pandas dataframe object
    src = get_src_dataframe()
    src.head()

    # The following line is for testing purposes
    # print(dashboard.organizations.getOrganizations())

    for index, row in src.iterrows():
        cfg_template_id = get_template_id(dashboard, org_id, row['config template'])
        net_id = create_net(dashboard, org_id, row['network'])
        dev_serial = [row['sn']]
        claim_dev(dashboard, net_id, dev_serial)
        dev_cfg_template(dashboard, net_id, cfg_template_id)
        name_dev(dashboard, row['hostname'], row['sn'])



if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\nScript complete, total runtime: {end_time - start_time}')
    print('\n\n')
    print('*'*50)
