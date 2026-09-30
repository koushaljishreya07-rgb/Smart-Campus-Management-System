# Module 1 : Resource Registration

def resource_registration():
    
    resources=[]
    print("\n*~~~~~~~~~~* RESOURCE REGISTRATION *~~~~~~~~~~*")
    
    while True:
        resource_id=input("Enter the resource ID :")
        resource_name=input("Enter the resource name :")
        resource_type=input("Enter the resource type :")
        location=input("Enter the location :")
        capacity=input("Enter the capacity :")

        resource={"ID": resource_id,
            "Name": resource_name,
            "Type": resource_type,
            "Location": location,
            "Capacity": capacity}

        resources.append(resource)

        print("\nResource Registered Successfully!!!")
        
        choice = input("\nDo you want to register another resource? (yes\no) :")

        if choice.lower()!="yes":
            break

    print("\n*~~~~~~~~~~* REGISTERED RESOURCES *~~~~~~~~~~*")

    for resource in resources:
        print("\nResource Id     :-    ",resource_id)
        print("Resource Name     :-    ",resource_name)
        print("Resource Type     :-    ",resource_type)
        print("Location          :-    ",location)
        print("Capacity          :-    ",capacity)

    return resources
