# Module 4 : Inefficiency and Waste Management

def inefficiency_detection():

    print("\n*~~~~~~~~~~* RESOURCE USAGE CALCULATION *~~~~~~~~~~*")

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")

    previous_usage=float(input("Enter previous usage :"))
    current_usage=float(input("Enter current usage :"))

    if previous_usage<=0:
        print("\nInvalif previous usage.")
        return

    usage_difference=current_usage-previous_usage
    percentage_increase=(usage_difference/previous_usage)*100

    print("\n*~~~~~~~~~~* ANANLYSIS RESULT *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Previous Usage    :-    ",previous_usage)
    print("Current Usage     :-    ",current_usage)
    print("Usage Increase    :-    ",round(usage_difference,2))
    print("Percentage Increase :-   ",round(percentage_increase,2),'%')

    if percentage_increase>30:
        print("Status    :    High Inefficiency Detected")
        print("Alert     :    Possible resource wastage.")
        
    elif percentage_increase>10:
        print("Status    :    Moderate Increase")
        print("Alert     :    Resource usage should be monitored.")
        
    elif percentage_increase>=0:
        print("Status    :    Normal Usage")
        print("Alert     :    No significant inefficiency detected.")
        
    else:
        print("Status    :    Reduced Usage")
        print("Alert     :    Resource consumption has decreased.")

