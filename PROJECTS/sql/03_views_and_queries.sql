-- Ola Bengaluru Ride Analytics | the 10 SQL questions from the project brief
-- NOTE: the dataset uses US spelling ("Canceled"), so filters use that spelling.
USE Ola;

-- 1. Retrieve all successful bookings
CREATE OR REPLACE VIEW Successful_Bookings AS
SELECT * FROM bookings WHERE Booking_Status = 'Success';

-- 2. Average ride distance for each vehicle type (successful rides only;
--    non-success rows have distance 0 and would skew the average)
CREATE OR REPLACE VIEW ride_distance_for_each_vehicle AS
SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) AS avg_distance
FROM bookings
WHERE Booking_Status = 'Success'
GROUP BY Vehicle_Type;

-- 3. Total number of rides canceled by customers
CREATE OR REPLACE VIEW canceled_rides_by_customers AS
SELECT COUNT(*) AS canceled_by_customer
FROM bookings WHERE Booking_Status = 'Canceled by Customer';

-- 4. Top 5 customers by number of rides
CREATE OR REPLACE VIEW Top_5_Customers AS
SELECT Customer_ID, COUNT(Booking_ID) AS total_rides
FROM bookings
GROUP BY Customer_ID
ORDER BY total_rides DESC, Customer_ID
LIMIT 5;

-- 5. Rides canceled by drivers due to personal & car-related issues
CREATE OR REPLACE VIEW Rides_canceled_by_Drivers_P_C_Issues AS
SELECT COUNT(*) AS personal_car_issue_cancellations
FROM bookings WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- 6. Max and min driver rating for Prime Sedan bookings
CREATE OR REPLACE VIEW Max_Min_Driver_Rating AS
SELECT MAX(Driver_Ratings) AS max_rating, MIN(Driver_Ratings) AS min_rating
FROM bookings WHERE Vehicle_Type = 'Prime Sedan';

-- 7. All rides paid with UPI
CREATE OR REPLACE VIEW UPI_Payment AS
SELECT * FROM bookings WHERE Payment_Method = 'UPI';

-- 8. Average customer rating per vehicle type
CREATE OR REPLACE VIEW AVG_Cust_Rating AS
SELECT Vehicle_Type, ROUND(AVG(Customer_Rating), 2) AS avg_customer_rating
FROM bookings
GROUP BY Vehicle_Type;

-- 9. Total booking value of successfully completed rides
CREATE OR REPLACE VIEW total_successful_ride_value AS
SELECT SUM(Booking_Value) AS total_successful_ride_value
FROM bookings WHERE Booking_Status = 'Success';

-- 10. All incomplete rides with the reason
CREATE OR REPLACE VIEW Incomplete_Rides_Reason_View AS
SELECT Booking_ID, Incomplete_Rides_Reason
FROM bookings WHERE Incomplete_Rides = 'Yes';

-- ---- Retrieve the answers ----
SELECT * FROM Successful_Bookings LIMIT 100;
SELECT * FROM ride_distance_for_each_vehicle;
SELECT * FROM canceled_rides_by_customers;
SELECT * FROM Top_5_Customers;
SELECT * FROM Rides_canceled_by_Drivers_P_C_Issues;
SELECT * FROM Max_Min_Driver_Rating;
SELECT * FROM UPI_Payment LIMIT 100;
SELECT * FROM AVG_Cust_Rating;
SELECT * FROM total_successful_ride_value;
SELECT * FROM Incomplete_Rides_Reason_View;
