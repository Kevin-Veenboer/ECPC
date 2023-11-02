class ElectronicLoadMeasurement:
    def __init__(self):
        self.Loads = list()
        self.Voltages = list()
        self.Currents = list()
        self.Powers = list()

    # Method to add measurement to instance
    def add_Measurement(self, R, U):
        # append load and volatage to storage lists directly
        self.Loads.append(R)
        self.Voltages.append(U)

        # Calculate the current with voltage/load and store teh result
        self.currents.append(U / R)

        # calculate the power with (U**2/R) this is equal to (I**2 * R), store the result
        self.powers.append(U**2 / R)

    # Methods to retrieve the measurements from an instance
    def get_loads(self):
        return self.Loads

    def get_voltages(self):
        return self.Voltages

    def get_currents(self):
        return self.Currents

    def get_powers(self):
        return self.Powers

    # Method to clear the measurements of instance
    def clear(self):
        self.Loads = list()
        self.Voltages = list()
        self.Currents = list()
        self.Powers = list()
