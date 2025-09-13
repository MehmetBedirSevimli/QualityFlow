USE QualityFlowDB;
IF OBJECT_ID('dbo.SensorData','U') IS NULL
BEGIN
  CREATE TABLE dbo.SensorData (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    SensorName NVARCHAR(50),
    Value FLOAT,
    Timestamp DATETIME DEFAULT GETDATE()
  );
END;
