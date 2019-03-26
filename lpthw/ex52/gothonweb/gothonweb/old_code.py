if room_name == 'laser_weapon_armory':
            room = planisphere.load_room(room_name)
            
            action = request.form.get('action')
            guesses = 0
            while action != '123' and guesses < 3:
                guesses = guesses + 1
                pdb.set_trace()
                return render_template("show_room.html", room=room)
            else:
                return render_template("you_died.html")
                #pdb.set_trace()


#pdb.set_trace()                        
        # if a room object doesn't exist on that direccion
        if not next_room:
            # saves planisphere scenes' key 'central_corridor' as value for session's key 'room_name'
            session['room_name'] = planisphere.name_room(room)
        else:
            session['room_name'] = planisphere.name_room(next_room)