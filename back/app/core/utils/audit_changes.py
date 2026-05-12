def extract_changes(

    old_data: dict,

    new_data: dict
):

    old_values = {}

    new_values = {}

    for key in new_data:

        old_value = old_data.get(key)

        new_value = new_data.get(key)

        if old_value != new_value:

            old_values[key] = old_value

            new_values[key] = new_value

    return {

        "old_values": old_values,

        "new_values": new_values
    }