-- Load data/bookings.csv (created by python/prepare_data.py).
-- Run with:  mysql --local-infile=1 -u <user> -p
-- Change the path below to the absolute path of bookings.csv on your machine.
USE Ola;

LOAD DATA LOCAL INFILE '/path/to/ola-ride-analytics/data/bookings.csv'
INTO TABLE bookings
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(Date, Time, Booking_ID, Booking_Status, Customer_ID, Vehicle_Type,
 Pickup_Location, Drop_Location, @v_tat, @c_tat, @cc, @cd, @inc, @inc_reason,
 Booking_Value, @pay, Ride_Distance, @dr, @cr)
SET V_TAT = NULLIF(@v_tat, ''),
    C_TAT = NULLIF(@c_tat, ''),
    Canceled_Rides_by_Customer = NULLIF(@cc, ''),
    Canceled_Rides_by_Driver   = NULLIF(@cd, ''),
    Incomplete_Rides           = NULLIF(@inc, ''),
    Incomplete_Rides_Reason    = NULLIF(@inc_reason, ''),
    Payment_Method             = NULLIF(@pay, ''),
    Driver_Ratings             = NULLIF(@dr, ''),
    Customer_Rating            = NULLIF(@cr, '');

SELECT COUNT(*) AS rows_loaded FROM bookings;   -- expect 103024
