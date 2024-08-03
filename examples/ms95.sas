data ms95;
  infile "ms95.dat" firstobs=2;
  input soilphos plantphos;
run;

proc reg ms95;
 model plantphos = soilphos;
 plot phantphos * soilphos;
run;
