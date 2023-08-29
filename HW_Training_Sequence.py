import random
import Core.ValidationError as ValidationError
import PyBuffer
import os
import json
import subprocess
import Protocol.SCSI.Basic.TestCase as TestCase
import CTFServiceWrapper as PyServiceWrap
import ScsiCmdWrapper as PyScsiWrap
from ScsiCmdLib import *

import json
import requests
import csv

class HW_Training_Sequence(TestCase.TestCase):
    MULT_Data = []
    CE = [0,1]
    Die = [0,1,2,3]
    def setup(self):
        otherHW = dict()   
        otherHW["SerialCommunication"] = "HIDAndCOMPorts"
        scsiSession = PyServiceWrap.Session.GetSessionObject(PyServiceWrap.SCSI_Protocol, PyServiceWrap.DRIVER_TYPE.WIN_USB, otherHW)
        configParser = scsiSession.GetConfigInfo()
        configParser.SetValue("adapter_index",0)

    def DoPowerCycle(self):
        gsdCmd = PyServiceWrap.PowerCycle(shutdownType=PyServiceWrap.SHUTDOWN_TYPE.GRACEFUL, pModelPowerParamsObj=None, pGPIOMap=None)
        gsdCmd.Execute()
        print("Power Cycle Complete")

    def readFile(self):
        #Read HWDump.bin rec-> Convert to hex string -> int 
        tempHexDump = open("HWDump.bin",'rb')
        tempHexDump = tempHexDump.read(8)
        hex_list = ["{:02x}".format(ord(c)) for c in tempHexDump]
        int_list = [int(hex_string, 16) for hex_string in hex_list]
        return int_list
    
    def issueTrainingCmd(self,CE,Die):
        dataBuffer = PyServiceWrap.Buffer.CreateBuffer(1)
        diagCmd = PyServiceWrap.DIAG_FBCC_CDB()
        diagCmd.cdbLen = 16
        diagCmd.cdb = [0] * 16
        diagCmd.cdb[0] = 0xF7
        diagCmd.cdb[1] = int(CE[0])
        diagCmd.cdb[2] = int(Die[0])
        sctpCommand = PyServiceWrap.SCTPCommand.SCTPCommand(diagCmd, dataBuffer, PyServiceWrap.DIRECTION_OUT)
        sctpCommand.Execute()       
        dataBuffer.WriteToFile("HWDump.bin",4)
        mult_data = self.readFile()
        HW_Training_Sequence.MULT_Data += [mult_data]

    def getMultData(self):
        return HW_Training_Sequence.MULT_Data

    def testHW_Training_Sequence(self):
        self.DoPowerCycle()
        self.setup()
        for ce in HW_Training_Sequence.CE:
            for die in HW_Training_Sequence.Die:
                self.issueTrainingCmd(HW_Training_Sequence.CE,HW_Training_Sequence.Die)
        
        HW_Training_Sequence.MULT_Data = [[str(num) for num in sublist] for sublist in HW_Training_Sequence.MULT_Data]
        for ce in HW_Training_Sequence.CE:
            for die in HW_Training_Sequence.Die:
                index = ce*len(HW_Training_Sequence.Die)+die
                string = "CE "+str(ce)+" Die "+str(die)
                HW_Training_Sequence.MULT_Data[index].insert(0,string)
        print(HW_Training_Sequence.MULT_Data)

        file_path="HW_Chaz.csv"
        with open(file_path, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(HW_Training_Sequence.MULT_Data)
