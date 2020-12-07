# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:06:52 2019

@author: jackw
"""

"""Example to scrape a list of Companies, and put overviews in csv form"""

from scrape_linkedin import CompanyScraper
import pandas as pd



# ---------------------------------------- READIN PRODUCTS --------------------------------------------------------------

newproducts = []

# Need to download new products from drive then reduce the .csv to one column containing linkedin urls 

# Enter csv file name below
newproducts = pd.read_csv('', squeeze = 'true')


#driver = webdriver.Chrome('C:/Users/jackw/webdriver.py')

# LIST YOUR COMPANIES HERE
my_company_list = newproducts

company_data = []


 # ------------------------------------ RUN SCRAPER FOR EACH COMPANY ------------------------------------------------------------------------------------------------------------------------------
 
 
with CompanyScraper(cookie='') as scraper:
    
    # Get each company's overview, add to company_data list
    for name in my_company_list:
        overview = scraper.scrape(company=name).overview
        overview['company_name'] = name
        
        
        overviewkeys = ['description','name','website','industry','company_size','headquarters','type','founded','num_employees','image','company_name']
        for y in overviewkeys:
            if overview.get(y) == None:
                overview[y] = ''
                
        
        # Clean-up data - rearrange dataframe
        
        del[overview['headquarters']]
        del[overview['name']]
        del[overview['num_employees']]
        
        overview['HQ'] = overview.pop('company_size')
        
        overview['company_tags'] = overview.pop('founded')
        
        overview['founded'] = overview.pop('type')
        
        
        
        
        
# --------------------------------------------- CATEGORIES ----------------------------------------------------------------------------------------------------------------------------------------------  
      
        
        # Catagorisation methods - initalise category variables 
        
        overview['Catagory'] = ''
        overview['SubCategory'] = ''
        
        
        # Categorise based on keyword in description - comment this section out for manual categorisation
      
# ---------------------------- FINCRIME ---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Financial Crime
        fincrime = ["KYC","AML","Financial Crime","CTF","Fraud","fraud","Onboarding","CDD","Customer due dilligence","FinCrime","PEPs","sanctions","adverse media","transaction monitoring","identity verification","counter-terrorism financing","anti-money laundering","kyc","aml","Digital KYC"]
        for x in fincrime:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Financial Crime"    
                else:
                    overview['Catagory'] += ", Financial Crime"
                break
        
        # Financial Crime - sub category
        if "Financial Crime" in overview['Catagory']:
            
            # Namescreening
            namescreen = ["Name Screening","name screening","PEPs","Sanctions","sanctions","adverse media","Adverse Media"]
            for x in namescreen:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Name Screening"    
                    else:
                        overview['SubCategory'] += ", Name Screening"
                    break
            
            # Fraud
            fraud = ["fraud","Fraud","fraud monitoring","fraud detection","real-time monitoring"]
            for x in fraud:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Fraud, real-time monitoring"    
                    else:
                        overview['SubCategory'] += ", Fraud, real-time monitoring"
                    break
            
            # CDD
            cdd = ["KYC","ID&V","identity and verification","verification","risk assesment","Know Your Customer"]
            for x in cdd:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "CDD"    
                    else:
                        overview['SubCategory'] += ", CDD"
                    break
            
            # Third party risk
            thirdpartyrisk = ["Third party risk management","3rd party risk management","Third Party Risk Management","3rd Party Risk"]
            for x in thirdpartyrisk:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "3rd Party Risk Management"    
                    else:
                        overview['SubCategory'] += ", 3rd Party Risk Management"
                    break
                
            # Transaction Monitoring
            transmon = ["Transaction Monitoring","Suspicious transaction reporting","transaction monitoring","AML","aml"]
            for x in transmon:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Transaction Monitoring"    
                    else:
                        overview['SubCategory'] += ", Transaction Monitoring"
                    break


#--------------------------- REGCHANGE -------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
                
                
        # Regulatory Change
        regchange = ["Regulatory Change","Reg change","analyse new regulations","legislation changes","regulatory complexity","regulatory change","Regulatory change","monitor regulatory content"]
        for x in regchange:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Regulatory Change"
                else:
                    overview['Catagory'] += ", Regulatory Change"
                break
        
        
# -------------------------- CYBER/DATAPRIV/IDENT -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # Cyber/Data Privacy/Identity
        priv = ["privacy","GDPR","data protection","data privacy","cybersecurity","cyber security","biometrics","PII","CCPA","PET","COPPA","CalOPPA","PECR","PIPEDA","CASL","ePrivacy","identity verification","digital identity","Cybersecurity","authentication","behavioural authentication","security as a service","SOC","MSSP","MDR","synthetic data","Data Protection","Privacy Compliance","Data Loss Prevention","data loss prevention","cyber risk"]
        for x in priv:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Cyber/Data Privacy/Identity"
                else:
                    overview['Catagory'] += ", Cyber/Data Privacy/Identity"
                break
            
                    
        # Cyber/Data Privacy/Identity sub-categories
        if "Cyber/Data Privacy/Identity" in overview['Catagory']:
            
            # Cyber Security
            cyber = ["CyberSecurity","cybersecurity","cyber attacks","Cyber Security","Security Testing","Vulnerability Assesment","Threat Intelligence","threat intelligence","protection"]
            for x in cyber:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Cyber Security"    
                    else:
                        overview['SubCategory'] += ", Cyber Security"
                    break
            
            # ID
            ident = ["Identity","identity","internal actors"]
            for x in ident:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Identity"    
                    else:
                        overview['SubCategory'] += ", Identity"
                    break
            
            # Data Privacy
            datapriv = ["Data Privacy","data privacy","privacy enhancing technology","PET","GDPR","privacy regulations","Privacy"]
            for x in datapriv:
                if x in overview['description'] or x in overview['company_tags']:
                    if len(overview['SubCategory']) == 0:
                        overview['SubCategory'] = "Data Privacy"    
                    else:
                        overview['SubCategory'] += ", Data Privacy"
                    break
            
            
    
# --------------------------------------------- REGREPORTING ------------------------------------------------------------------------------------------------------------------------    
        
            
        # Regulatory Reporting
        regreport = ["Regulatory Reporting","Reg reporting","regulatory reporting","COREP","CRR","CRD IV","FINREP","legislative reporting"]
        for x in regreport:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Regulatory Reporting"
                else:
                    overview['Catagory'] += ", Regulatory Reporting"
                break
            
            
# ------------------------------- MARKETINTEG&TRANS -------------------------------------------------------------------------------------------------------------------------------------
            
            
        # Market Integrity and Transparency
        mintegtrans = ["Insider dealing","market manipulation","MiFID II","MiFID 2","Dodd-Frank","market transparency","Market surveillance","market abuse and misconduct","market abuse"]
        for x in mintegtrans:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Market Integrity and Transparency"
                else:
                    overview['Catagory'] += ", Market Integrity and Transparency"
                break
                

# ------------------------------------ REGRISK&CALCS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
            
        # Regulatory Risk Analytics and Calculations
        riskcalc = ["Regulatory Risk Analytics and Calculations","capital allocation","stress testing","Basel 3","Solvency 2","risk calculations","Basel III","AIFMD FRTB","Solvency II","UCITS IV","scenario analysis","risk simulations"]
        for x in riskcalc:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Regulatory Risk Analytics and Calculations"
                else:
                    overview['Catagory'] += ", Regulatory Risk Analytics and Calculations"
                break
            
            
# ------------------------------------------- REGDATA&INFOMANAGE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            
        # Regulatory Data and Information Management
        dataandinfo = ["Regulatory Data and Information Management","BCBS 239","KID","Aggregation of data","Data Governance","Metadata Management","aggregates data","data sharing","spreadsheet management","spreadsheet governance","Data Management"]
        for x in dataandinfo:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Regulatory Data and Information Management"
                else:
                    overview['Catagory'] += ", Regulatory Data and Information Management"
                break
            
        
# ---------------------------- TAXCOMPLIANCE ------------------------------------------------------------------------------------------------------------------------------------------------------        


        # Tax Compliance
        taxcomp = ["Tax Compliance","tax compliance","FATCA","UK’s Making Tax Digital initiative","OECD CRS","CRS","AEOI","IRS","HMRC","Accounting","tax issues","VAT","Tax"]
        for x in taxcomp:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "Tax Compliance"
                else:
                    overview['Catagory'] += ", Tax Compliance"
                break
        


# ---------------------------- ESG ------------------------------------------------------------------------------------------------------------------------------------------------------        


        # ESG
        esg = ["ESG","SRI","socially responsible","environmental","social"]
        for x in esg:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Catagory']) == 0:
                    overview['Catagory'] = "ESG"
                else:
                    overview['Catagory'] += ", ESG"
                break

        
        
# ------------------------------------ TECHNOLOGY ----------------------------------------------------------------------------------------------------------------------------------------------------        
        
        
        overview['Underlying Tech'] = ''
        
        # Underlying tech
        
        ai = ["Artificial Intelligence","artificial intelligence","Machine learning","Machine Learning","machine learning","supervised","unsupervised","Supervised","Unsupervised","Machine intelligence"]
        for x in ai:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "AI/ML"
                else:
                    overview['Underlying Tech'] += ", AI/ML"
                break
        
        blockchain = ["Blockchain","blockchain","MultiChain","Blockchain-as-a-service"]
        for x in blockchain:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "Blockchain"
                else:
                    overview['Underlying Tech'] += ", Blockchain"
                break
        
        
        dlt = ["Distributed Ledger","distributed ledger","DLT","dlt","shared ledger","distributed ledger technology"]
        for x in dlt:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "DLT"
                else:
                    overview['Underlying Tech'] += ", DLT"
                break        

        nlp = ["NLP","nlp","Natural language processing","Natural Language Processing","natural language processing","natural language understanding"]
        for x in nlp:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "NLP"
                else:
                    overview['Underlying Tech'] += ", NLP"
                break  

        rpa = ["RPA","rpa","Robotic process automation","Robotic Process Automation","robotics","digital workforce","Digital Workforce"]
        for x in rpa:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "RPA"
                else:
                    overview['Underlying Tech'] += ", RPA"
                break  
        
        
        cloud = ["Cloud","cloud","AWS","Amazon web services","Cloud computing","Cloud strategy","Cloud security","Cloud platform","Microsoft Azure","Google Cloud Platform"]
        for x in cloud:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Underlying Tech']) == 0:
                    overview['Underlying Tech'] = "Cloud"
                else:
                    overview['Underlying Tech'] += ", Cloud"
                break  
        
        
        
# ---------------------------------- REGULATION -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Automate regulation adressed depending on keywords in description
        
        overview['Regulation'] = ''
           
        regs = ["MiFID","EMIR","SFTR","MAR","GDPR","FATCA","Basel 2","Basel 3","CRD","CRR","MAD","AIFMD","AMLD","PSD2","CSD","SRD","ESG","LIBOR","Basel II","Basel III","BRRD","FINREP","COREP","DFA","Dodd-Frank"]
        for x in regs:
            if x in overview['description'] or x in overview['company_tags']:
                if len(overview['Regulation']) == 0:
                    overview['Regulation'] = x
                else:
                    overview['Regulation'] += ", " + x
            
            
            
            
       
# ------------------------------------ MATURITY -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # New kid/Challenger/Incumbent - NOT NEEDED -> AUTOMATION IN SHEETS
        #if overview['founded'] != '' and len(overview['founded']) == 4:
        #    i = overview['founded']  
        #    i = int(i)
        #    if i >= 2013:
        #        overview['Maturity'] = "New kid"
        #    elif i >= 2005:
        #        overview['Maturity'] = "Challenger"
        #    else:
        #        overview['Maturity'] = "Incumbent"
        
       
# --------------------------------------------------------------------------------------------------------
        # Append collected data to each scraped product        
        company_data.append(overview)


        
# Turn into dataframe for easy csv output
df = pd.DataFrame(company_data)
# Name output file below - saved to working directory
df.to_csv('', index=False)

