def usd_to_inr_conversion():
    try:
        amnt_usd = input("Enter the amnt in USD: ")
        amnt_usd = float(amnt_usd)  

        if amnt_usd < 0:
            raise ValueError("amnt cannot be negative.")
        
        conversion_rate = input("Enter the conversion rate (1 USD to INR): ")
        conversion_rate = float(conversion_rate)  
        
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")

      
        amnt_inr = amnt_usd * conversion_rate
        print(f"{amnt_usd} USD converted at a rate of {conversion_rate} INR/USD is {amnt_inr:.2f} INR")

    except ValueError as e:
        print(f"Invalid input: {e}")


usd_to_inr_conversion()
