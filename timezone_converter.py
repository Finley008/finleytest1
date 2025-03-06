from datetime import datetime
import pytz

def display_timezone_options():
    """Display common timezone options"""
    timezones = {
        1: "America/New_York",
        2: "America/Los_Angeles",
        3: "America/Chicago",
        4: "Europe/London",
        5: "Europe/Paris",
        6: "Asia/Tokyo",
        7: "Asia/Dubai",
        8: "Asia/Singapore",
        9: "Australia/Sydney",
        10: "Pacific/Auckland"
    }
    
    print("\nAvailable Timezones:")
    print("-" * 20)
    for key, zone in timezones.items():
        print(f"{key}. {zone}")
    
    return timezones

def get_user_input():
    """Get datetime input from user"""
    try:
        year = int(input("Enter year (e.g., 2025): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        hour = int(input("Enter hour (0-23): "))
        minute = int(input("Enter minute (0-59): "))
        
        return datetime(year, month, day, hour, minute)
    except ValueError:
        print("Invalid date/time input!")
        return None

def convert_timezone(from_time, from_zone, to_zone):
    """Convert time between timezones"""
    try:
        # Create timezone objects
        from_tz = pytz.timezone(from_zone)
        to_tz = pytz.timezone(to_zone)

        # Localize the input time to the source timezone
        localized_time = from_tz.localize(from_time)

        # Convert to the destination timezone
        converted_time = localized_time.astimezone(to_tz)

        return converted_time
    except pytz.exceptions.PytzError as e:
        print(f"Timezone conversion error: {e}")
        return None

def main():
    while True:
        print("\nTimezone Converter")
        print("=" * 20)
        
        # Display timezone options
        timezones = display_timezone_options()
        
        # Get source timezone
        try:
            from_choice = int(input("\nSelect source timezone number (0 to exit): "))
            if from_choice == 0:
                print("Goodbye!")
                break
            if from_choice not in timezones:
                print("Invalid choice!")
                continue
            
            # Get destination timezone
            to_choice = int(input("Select destination timezone number: "))
            if to_choice not in timezones:
                print("Invalid choice!")
                continue
            
            # Get datetime input
            input_time = get_user_input()
            if input_time is None:
                continue
            
            # Convert timezone
            result = convert_timezone(
                input_time,
                timezones[from_choice],
                timezones[to_choice]
            )
            
            if result:
                print("\nResults:")
                print("-" * 20)
                print(f"From: {timezones[from_choice]}")
                print(f"Original time: {input_time}")
                print(f"\nTo: {timezones[to_choice]}")
                print(f"Converted time: {result}")
                
        except ValueError:
            print("Please enter valid numbers!")
            continue

if __name__ == "__main__":
    main()
