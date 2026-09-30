# Module 5 : Optimization and Recommendation

def optimization_recommendation():

    print("\n*~~~~~~~~~~* RESOURCE USAGE CALCULATION *~~~~~~~~~~*")

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")
    resource_type=input("Enter the resource type :")

    previous_usage=float(input("Enter previous usage :"))
    current_usage=float(input("Enter current usage :"))

    if previous_usage<=0:
        print("\nInvalid previous usage.")
        return

    percentage_change=((current_usage-previous_usage)/previous_usage)*100

    print("\n*~~~~~~~~~~* OPTIMIZATION ANALYSIS *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Resource Type     :-    ",resource_type)
    print("Usage Change      :-    ",round(percentage_change,2),'%')

    print("\nRecommendation :")

    if percentage_change>30:
        print("High resource consumption detected :-")

        if resource_type.lower()=="electricity":
            print("Switch off unecessary electrical equipment.")
            print("Monitor equipment during during low-occupancy periods.")
            print("Review operating hours.")
            
        elif resource_type.lower()=="water":
            print("Check for possible water leakage.")
            print("Reduce unnecessary water usage.")
            print("Monitor water consumption regularly.")
            
        elif resource_type.lower()=="classroom":
            print("Review classroom utilization.")
            print("Consider reallocating classes according to occupancy.")
        elif resource_type.lower()=="laboratory":
            print("Review laboratory usage hours.")
            print("Avoid unnecessary operation of laboratory equipment.")
            
        else:
            print("Monitor the resource regularly.")
            print("Investigate the reason for increased consumption.")
            print("optimize usage during low-demand periods.")

    elif percentage_change>10:
        print("Moderate increase in resource usage detected.")
        print("Continue monitoring the resource.")
        print("Compare future usage with the average.")
        print("Identify possible cause of increased consumption.")

    elif percentage_change>=0:
        print("Resource usage is within the normal range.")
        print("Continue regular monitoring.")
        print("Maintain efficient resource usage.")

    else:
        print("Resource usage has decreased.")
        print("Current usage is improving.")
        print("Maintain efficient resource usage.")

