class Request():
    def __init__(self,id,name,arrive_time,processing_time,state,algname):
        self.algname= algname

        self.processing_time = processing_time
        self.timeleft=processing_time
        self.arrive_time= arrive_time
        self.id=id
        self.name=name
        self.state=state
        self.waiting_time_till_start = 0

        self.overall_time=0





        # switchtime add 1 with every switch.
        # Probability rozklad cn
        #Don't kick done tasks, we'll be useful stat-wise.
        #dupa w srodku
        #ascii cody
        # average expected time
        #ustalona liczba tasków



    def __str__(self):
        return f'AlgName: {self.algname}\tID: {self.id}\tNAME: {self.name}\tARRIVE_TIME: {self.arrive_time}\tTIMELEFT: {self.timeleft}\tPROCESSING_TIME: {self.processing_time}\tSTATE: {self.state}\tOVERALL_TIME: {self.overall_time}\tWAITING_TIME_TILL_START: {self.waiting_time_till_start}'






