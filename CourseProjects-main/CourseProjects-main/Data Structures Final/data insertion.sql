#Inserts all data into school table
insert into school(name,grad_undergrad,sub_category)values
('Portland State University','Undergraduate',null),
('Portland State University','Graduate',null),
('Portland State University','Graduate','College of the Arts(all programs)'),
('Portland State University','Graduate','College of Education(all programs)'),
('Portland State University','Graduate','College of Liberal Arts and Sciences Level 1'),
('Portland State University','Graduate','College of Liberal Arts and Sciences Level 2'),
('Portland State University','Graduate','College of Urban Affairs: Economics'),
('Portland State University','Graduate','College of Urban Affairs: EMPA'),
('Portland State University','Graduate','Maseeh College of Engineering & Computer Science (all programs)'),
('Portland State University','Graduate','School of Business: Master of Finance & Master of Taxation'),
('Portland State University','Graduate','School of Business: Master of Global Supply Chain Management'),
('Portland State University','Graduate','School of Business: All other Graduate Buiness Programs'),
('Portland State University','Graduate','School of Social Work: MSW and PhD'),
('Southern Oregon University','Undergraduate',null),
('Southern Oregon University','Graduate',null),
('Southern Oregon University','Graduate','Online Masters of Business Administration Program'),
('Oregon State University','Undergraduate',null),
('Oregon State University','Graduate',null),
('Oregon Institute of Technology','Undergraduate','Kalamath Falls'),
('Oregon Institute of Technology','Undergraduate','Portland-Metro'),
('Rogue Community College','Undergraduate',null),
('Portland Community College','Undergraduate',null),
('Pacific University Oregon','Undergraduate','College of Arts & Sciences'),
('Pacific University Oregon','Undergraduate','College of Health Profession Bachelor of Health Science'),
('Pacific University Oregon','Undergraduate','College of Health Profession Bachelor of Science in Dental Health'),
('Pacific University Oregon','Undergraduate','College of Education Lane County Undergraduate'),
('Pacific University Oregon','Undergraduate','College of Education Woodburn Undergraduate'),
('Linn Benton Community College','Undergraduate',null),
('Central Oregon Community College','Undergraduate',null);

#inserts all data from Portland State University
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident w/ Family',4035,10386,60,1200,1002,1500,350,1),
('Resident on Campus',12144,10386,60,1200,1002,1500,350,1),
('Washington Border Discount',12144,11392,60,1200,1002,1500,350,1),
('Western Undergrad Exchange',12144,14730,60,1200,1350,1500,350,1),
('Non-Resident',12144,29286,60,1200,1350,1500,350,1),

('Resident & WICHE',12144,456,65,1200,1002,1500,2,2),
('Washington Border Discount',12144,502,65,1200,1002,1500,2,2),
('Non-Resident',12144,683,65,1200,1350,1500,2,2),

('Resident',12144,503,65,1200,1002,1500,2,3),
('Washington Border Discount',12144,549,65,1200,1002,1500,2,3),
('Non-Resident',12144,734,65,1200,1350,1500,2,3),

('Resident',12144,505,65,1200,1002,1500,2,4),
('Washington Border Discount',12144,551,65,1200,1002,1500,2,4),
('Non-Resident',12144,732,65,1200,1350,1500,2,4),

('Resident & WICHE',12144,471,65,1200,1002,1500,2,5),
('Washington Border Discount',12144,517,65,1200,1002,1500,2,5),
('Non-Resident',12144,698,65,1200,1350,1500,2,5),

('Resident & WICHE',12144,478,65,1200,1002,1500,2,6),
('Washington Border Discount',12144,524,65,1200,1002,1500,2,6),
('Non-Resident',12144,708,65,1200,1350,1500,2,6),

('Resident',12144,471,65,1200,1002,1500,2,7),
('Washington Border Discount',12144,517,65,1200,1002,1500,2,7),
('Non-Resident',12144,698,65,1200,1350,1500,2,7),

('Resident',12144,1900,65,1200,1002,1500,2,8),
('Washington Border Discount',12144,1900,65,1200,1002,1500,2,8),
('Non-Resident',12144,1900,65,1200,1350,1500,2,8),

('Resident',12144,509,65,1200,1002,1500,2,9),
('Washington Border Discount',12144,554,65,1200,1002,1500,2,9),
('Non-Resident',12144,736,65,1200,1350,1500,2,9),

('Resident & WICHE',12144,542,65,1200,1002,1500,2,10),
('Washington Border Discount',12144,588,65,1200,1002,1500,2,10),
('Non-Resident',12144,736,65,1200,1350,1500,2,10),

('Resident & WICHE',12144,542,65,1200,1002,1500,2,11),
('Washington Border Discount',12144,588,65,1200,1002,1500,2,11),
('Non-Resident',12144,720,65,1200,1350,1500,2,11),

