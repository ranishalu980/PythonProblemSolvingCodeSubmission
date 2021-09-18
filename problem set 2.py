##Problem set 2.1
def evaluationofpoly (poly,x):
  result=0
  for i in poly:
    result+=(poly[poly.index(i)])*(x**(poly.index(i)))
  return result

  Eqn=tuple(poly)
  result=Eqn[0]
  for i in range(1,len(Eqn)):
     result+=Eqn[i]*(x**1)
     print(Eqn[i],resuly)
     print(float(result))

poly=(0.0,0.0,5.0,9.3,7.0)
print(evaluationofpoly(poly,-13))


##problem set 2.2
def compute_deriv(poly):
    deriv=()
    for i in poly:
        if(poly.index(i))>0:
            deriv= deriv+(((poly.index(i))*i),)
    return result
    Eqn=tuple(poly)
    result=0
    result=result+(Eqn[1],)
    for i in range(1,(Eqn[1])):
        if Eqn[1] !=0:
            result+=(Eqn[1]*i,)
            print(result)

poly=(-13.39,0.0,17.5,3.0,1.0)
print(Compute_deriv(poly))

##problem set 2.3
def compute_root(poly,x_0,epln):
   root=x_0
   i=1.0
   deriv=compute_derive(poly)

   while abs(evaluate_poly(poly,root))>epln:
     root=root-evaluate_poly(poly,root)/evalute_poly(derive,root)
     i+=1.0
   return root,1

     -root_poly=x_0
     inc=1
     while(evaluate_poly(poly,root_poly))>=epln:
         root_poly=(root_poly-evaluate_poly(poly,root_poly)/compute_deriv(poly,root_poly)
         inc+=1
     return (root_poly,inc)

poly=(-13.39,0.0,17.5,3.0,1.0)
x_0=0.1
epln=0.0001
print(compute_root(poly,x_0,epln)









                   
    
          
     






