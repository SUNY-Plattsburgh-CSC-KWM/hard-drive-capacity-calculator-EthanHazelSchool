platters = int(input('Enter number of platters: '))
surfaces = int(input('Enter number of surfaces per platter: '))
tracks = int(input('Enter number of tracks per surface: '))
sectors = int(input('Enter number of sectors per track: '))
bytes_per_sector = int(input('Enter number of bytes per sector: '))

capacity = platters * surfaces * tracks * sectors * bytes_per_sector

kilobytes = capacity / 1024
megabytes = kilobytes / 1000
gigabytes = megabytes / 1000
terabytes = gigabytes / 1000

if terabytes > 1.0:
    print('{:.1f} TB'.format(terabytes))
elif gigabytes > 1.0:
    print('{:.1f} GB'.format(gigabytes))
elif megabytes > 1.0:
    print('{:.1f} MB'.format(megabytes))
else:
    print('{:.1f} KB'.format(kilobytes))