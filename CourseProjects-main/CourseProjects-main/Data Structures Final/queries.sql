select * from fees,school where school_unitID=1 and unitID=1;

select distinct name from school;

select * from fees order by tuition;

select avg(tuition) from fees where school_unitID=15;

select count(one_time_fees) from fees;

select fees.*, school.name from fees inner join school on fees.school_UnitID=school.UnitID;

select student.first_name,student.last_name,fees.tuition from student inner join fees on fees.feeID=student.fees_feeID;

update student set fees_feeID = 2 where studentID=13;
select * from student where studentID=13;

delete from student where fees_feeID=4;
select * from student where fees_feeID=4;