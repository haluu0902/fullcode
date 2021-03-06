USE [master]
GO
Create database Y20FA1B1
GO
USE Y20FA1B1
GO

CREATE TABLE [dbo].[Laptop](
	[LaptopID] [nvarchar](10) NOT NULL primary key,
	[LaptopName] [nvarchar](30) NOT NULL,
	[ProductDate] datetime NOT NULL,
	[Price] [int] NOT NULL,
	[Quantity] [int] NOT NULL
)
GO
insert into Laptop values('CP20190304','Dell Inspiron N1',CAST(N'2019-03-04' AS Date),1000,5)
insert into Laptop values('CP20190101','Dell Vostro V3',CAST(N'2019-01-01' AS Date),800,4)
insert into Laptop values('CP20200302','Dell Inspiron N2',CAST(N'2020-03-02' AS Date),1200,8)
insert into Laptop values('CP20190904','Dell Vostro V4',CAST(N'2019-09-04' AS Date),900,0)
insert into Laptop values('CP20200605','Acer Aspire A5',CAST(N'2020-06-05' AS Date),700,1)
insert into Laptop values('CP20190306','Acer Swift S6',CAST(N'2019-03-04' AS Date),850,3)
insert into Laptop values('CP20200807','Acer Aspire A7',CAST(N'2020-08-07' AS Date),970,5)
GO

CREATE TABLE [dbo].[Television](
	[TelevisionID] [varchar](10) NOT NULL primary key,
	[TelevisionName] [nvarchar](30) NOT NULL,
	[ProductDate] datetime NOT NULL,
	[Price] [int] NOT NULL,
	[Quantity] [int] NOT NULL
)
GO
insert into Television values('TV0804','LG L1',CAST(N'2019-08-04' AS Date),100,10)
insert into Television values('TV0305','LG L2',CAST(N'2019-03-05' AS Date),200,6)
insert into Television values('TV0506','LG L3',CAST(N'2020-05-06' AS Date),150,1)
insert into Television values('TV0204','Sony L5',CAST(N'2019-02-04' AS Date),120,3)
insert into Television values('TV0307','Sony L6',CAST(N'2020-03-07' AS Date),230,7)
insert into Television values('TV0108','Sony L7',CAST(N'2019-01-08' AS Date),900,0)
GO

CREATE TABLE [dbo].[Speaker](
	[SpeakerID] [varchar](10) NOT NULL primary key,
	[SpeakerName] [nvarchar](30) NOT NULL,
	[ProductDate] datetime NOT NULL,
	[Price] [int] NOT NULL,
	[Quantity] [int] NOT NULL
)
GO

insert into Speaker values('SP202001','Microlab L01',CAST(N'2019-03-04' AS Date),1000,11)
insert into Speaker values('SP202002','Microlab L02',CAST(N'2020-02-01' AS Date),700,5)
insert into Speaker values('SP202003','Microlab L03',CAST(N'2019-01-09' AS Date),6000,2)
insert into Speaker values('SP202004','Sony L01',CAST(N'2020-03-04' AS Date),1100,8)
insert into Speaker values('SP202005','Sony L06',CAST(N'2019-08-05' AS Date),650,0)
insert into Speaker values('SP202006','Sony L07',CAST(N'2019-01-09' AS Date),850,1)
GO