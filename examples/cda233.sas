/* CDA pp. 232 - 233 using SBS */

data cda233;
 infile "cda233.dat" firstobs=2;
 length penicillin $ 5 delay $ 4 response $ 5;
 input penicillin delay response count;
run;

proc freq cda233;
 tables penicillin * delay * response / norow nocol nopercent cmh;
 weight count;
run;
