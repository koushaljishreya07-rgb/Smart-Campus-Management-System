def main_function():
    
    from MODULE1 import resource_registration
    from MODULE2 import resource_usage_calculation
    from MODULE3 import resource_utilization_analysis
    from MODULE4 import inefficiency_detection
    from MODULE5 import optimization_recommendation
    from MODULE6 import report_generation
    from MODULE7 import validate_resource_data

    print("\n***********************************************************************")
    print("                     SMART CAMPUS MANAGEMENT SYSTEM                     ")
    print("\n***********************************************************************")

    print("\n1. Resorce Registration")
    print("2. Resource Usage Calculation")
    print("3. Resource Utilization Analysis")
    print("4. Inefficiency and Wastage Detection")
    print("5. Optimization and Recommendation")
    print("6. Report Generation")
    print("7. Validation and System Control")
    print("8. Exit")
    
    y='yes'
    
    while y=='yes':
        choice=input("\nEnter your choice :")
        
        if choice=='1':
            resource_registration()
        
        elif choice=='2':
            resource_usage_calculation()
    
        elif choice=='3':
            resource_utilization_analysis()
        
        elif choice=='4':
            inefficiency_detection()
        
        elif choice=='5':
            optimization_recommendation()
        
        elif choice=='6':
            report_generation()
        
        elif choice=='7':
            validate_resource_data()
    
        elif choice=='8':
            print("\nExiting the system...!")
            break
    
        else:
            print("\nInvalid choice! Please enter the number from 1 to 8.")
            n=input('Enter yes for continue :')
            y=n.lower()

main_function()

