-- Ola Bengaluru Ride Analytics | MySQL 8.x
CREATE DATABASE IF NOT EXISTS Ola;
USE Ola;

DROP TABLE IF EXISTS bookings;
CREATE TABLE bookings (
    Date                        DATE,
    Time                        TIME,
    Booking_ID                  VARCHAR(15) PRIMARY KEY,
    Booking_Status              VARCHAR(30),
    Customer_ID                 VARCHAR(15),
    Vehicle_Type                VARCHAR(20),
    Pickup_Location             VARCHAR(50),
    Drop_Location               VARCHAR(50),
    V_TAT                       DECIMAL(8,1),
    C_TAT                       DECIMAL(8,1),
    Canceled_Rides_by_Customer  VARCHAR(60),
    Canceled_Rides_by_Driver    VARCHAR(60),
    Incomplete_Rides            VARCHAR(5),
    Incomplete_Rides_Reason     VARCHAR(30),
    Booking_Value               INT,
    Payment_Method              VARCHAR(20),
    Ride_Distance               INT,
    Driver_Ratings              DECIMAL(3,1),
    Customer_Rating             DECIMAL(3,1)
);
