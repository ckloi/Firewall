import csv

class Rules:
    def __init__(self,dir,p_type,iMin,iMax,pMin,pMax):
        self.direction = dir
        self.type = p_type
        self.ipMin = int(iMin.replace('.',''))
        self.ipMax = int(iMax.replace('.',''))
        self.portMin = int(pMin)
        self.portMax = int(pMax)

    def checkDir(self,dir):
        return self.direction == dir

    def checkIp(self,ip):
        return self.ipMin <= int(ip) <= self.ipMax

    def checkPort(self,port):
        return self.portMin <= int(port) <= self.portMax

class FireWall:
    def __init__(self):
        self.tcpRules = []
        self.udpRules = []

        with open('fw.csv') as csvfile:
            for row in csvfile:
                self.__addRules(row)

    def __addRules(self,row):
        dir,pType,port,ip = row.split(',')

        portMin = ipMin = float('-inf')
        portMax = ipMax = float('inf')

        if '-' in port:
            portMin, portMax = port.split('-')
        else:
            portMin = port
            portMax = port

        if '-' in ip:
            ipMin,ipMax = ip.split('-')
        else:
            ipMin = ip
            ipMax = ip

        if pType == 'tcp':
            self.tcpRules.append(Rules(dir,pType,ipMin,ipMax,portMin,portMax))
        elif pType == 'udp':
            self.udpRules.append(Rules(dir,pType,ipMin,ipMax,portMin,portMax))
        else:
            raise ValueError('Wrong Type.')

    def accept_packet(self,dir,pType,port,ip):

        rules = None

        if pType == 'tcp':
            rules = self.tcpRules
        elif pType == 'udp':
            rules = self.udpRules
        else:
            raise ValueError('Wrong Type.')

        ip = ip.replace('.','')

        for r in rules:
            if r.checkDir(dir) and r.checkIp(ip) and r.checkPort(port):
                return True
        return False
