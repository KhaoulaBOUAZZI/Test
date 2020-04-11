from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import numpy as np


class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2: implement this method
        """
        B=[]
        for value in (self.peer_pool.values()):
            B.append(value)
        return B


class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2: implement this method
        """
        durations=[]
        for i in range(len(self.network)):
            durations.extend(self.network[i].send_data_to_backend())
        return compute_histogram_bins(data=durations, bins=BINS)

if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()


    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
