﻿import clr
clr.AddReference("System")

from System import *

def execute(session, request):
	session.Send((Convert.ToInt32(request[0]) * Convert.ToInt32(request[1])).ToString())