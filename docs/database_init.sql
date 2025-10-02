CREATE DATABASE QualityFlowDB;
GO

USE QualityFlowDB;
GO

IF OBJECT_ID('dbo.readings', 'U') IS NOT NULL
    DROP TABLE dbo.readings;
GO

CREATE TABLE dbo.readings (
    id INT IDENTITY(1,1) PRIMARY KEY,
    timestamp DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    device_id NVARCHAR(50) NOT NULL,
    temperature FLOAT NULL,
    pressure FLOAT NULL,
    motorspeed FLOAT NULL,
    cyclecounter BIGINT NULL
);
GO
