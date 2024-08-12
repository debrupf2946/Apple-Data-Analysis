class FirstWorkFlow:
    """
    ETL pipeline to generate the data for all customers who have bought Airpods just after buying iPhone
    """ 
    def __init__(self):
        pass

    def runner(self):

        # Step 1: Extract all required data from different source
        inputDFs = AirpodsAfterIphoneExtractor().extract()

        # Step 2: Implement the Transformation logic
        # Customers who have bought Airpods after buying the iPhone
        firstTransformedDF = AirpodsAfterIphoneTransformer().transform(inputDFs)

        # Step 3: Load all required data to differnt sink
        AirPodsAfterIphoneLoader(firstTransformedDF).sink()
        