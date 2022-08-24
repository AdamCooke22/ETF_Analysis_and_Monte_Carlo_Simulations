import sys
import fire
import questionary

def suggestion_questionaire():
    """Suggest ETFs based on risk, time and type.

    Args:
        None
    """

    important_aspect_response = str(questionary.text("What is the most important aspect of your investment (RISK, TIME, TYPE)?").ask())
    #print ("You said " + important_aspect_response )
    if important_aspect_response.lower() == "risk" :
        #TODO  Do risk stuff
        level_of_risk_response = str(questionary.text("What level of risk you are comfortable with or willing to take (little, moderate, high)?").ask())
        #print ("You said " + level_of_risk_response )  
        if level_of_risk_response.lower() == "little" :
            print ("Please invest in the ETF with the lowest standard deviation (STD). We suggest: BND. The annualized STD of the ETFs are -> BND: 0.050045, VIG: 0.181407, SNP: 0.206733, VOX: 0.217649, VNQ: 0.318735")
        elif level_of_risk_response.lower() == "moderate" :
            print ("You need to invest in the ETFs with the median standard deviation (STD). We suggest: VIG, SNP, VOX. The annualized STD of the ETFs are -> BND: 0.050045, VIG: 0.181407, SNP: 0.206733, VOX: 0.217649, VNQ: 0.318735")
            type_of_etf_response = str(questionary.text("what is the type of investment you are comfortable to invest in? \n \
            1- MutualFunds, \n \
            2- Specialty/sector ETFs, \n \
            3- Dividend ETFs)?").ask())
            if type_of_etf_response == "1" :
                print ("Please invest in SNP.") 
            elif type_of_etf_response == "2" :
                print ("Please invest in VOX.") 
            elif type_of_etf_response == "3" :
                print ("Please invest in VIG.")        
        elif level_of_risk_response.lower() == "high" :
            print ("Please invest in the ETF with the highest STD Example: VNQ. The annualized STD of the ETFs are -> BND: 0.050045, VIG: 0.181407, SNP: 0.206733, VOX: 0.217649, VNQ: 0.318735")
    elif important_aspect_response.lower() == "type" :
        #TODO  Do type stuff
        type_of_etf_response = str(questionary.text("what is the type of investment you are comfortable ? \n \
        1- MutualFunds,  \n \
        2- Bond/Fixed Income ETFs,  \n \
        3- Real Estate ETFs,  \n \
        4- Specialty/sector ETFs,  \n \
        5- Dividend ETFs)?").ask())
        if type_of_etf_response == "1" :
            print ("Please invest in SNP. SNP is a mixture of different mutual funds") 
        elif type_of_etf_response == "2" :
            print ("Please invest in BND. BND focuses on investing in bonds or fixed-income securities.") 
        elif type_of_etf_response == "3" :
            print ("Please invest in VNQ. VNQ focuses on investing in real estate.")  
        elif type_of_etf_response == "4" :
            print ("Please invest in VOX. VOX focuses on investing in communication sector.") 
        elif type_of_etf_response == "5" :
            print ("Please invest in VIG. VIG focuses on investing in to high dividend returns.")  
    elif important_aspect_response.lower() == "time" :
        #TODO  Do time stuff
        timeperiod_response = str(questionary.text("Are you interested in investing for 2, 5, 10+ years?").ask())
        #print ("You said " + timeperiod_response )  
        if timeperiod_response.lower() == "2" :
            print ("We recommend to invest in VIG. The short term average future performance of VIG is 1.2485. The short term average future performance of the other ETFs are: SNP: 1.2135, BND: 1.2296, VNQ: 1.2101, and VOX: 1.1130")
        elif timeperiod_response.lower() == "5" :
            print ("We recommend to invest in VIG, VNQ or SNP. The medium term average future performance of the ETFS are: SNP: 1.6341, BND: 1.1785, VNQ: 1.6442, VOX: 1.3314 and VIG: 1.6668.")
        elif timeperiod_response.lower() == "10+" :
            print ("We recommend to invest in VNQ. The long term average future performance of the ETFs are: SNP: 2.4541, BND: 1.3851, VNQ: 2.8746, VOX: 1.8839, and VIG: 2.7883.")



if __name__ == "__main__":
    fire.Fire(suggestion_questionaire)