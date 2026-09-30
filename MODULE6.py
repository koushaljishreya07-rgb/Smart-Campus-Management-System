# Module 6 : Report Generation

def report_generation():

    print("\n*~~~~~~~~~~* RESOURCE REGISTRATION *~~~~~~~~~~*") 

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")
    resource_type=input("Enter the resource type :")
    location=input("Enter the location :")

    previous_usage=float(input("Enter previous usage :"))
    current_usage=float(input("Enter current usage :"))

    if previous_usage<=0:
        print("\nInvalid previous usage.")
        return

    usage_difference=current_usage-previous_usage

    percentage_change=((usage_difference/previous_usage)*100)

    print("\n*~~~~~~~~~~* RESOURCE ANALYSIS REPORT *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Resource Type     :-    ",resource_type)
    print("Loaction          :-    ",location)

    print("\n*~~~~~~~~~~* RESOURCE STATUS *~~~~~~~~~~*")

    if percentage_change>30:
        status="High Inefficiency"
        recommendation="Immediate optimization is recommended"
        
    elif percentage_change>10:
        status="Moderate increase"
        recommendation="Resource usage should be monitored"
        
    elif percentage_change>=0:
        status="Normal"
        recommendation="Continue efficient resource utilization"
        
    else:
        status="Improved"
        recommendation="Resource consumption has decreased"

    print("Status    :    ",status)

    print("\n*~~~~~~~~~~* RECOMMENDATION *~~~~~~~~~~*")

    print(recommendation)

    print("\n*~~~~~~~~~~* END OF REPORT *~~~~~~~~~~*")
