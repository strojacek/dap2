/* CDA pp. 49 - 50 using SBS */

data cda50;
 infile "cda50.dat" firstobs=2;
 length income $ 5 jobsat $ 10;
 input income jobsat count;
run;

proc freq cda50;
 tables income * jobsat / measures chisq expected
                          norow nocol nopercent;
 weight count;
run;