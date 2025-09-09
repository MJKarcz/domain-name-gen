def prompt_template(num_records: int = 5):


    return f"""You are an expert synthetic data generator assisting a machine learning engineer in creating a high-quality instruction tuning dataset.  
    Your task is to generate **business description and domain name examples pairs** that will be used 
    to fine-tune a language model.  
    
    Generate a JSON with {num_records} entries, containing:  
    - A realistic **business description** (short paragraph, 1–3 sentences).  
    - One or more **domain name suggestions** that fit the business description.  
    - Ensure domain names vary in style (short, creative, keyword-based, professional, playful) and complexity and that they mach **business description**.  
    
    The output must be valid JSON. Each entry should have the following fields:  
    
        "business_description": "Concise description of the business or service...",  
        "domain_names": ["example1.com", "example2.io", "example3.net"]  
    
    Guidelines:  
    - Include examples from different industries (e.g., tech, retail, education, health, entertainment, logistics, environment, nonprofits, etc.).  
    - Ensure a mix of complexity: from simple/local businesses to large/global enterprises. 
    - New model must be able to exclude any inappropriate content. Therefore provide busineess descriptions that mention any sexual, adult, or inappropriate content. "domain_names" to have one element:
      Request rejected: inappropriate content.
    
    Examples:  
    
        {{  
            "business_description": "An eco-friendly cleaning service specializing in biodegradable products for urban households.",  
            "domain_names": ["GreenCleaners.com", "EcoUrbanClean.io", "BioFreshServices.net"]  
        }}  

           
    
        {{  
            "business_description": "Adult website with explicit nude content",  
            "domain_names": ["Request rejected: inappropriate content"]  
        }}  
    
    By following these guidelines, you’ll contribute to a diverse and ethically sound dataset that helps the model learn how to suggest 
    domain names across contexts, while rejecting harmful or sensitive requests.  
    """


if __name__ == "__main__":
    print(prompt_template(10))