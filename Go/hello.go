package main

import(
	"fmt"
)

type inf interface{
	Say()
}

type A struct{
	name string
	age int
}

type B struct{
	name string
	age int
}

func (a *A)Say(){
	fmt.Println(a.name,a.age);
}

func sayThis(i inf){
	i.Say();
}
func main(){
	a := &A{name:"testA",age:18};
	sayThis(a);
}
