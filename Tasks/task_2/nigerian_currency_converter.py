# Nigerian Currency Converter
# Step 1: Collect amount in Naira
# Step 2: Collect exchange rates
# Step 3: Perform conversions
# Step 4: Print results

amount_naira = float(input("Enter the amount in Naira: "))
rate_usd = float(input("Enter the exchange rate to US Dollars: "))
rate_gbp = float(input("Enter the exchange rate to British Pounds: "))

amount_usd = amount_naira / rate_usd
amount_gbp = amount_naira / rate_gbp

print("\n--- NIGERIAN CURRENCY CONVERTER ---")
print(f"Amount in Naira:\t₦{amount_naira:,}")
print(f"{'Currency':<8}\t{'Amount':>13}")
print("-" * 45)
print(f"{'USD ($)':<10}\t${amount_usd:,}")
print(f"{'GBP (£)':<10}\t£{amount_gbp:,}")
print("-" * 45 + "")