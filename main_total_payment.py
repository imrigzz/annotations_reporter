import pandas as pd


def total_payment(counts_csv_path, rate):
    csv_input = pd.read_csv(counts_csv_path)
    csv_input.drop(['accept image_ids','ignore image_ids','accept no_spans image_ids','recject image_ids'],axis=1,inplace=True)
    csv_input['Total_payment']=None
    csv_input['Total_payment']=csv_input["accept counts"]*rate
    # print(csv_input)
    csv_input.to_csv('outputs/annotators_payment.csv',index=False)
    print("Payment successfully calculated")
    return csv_input


def main():
    # calculate total payment
    # path to annotator counts csv generated earlier
    counts_csv_path = "outputs/annotators_report.csv"
    rate  = float(input("Please provide the price for per-line annotations: "))
    total_payment(counts_csv_path, rate)



# Call the main() function
if __name__ == "__main__":
    main()