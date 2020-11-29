from evdev import ecodes, InputDevice, list_devices

def get_devices_from_paths(device_paths):
    return [InputDevice(device_fn) for device_fn in device_paths]
devices = get_devices_from_paths(reversed(list_devices()))

def print_device_list(devices):
    device_format = '{1.fn:<20} {1.name:<35} {1.phys}'
    device_lines = []
    for n, d in enumerate(devices):
        if 'usb' in d.phys:
            device_lines.append(device_format.format(n, d))

    print('-' * len(max(device_lines, key=len)))
    print('{:<20} {:<35} {}'.format('Device', 'Name', 'Phys'))
    print('-' * len(max(device_lines, key=len)))
    print('\n'.join(device_lines))
    print('')

devices = get_devices_from_paths(reversed(list_devices()))
print_device_list(devices)
