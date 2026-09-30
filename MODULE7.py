# Module 7 : Validation and System Control

def validate_resource_data():

    print("\n*~~~~~~~~~~* DATA VALIDATION AND SYSTEM CONTROL *~~~~~~~~~~*")

    resource_id=input("Enter the resource ID :")
    resource_name=input("Enter the resource name :")
    resource_type=input("Enter the resource type :")
    location=input("Enter the location :")

    print("\nEnter resource capacity ")

    try:
        capacity=float(input("Capacity :"))

        if capacity<=0:
            print("\nInvalid data!")
            print("Capacity must be greater than 0.")
            return

    except ValueError:
        print("\nInvalid Data!")
        print("Capacity must be number.")
        return

    if resource_id.strip()=="":
        print("\nInvalid Data!")
        print("Resource ID cannot be empty")
        return

    if resource_name.strip()=="":
        print("\nInvalid Data!")
        print("Resource name cannot be empty.")

    if resource_type.strip()=="":
        print("\nInvalid Data!")
        print("Resource type cannot be empty.")
        return

    if location.strip()=="":
        print("\nInvalid Data!")
        print("Location cannot be empty.")
        return

    print("\n*~~~~~~~~~~* VALIDATION RESULT *~~~~~~~~~~*")

    print("\nResource Id     :-    ",resource_id)
    print("Resource Name     :-    ",resource_name)
    print("Resource Type     :-    ",resource_type)
    print("Loaction          :-    ",location)
    print("Capacity          :-    ",capacity)

    print("\nData Validation Successful!!!")
    print("All entered information is valid.")


