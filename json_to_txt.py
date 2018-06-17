import json


def convert_json_to_text():
    """Converts json addresses file to a text file"""
    file_name = 'addresses'
    with open(f'{file_name}.json') as json_file:
        addresses = json.load(json_file)

    with open(f'{file_name}.txt', 'w') as txt_file:
        txt_file.write('Title\tAddress\tUrl\n')
        for address in addresses:
            txt_file.write('\t'.join([
                address['title'] or '',
                address['address'] or '',
                address['url'] or '',
            ]) + '\n')

if __name__ == '__main__':
    convert_json_to_text()
