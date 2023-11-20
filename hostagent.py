from sys import argv
import threading
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import start_loop
from truckagent import TruckAgent
from pade.core.agent import Agent

from globals import Global
from gui import Gui

class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        self.agent.truck.move()

        gui.update()

class YourTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(YourTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(YourTimedBehaviour, self).on_time()
        
        

class HostAgent(Agent):
    gui = None
    truck = None

    def __init__(self, aid, extra_parameter=None):
        super(HostAgent, 
              self).__init__(aid=aid, debug=False)

        self.truck = TruckAgent(extra_parameter)

        mytimed = MyTimedBehaviour(self, .9)
        yourtimed = YourTimedBehaviour(self, 9)
        self.behaviours.append(mytimed)
        self.behaviours.append(yourtimed)

def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    c=0
    agents = list()
    for i in range(Global.num_trucks):
        port = int(argv[1]) + c
        host_agent_name = 'agent_hello_{}@localhost:{}'.format(port, port)
        host_agent = HostAgent(AID(name=host_agent_name),i+1)
        agents.append(host_agent)
        c += 1

    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    gui = Gui(agents)
    gui.show()
    app.exec()
    x.join()
