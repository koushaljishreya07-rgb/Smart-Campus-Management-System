# Module 2 : Resource Usage calculation

def resource_usage_calculation():

    print("\n*~~~~~~~~~~* RESOURCE USAGE CALCULATION *~~~~~~~~~~*")

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")

    print("\nEnter resource usage details ")

    previous_usage=float(input("Enter previous usage :"))
    current_usage=float(input("Enter current usage :"))

    usage_difference=current_usage-previous_usage

    if previous_usage!=0:
        percentage_change=(usage_difference/previous_usage)*100
    else:
        percentage_change=0


    print("\n*~~~~~~~~~~* USAGE RESULT *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Previous Usage    :-    ",previous_usage)
    print("Current Usage     :-    ",current_usage)
    print("usage Difference  :-    ",usage_difference)
    print("Percentage Change :-    ",round(percentage_change,2),'%')


