import numpy as np

# Single machine infinite bus system
class SmibSystem:
    def __init__(self, M, D, P, K):
        self.M = M # inertia
        self.D = D # damping
        self.P = P # power injection/consumption
        self.K = K  # line impedance
        print('SMIB system initialized with M={}, D={}, P={}, K={}'.format(M, D, P, K))

    def __call__(self, t, u):
        phi, omega = u
        dphi = omega
        domega = (self.P - self.D * omega - self.K * np.sin(phi)) / self.M
        return [dphi, domega]

# Two area model
class GeneralModel:
    def __init__(self, Ms, Ds, Ps, Kmatrix, events=[]):
        self.N = len(Ms)
        # Check size of input arrays
        assert len(Ds) == self.N
        assert len(Ps) == self.N
        assert Kmatrix.shape == (self.N, self.N)
        # Set instance parameters
        self.Ms = Ms # inertias
        self.Ds = Ds # dampings
        self.Ps = Ps  # power injections    
        self.Kmatrix = np.array(Kmatrix) # coupling matrix 
        self.events = events

    def __call__(self, t, u):
        # Check for events
        self.check_events(t)
        # Get states 
        phis = u[0:(self.N)]
        omegas = u[self.N:]
        dphis = omegas.copy()
        # Compute interactions
        interactions = np.array([np.sum([self.Kmatrix[i, j] * np.sin(phis[j] - phis[i]) for i in range(self.N)]) for j in range(self.N)])
        # print('I:', (I))
        print('phis:', phis)
        # print('I.shape:', (I.shape)  )
        domegas = (self.Ps - self.Ds * omegas + interactions) / self.Ms
        print('domegas:', domegas)
        print('domegas.shape:', domegas.shape)
        return np.concatenate((dphis, domegas))
    
    def check_events(self, t):
        for event in self.events:
            if event['time'] >= t:
                print('Event at time {}: {}'.format(t, event['message']))
                if 'Ms' in event:
                    self.Ms = event['Ms']
                if 'Ds' in event:
                    self.Ds = event['Ds']
                if 'Ps' in event:
                    self.Ps = event['Ps']
                if 'Kmatrix' in event:
                    self.Kmatrix = event['Kmatrix']