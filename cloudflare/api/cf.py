import CloudFlare
from enum import Enum

class RequestType(Enum):
    GET = 1
    POST = 2

def handle_api_call(func, *argv):
    result = None
    try:
        if argv:
            result = func(argv[0])
        else:
            result = func()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        return('/user.get %d %s - api call failed' % (e, e))
    except Exception as e:
        return('/user.get - %s - api call failed' % (e))
    return result

def get_users():
    cf = CloudFlare.CloudFlare()
    ips = handle_api_call(cf.user.get)
    return ips

def get_ips():
    cf = CloudFlare.CloudFlare()
    ips = handle_api_call(cf.ips.get)
    return ips

def get_zones():
    cf = CloudFlare.CloudFlare()
    zones = handle_api_call(cf.zones.get)
    return zones

def get_settings(zone_id):
    cf = CloudFlare.CloudFlare()
    result = []
    zones = get_all_zones()
    # there should only be one zone
    for zone in zones:
        if zone['id'] == zone_id: 
            zone_name = zone['name']
            break

    settings = handle_api_call(cf.zones.settings.get, zone_id)

    curr_setting = []
    for setting in settings:
        name = setting['id']
        value = setting['value']
        editable = setting['editable']
        curr_setting.append({'name': name, 'value': value, 'editable': editable})
    result.append({'zone_id': zone_id, 'zone_name': zone_name, 'settings': curr_setting})
    return result

def get_dns_records(zone_id):
    cf = CloudFlare.CloudFlare()
    result = []
    # dns_records = cf.zones.dns_records.export.get(zone_id)

    # if len(zones) != 1:
    #     return('/zones.get - %s - api call returned %d items' % (zone_name, len(zones)))

    # # there should only be one zone
    # zone = zones[0]

    # zone_name = zone['name']
    # zone_id = zone['id']

    # print("Zone:\t%s %s" % (zone_id, zone_name))

    # params = {'name': dns_name}
    dns_records = cf.zones.dns_records.get(zone_id)
   
    if len(dns_records) == 0:
        return('/zones.dns_records.get - %s - no records found' % (dns_name))

    for dns_record in dns_records:
        # print(dns_record)
        result.append({
            'zone_id': dns_record['zone_id'],
            'id': dns_record['id'],
            'name': dns_record['name'],
            'type': dns_record['type'],
            'content': dns_record['content'],
            'ttl': dns_record['ttl'],
            'proxied': dns_record['proxied'],
            'proxiable': dns_record['proxiable']
        })
    return result
        # return('Record:\t%s %s %s %6d %-5s %s ; proxied=%s proxiable=%s' % (
        #     r_zone_id, r_id, r_name, r_ttl, r_type, r_content, r_proxied, r_proxiable
        # ))

    