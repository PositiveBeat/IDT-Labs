from math import sqrt



class outliers_begone:
    def __init__(self):
        pass
  


    def purge(self, utm):
        
        accepted = []
        t_prev = utm[0]
        n_prev = utm[1]
        e_prev = utm[2]

        for i, row in enumerate(utm):
            time = row[0]
            northing = row[1]
            easting = row[2]
            
            if (i == 0):
                accepted.append([time, northing, easting])
            
            else:
                dist = sqrt( (northing - n_prev)**2 + (easting - e_prev)**2 )
                time_diff = time - t_prev
                
                print(time_diff)
            
                margin = 0.5 + time_diff*0.1
                if (dist < (1.4 * time_diff + margin)):   # 1.4 meters pr. second + margin
                    accepted.append([time, northing, easting])
                    
                    n_prev = northing
                    e_prev = easting
                    t_prev = time
                
        return accepted


if __name__ == '__main__':
    test = outliers_begone()

    utm = [[1,2,3],[2,2,3],[3,2,3]]
    
    purged = test.purge(utm)
    
    print(purged)







