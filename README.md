# CNTCollege
solve_diophantine(a,b,c) =
{
  if(a==0 && b==0,
    if(c==0, print("Infinite solutions (0x + 0y = 0)."); return([0,0]);,
           print("No solutions (0x + 0y = ",c,")."); return([]); )
  );

  V = gcdext(a,b);    
  xg = V[1]; yg = V[2]; d = V[3];

  if(d == 0,
    if(c==0, print("Infinite solutions."); return([0,0]);, print("No solutions."); return([]);)
  );

  if(c % d != 0,
    print("No integer solutions: gcd(",a,", ",b,") = ",d," does not divide ",c);
    return([]);
  );

  x0 = xg * (c/d);
  y0 = yg * (c/d);
  print("GCD","(",a",",b,")","=",d );
  print("Particular solution: x = ", x0, ", y = ", y0);
  print("General solution: x = ", x0, " + k*(", b/d, "), y = ", y0, " - k*(", a/d, ")");

  return([x0,y0]);
}