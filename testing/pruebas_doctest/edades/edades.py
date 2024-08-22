


def edad(numero):
    try:  
        if(numero <= 0):
            return 'No existes'
        if(numero == 3):
            return 'Eres un niño'
        if(numero ==13):
            return 'Eres un puberto'
        if(numero ==17 or numero == 16):
            return 'Eres un adolecente'
        if(numero ==18 or numero == 25):
            return 'Eres un adulto'
        if(numero == 61):
            return 'Eres un adulto mayor'
        if(numero >= 110):
            return 'Eres un mumm-ra'
        if(numero == None):
                return 'Introduce una edad'
    except:
        return 'Edad solo numerica'
    