('Resident & WICHE',12144,656,65,1200,1002,1500,2,12),
('Washington Border Discount',702,502,65,1200,1002,1500,2,12),
('Non-Resident',12144,797,65,1200,1350,1500,2,12),

('Resident',12144,521,65,1200,1002,1500,2,13),
('Washington Border Discount',12144,567,65,1200,1002,1500,2,13),
('Non-Resident',12144,748,65,1200,1350,1500,2,13);

#Inserts all data from Southern Oregon University
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident (on campus)',15066,11142,60,999,999,1500,null,14),
('Resident (off campus)',11501,11142,60,999,999,1500,null,14),
('Resident (w/ family)',4909,11142,60,999,999,1500,null,14),
('Non-Resident (on campus)',15066,28962,60,999,999,1500,null,14),
('Non-Resident (off campus)',11501,28962,60,999,999,1500,null,14),
('Non-Resident (w/ family)',4909,28962,60,999,999,1500,null,14),
('WUE (on campus)',15066,15664,60,999,999,1500,null,14),
('WUE (off campus)',11501,15664,60,999,999,1500,null,14),
('WUE (w/ family)',4909,15664,60,999,999,1500,null,14),

('Resident (on campus)',15066,15462,60,999,999,1500,null,15),
('Resident (off campus)',11501,15462,60,999,999,1500,null,15),
('Resident (w/ family)',4909,15462,60,999,999,1500,null,15),
('Non-Resident (on campus)',15066,18567,60,999,999,1500,null,15),
('Non-Resident (off campus)',11501,18567,60,999,999,1500,null,15),
('Non-Resident (w/ family)',4909,18567,60,999,999,1500,null,15),
('Online',10166,7895,60,999,999,1698,null,16);

#Inserts all data from Oregon State University
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident',13860,12444,null,600,567,2178,null,17),
('Non-Resident',13860,33063,null,600,576,2178,null,17),
('Ecampus',14248,13479,null,600,594,2247,null,17),

('Resident',13860,15576,null,600,567,2178,null,18),
('Non-Resident',13860,29403,null,600,576,2178,null,18),
('Ecampus',14248,13479,null,600,594,2247,null,18);

#Inserts all data from OIT 
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident',5835,11622,50,1225,2459,2459,null,19),
('WUE',5835,16408,50,1225,2459,2459,null,19),
('Non-Resident',5835,32516,50,1225,2459,2459,null,19),

('Resident',5835,9986,50,1225,2459,2459,null,20),
('WUE',5835,14771,50,1225,2459,2459,null,20),
('Non-Resident',5835,30880,50,1225,2459,2459,null,20);

#Inserts all data from Rogue Community College
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident',null,1728,null,null,null,null,null,21),
('Non-Resident',null,2064,null,null,null,null,null,21),
('International',null,5088,null,null,null,null,null,21);

#Inserts all data from Portland Community College
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident',null,1759.70,null,75,53,null,null,22),
('Non-Resident',null,1759.70,null,75,53,null,null,22),
('Nursing',null,null,50,null,53,null,null,22);

#Inserts all data from Pacific University Oregon
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Student On Campus',14408,52072,null,1050,800,1000,null,23),
('Student Off Campus',9806,52072,null,1050,800,1000,null,23),

('1st Year',14166,12050,null,2300,1125,1125,170,24),
('2nd Year',4722,7020,null,150,375,375,null,24),

('1st Year',18888,35595,null,5400,1500,1500,905,25),
('2nd Year',18888,34370,null,700,2000,1500,2500,25),

('Entering(12 Months/30 Credits)',18600,12079,null,600,1800,1500,null,26),
('Returning(10 Months/22 Credits)',15500,8756,null,600,1500,1250,300,26),

('1st Year',14166,11166,null,1200,1125,2250,172,27),
('2nd Year',14166,11502,null,1200,1125,2250,587,27);

#Inserts all data from Linn Benton Community College
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('Resident (w/ family)',4548,6102,null,927,2064,1698,null,28),
('Resident (off campus)',13644,6102,null,927,2064,1698,null,28),
('Non-Resident',13644,8844,null,927,2064,1698,null,28),
('International',13644,10792.50,null,927,2064,1698,null,28);

#Inserts all data from Central Oregon Community College
insert into fees(type,housing_fees,tuition,application_fee,supply_fees,transportation,personal_expenses,one_time_fees,school_unitID)values
('In-District',null,1587,25,null,null,null,null,29),
('Non-Resident Veteran',null,1863,25,null,null,null,null,29),
('Out-of-District/In-State',null,2139,25,null,null,null,null,29),
('Border State(CA,ID,NV, & WA)',null,2139,25,null,null,null,null,29),
('Out-of-State',null,4203,25,null,null,null,null,29),
('International Students',null,4203,25,null,null,null,null,29);



