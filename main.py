def main():
    from interfaces.interfaces import AbstractLocalMeasurementDevice
    lmd = AbstractLocalMeasurementDevice() # Expecting error methods not implemented.

    from interfaces.informationObjects import GridVoltageReading
    print(GridVoltageReading(voltage=230))


if __name__ == "__main__":
    main()
