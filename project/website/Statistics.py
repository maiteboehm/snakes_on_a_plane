import os

def database_reader(class_variable):
    """Reads the Database which contains the Seat_IDs(Int,prim.key), Flight_Numbers(int), Seats(Capital Letters),
                Seat_types (defined by the seat_identifier function in Charreader) and Occupation_status(True or False Str)
                and evaluates how many seats are occupied or available and saves them to the Statistics.txt in the Output_Data
                Directory of the project.
    """
    occupied_types = class_variable.query.filter_by(seat_status='False').all()
    available_types = class_variable.query.filter_by(seat_status='True').all()
    number_types = class_variable.query.all()
    occupation_all_seats = (len(occupied_types) * 100) / len(number_types)
    available_all_seats = 100 - occupation_all_seats
    path = os.path.abspath(os.curdir)
    # Project_Path = os.path.dirname(Path)
    out_path = path + r'\Output_Data\\'

    # saving_directory = r'C:\Users' + '\\' + str(username) + '\\Downloads\\'
    name_of_file = 'Statistics.txt'
    filename_dictionary = os.path.join(out_path, name_of_file)
    if os.path.isfile(filename_dictionary):
        output = open(filename_dictionary, 'r')
        lines = output.readlines()
        version_counter_liste = []
        last_availability_entry_liste = []
        last_availability_entry = []

        for letter in lines[0]:
            if letter.isdigit():
                version_counter_liste.append(letter)
                version_counter = ''.join(version_counter_liste)
                version_counter = int(version_counter)
        print(lines[version_counter])
        for index, letter in enumerate(lines[version_counter]):
            if letter == ' ':
                break

            elif letter.isdigit() or '.':
                last_availability_entry.append(letter)

        last_availability_entry_liste.append(''.join(last_availability_entry))
        print(last_availability_entry_liste, occupation_all_seats)
        if float(last_availability_entry_liste[0]) == float(occupation_all_seats):
            print('File not updated, everything up2date')
            return filename_dictionary

        else:
            output = open(filename_dictionary, 'w')
            lines[0] = lines[0].replace(str(version_counter),str(version_counter + 1))
            lines.insert(version_counter+1, str(occupation_all_seats) + '    ' + str(available_all_seats) + '\n')
            for items in lines:
                output.write(str(items))
                print(items)
    else:
        output = open(filename_dictionary, 'a')
        output.write('All_Seat_Occupation All_Seat_Availability ' + str(1) +
                      '\n' + str(occupation_all_seats) + '    ' + str(available_all_seats) + '\n')
        output.write('Occupied_Seats Available Seats' + '\n')

        for i in range(len(occupied_types)):
            output.write(str(occupied_types[i]) + '    ' + str(available_types[i]) + '\n')
        output.close()
    print('Your file is saved at the following path: ' + out_path)

    return occupation_all_seats

