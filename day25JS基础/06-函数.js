//1、函数的声明：
//function 函数名（参数列表）{函数体}
//a、 function - 关键字
//b、函数名 - 驼峰式；见名知意
//c、参数：参数可以有默认值，有默认值的参数要写在后面。调用函数传参的时候，
//是按实参的位置来传参，保证每个参数都有值
//d、函数体；实现函数的功能，只有在调用的时候才能执行

//函数没有return的时候，函数返回值是undefined
function sum1(num1 = 1,num2){
	console.log('求两个数的和')
	return num1 + num2
}
console.log(sum1(10,42))

//2、函数的调用
//函数名（实参列表），调用过程和python一样

//3、作用域
//全局变量：声明在函数外的变量（从变量声明的位置到文件结束）
//局部变量：声明在函数里面的变量（从变量声明到函数结束）,函数的参数也是局部变量

//aaa就是全局变量
var aaa=100

function func2(){
	//bbb就是局部变量
	var bbb= 100
	console.log(aaa,bbb)
	//函数中可以修改全局变量的值
	aaa=200
	//函数中可以声明函数
	function func22(){
		bbb= 1.1
		console.log(bbb)
	}
}
//个数不定参数，js不支持