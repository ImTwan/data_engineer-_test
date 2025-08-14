-- Create sample tables
CREATE TABLE ORDER_TABLE (
    Order_ID INT PRIMARY KEY,
    Client_ID INT,
    Date_Order DATE,
    Good_Type VARCHAR(50),
    Good_Amount DECIMAL(10,2)
);

CREATE TABLE ORDER_DELIVERY (
    Delivery_ID INT PRIMARY KEY,
    Order_ID INT,
    Date_Delivery DATE
);

-- Insert sample data
INSERT INTO ORDER_TABLE (Order_ID, Client_ID, Date_Order, Good_Type, Good_Amount) VALUES
(1, 101, '2019-09-05', 'TypeA', 200),
(2, 101, '2019-09-15', 'TypeB', 300),
(3, 102, '2019-10-01', 'TypeA', 150),
(4, 103, '2019-09-20', 'TypeC', 500),
(5, 101, '2019-09-25', 'TypeA', 200);

INSERT INTO ORDER_DELIVERY (Delivery_ID, Order_ID, Date_Delivery) VALUES
(1, 1, '2019-09-07'),
(2, 2, '2019-09-18'),
(3, 3, '2019-10-02'),
(4, 4, '2019-09-21'),
(5, 5, '2019-09-27');
