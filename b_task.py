import json_read

def task(date_obj):

    volumes = json_read.retrieve_list(date_obj.get_dates(), 'total_volumes')

    return highest_volume(volumes)



def highest_volume(volumes):
    
    max_volume = volumes[0]

    for values in volumes:
        if max_volume[1] < values[1]:
            max_volume = values

    return max_volume

    