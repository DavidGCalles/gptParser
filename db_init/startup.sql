-- Create the receipts table if it does not already exist
CREATE TABLE IF NOT EXISTS receipts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    supermarket VARCHAR(255),  -- Storing supermarket as a string directly in receipts
    payment_method VARCHAR(50),  -- Storing payment method as a string directly in receipts
    base64_image LONGTEXT  -- Column to store base64 encoded image string
);

-- Create the items table if it does not already exist
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receipt_id INT,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (receipt_id) REFERENCES receipts(id) ON DELETE CASCADE
);
