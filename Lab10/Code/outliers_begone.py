from math import sqrt



class outliers_begone:
    def __init__(self):
        pass


    def purge(self, time, utm):
        
        accepted = []
        t_prev = 0
        n_prev = utm[1][0]
        e_prev = utm[2][0]

        expected_distance = 1.4 # Walking distance over one secind [m]

        for i, row in enumerate(utm):
            t = time[i]
            northing = row[0]
            easting = row[1]
            
            if (i == 0):
                accepted.append([northing, easting])
            
            else:
                dist = sqrt((northing - n_prev)**2 + (easting - e_prev)**2)
                time_diff = t - t_prev

                margin = 0.5 + time_diff * 0.5
                if (dist < (expected_distance * time_diff + margin)):
                    accepted.append([northing, easting])
                    
                    n_prev = northing
                    e_prev = easting
                    t_prev = t
                
        return accepted



if __name__ == '__main__':
    test = outliers_begone()

    utm = [[5,2,3],[5,2,3],[5,2,3]]
    
    purged = test.purge(utm)
    
    print(purged)







