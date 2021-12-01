#!/usr/bin/python
#/****************************************************************************
# QGroundControl example
# Copyright (c) 2018, Kjeld Jensen <kjen@mmmi.sdu.dk> <kj@kjen.dk>
# http://sdu.dk/uas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#****************************************************************************/
'''
2018-03-20 Kjeld Jensen, first version
2021-01-12 Nicoline L. Thomsen, created class for general use
'''

import json


class planclass:
    def __init__(self, filename):
        self.filename = filename

        self.plan = {}
        self.items = []

    
    def begin(self, groundstation):
        geoFence = {}
        self.plan['fileType'] = 'Plan'

        geoFence['polygon'] = [] 
        geoFence['version'] = 1 
        self.plan['geoFence'] = geoFence

        self.plan['groundStation'] = groundstation


    def record_plan(self, geodetic, altitude):

        for i in range(len(geodetic)):

            command = 22 if i == 0 else 16  # Set initial command

            item = {}
            item['autoContinue'] = True
            item['command'] = command
            item['doJumpId'] = i + 1
            item['frame'] = 3
            item['params'] = [0,0,0,0, geodetic[i][0], geodetic[i][1], altitude]
            item['type'] = 'SimpleItem'
            self.items.append (item)


    def end(self, home_position):
        mission = {}
        mission['cruiseSpeed'] = 15
        mission['firmwareType'] = 3
        mission['hoverSpeed'] = 5
        mission['items'] = self.items
        mission['plannedHomePosition'] = home_position
        mission['vehicleType'] = 2
        mission['version'] = 2
        self.plan['mission'] = mission

        rallyPoints = {}
        rallyPoints['points'] = [] 
        rallyPoints['version'] = 1 
        self.plan['rallyPoints'] = rallyPoints

        self.plan['version'] = 1

        plan_json = json.dumps(self.plan, indent=4, sort_keys=True)

        file = open(self.filename, 'w') 
        file.write (plan_json)
        file.close()