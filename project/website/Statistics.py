import os

@admins.route('/statistics', methods=['GET', 'POST'])
@login_required


def admin_statistics():
    admin = admin_user_checker(current_user)
    if admin:
        # Username = os.getlogin()


        def database_reader(class_variable):

            occupied_types = class_variable.query.filter_by(seat_status='False').all()
            available_types = class_variable.query.filter_by(seat_status='True').all()
            number_types = class_variable.query.all()
            occupation_all_seats = (len(occupied_types) * 100) / len(number_types)
            available_all_seats = 100 - occupation_all_seats
            username = os.getlogin()
            path = os.path.abspath(os.curdir)
            # Project_Path = os.path.dirname(Path)
            out_path = path + r'\Output_Data\\'

            # saveing_directory = r'C:\Users' + '\\' + str(username) + '\\Downloads\\'
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

                for index, letter in enumerate(lines[int(version_counter)]):
                    if letter == ' ':
                        break

                    elif letter.isdigit() or '.':
                        last_availability_entry.append(letter)

                last_availability_entry_liste.append(''.join(last_availability_entry))

                if float(last_availability_entry_liste[0]) == float(occupation_all_seats):
                    print('File not updated, everything up2date')
                    return filename_dictionary

                else:
                    output = open(filename_dictionary, 'a')
                    lines = output.readlines()
                    lines.insert(int(version_counter), str(occupation_all_seats) +
                                 '    ' + str(available_all_seats) + '\n')
                    lines[0] = str('All_Seat_Occupation All_Seat_Availability ' + str(int(version_counter) + 1) + '\n')
                    output.write('Occupied_Seats Available Seats' + '\n')

                    for i in range(len(occupied_types)):
                        output.write(str(occupied_types[i]) + '    ' + str(available_types[i]) + '\n')
            else:
                output = open(filename_dictionary, 'w')
                version_counter = 1
                output.write('All_Seat_Occupation All_Seat_Availability ' + str(version_counter) +
                             '\n' + str(occupation_all_seats) + '    ' + str(available_all_seats) + '\n')
                output.write('Occupied_Seats Available Seats' + '\n')

                for i in range(len(occupied_types)):
                    output.write(str(occupied_types[i]) + '    ' + str(available_types[i]) + '\n')

            print('Your file is saved at the following path: ' + out_path)

            return occupation_all_seats

        print(database_reader(Seat))
    return render_template('admin_statistics.html', user=current_user)
