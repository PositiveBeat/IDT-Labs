from math import sqrt



class outliers_begone:
    def __init__(self):
        pass
  


    def purge(self, utm):
        
        accepted = []
        n_prev = 0
        e_prev = 0
        t_prev = 0

        for i, row in enumerate(utm):
            time = row[0]
            northing = row[1]
            easting = row[2]
            
            if (i == 0):
                accepted.append([time, northing, easting])
            
            else:
                dist = sqrt( (northing - n_prev)**2 + (easting - e_prev)**2 )
                time_diff = time - t_prev
            
                if (dist < (1.4 * time_diff + 0.5)):   # 1.4 meters pr. second + margin
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







