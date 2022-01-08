grammar time;

options {
     language = Python3;
}
     
r : value':'value ;
value : Num ;
Num : [0-9]+ ;
WS : [ \t\r\n]+ -> skip;