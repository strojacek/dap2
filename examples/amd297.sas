/* AMD pp. 297 - 308 using SBS
 * Split plot
 */

data amd297;
 infile "amd297.dat" firstobs=2;
 length fertilizer $ 1 block $ 1 variety $ 1;
 input block variety fertilizer yield;
run;

proc glm amd297;
 title "Whole plot (block, fertilizer) analysis";
 class fertilizer block variety;
 model yield = fertilizer block;
 lsmeans fertilizer / e=fertilizer*block LSD;
run;

proc glm amd297;
 title "Subplot (variety) analysis";
 class fertilizer block variety;
 model yield = fertilizer block variety
               fertilizer*block fertilizer*variety;
run;