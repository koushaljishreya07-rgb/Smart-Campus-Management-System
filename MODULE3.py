# Module 3 : Resource Utilization Analysis

def resource_utilization_analysis():

    print("\n*~~~~~~~~~~* RESOURCE USAGE CALCULATION *~~~~~~~~~~*")

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")

    capacity=float(input("Enter total capacity :"))
    actual_usage=float(input("Enter actual usage :"))

    if capacity<=0:
        print("\nInvalid capacity. Capacity must be greater than 0")
        return

    utilization_percentage=(actual_usage/capacity)*100

    print("\n*~~~~~~~~~~* UTILIZATION RESULT *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Total Capacity    :-    ",capacity)
    print("Actual usage      :-    ",actual_usage)
    print("Utilization       :-    ",round(utilization_percentage,2),'%')

    if utilization_percentage<50:
        status="Underutilized"

    elif utilization_percentage<=80:
        status="Efficiently Utilized"
        
    else:
        status="Highly Utilized"

    print("Utilization Status :",status)
