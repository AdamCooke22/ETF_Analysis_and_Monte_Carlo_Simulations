import sys
import fire
import questionary

def suggestion_questionaire():
    """Suggest ETFs based on risk, time and type.

    Args:
        None
    """

    important_aspect_response = str(questionary.text("what is the most important aspect of your investment (RISK, TIME, TYPE)?").ask())
    #print ("You said " + important_aspect_response )
    if important_aspect_response.lower() == "risk" :
        #TODO  Do risk stuff
        level_of_risk_response = str(questionary.text("what level of risk you are comfortable with (little, moderate, high)?").ask())
        #print ("You said " + level_of_risk_response )  
        if level_of_risk_response.lower() == "little" :
            print ("Please invest in the ETF with the lowest STD. Example: BND")
        elif level_of_risk_response.lower() == "moderate" :
            print ("You need to invest in the ETFs with the median STD.")
            type_of_etf_response = str(questionary.text("what is the type of investment you are comfortable ? \n \
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
            print ("Please invest in the ETF with the highest STD Example: VNQ")
    elif important_aspect_response.lower() == "type" :
        #TODO  Do type stuff
        type_of_etf_response = str(questionary.text("what is the type of investment you are comfortable ? \n \
        1- MutualFunds,  \n \
        2- Bond/Fixed Income ETFs,  \n \
        3- Real Estate ETFs,  \n \
        4- Specialty/sector ETFs,  \n \
        5- Dividend ETFs)?").ask())
        if type_of_etf_response == "1" :
            print ("Please invest in SNP.") 
        elif type_of_etf_response == "2" :
            print ("Please invest in BND.") 
        elif type_of_etf_response == "3" :
            print ("Please invest in VNQ.")  
        elif type_of_etf_response == "4" :
            print ("Please invest in VOX.") 
        elif type_of_etf_response == "5" :
            print ("Please invest in VIG.")  
    elif important_aspect_response.lower() == "time" :
        #TODO  Do time stuff
        timeperiod_response = str(questionary.text("Are you interested in investing for 2, 5, 10+ years?").ask())
        #print ("You said " + timeperiod_response )  
        if timeperiod_response.lower() == "2" :
            print ("Recommendation for 2 years")
        elif timeperiod_response.lower() == "5" :
            print ("Recommendation for 5 years.")
        elif timeperiod_response.lower() == "10+" :
            print ("Recommendation for 10 or more years.")



if __name__ == "__main__":
    fire.Fire(suggestion_questionaire)