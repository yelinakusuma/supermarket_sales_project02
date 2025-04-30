-- URL dataset: https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales/data

-- Create table
CREATE TABLE table_m3 (
	"Invoice ID" TEXT,
	"Branch" TEXT,
	"City" TEXT,
	"Customer type" TEXT,
	"Gender" TEXT,
	"Product line" TEXT,
	"Unit price" NUMERIC(10,2),
	"Quantity" INTEGER,
	"Tax 5%" NUMERIC(10,4),
	"Sales" NUMERIC(10,4),
	"Date" DATE,
	"Time" TIME,
	"Payment" TEXT,
	"cogs" NUMERIC(10,2),
	"gross margin percentage" NUMERIC(10,9),
	"gross income" NUMERIC(10,4),
	"Rating" NUMERIC(3,1)
);

-- Copy table
COPY table_m3
FROM '/tmp/P2M3_yelina_kusuma_data_raw.csv'
DELIMITER ','
CSV HEADER;

