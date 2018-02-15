//console.log(document.getElementById("fish").innerHTML);
document.getElementById("fish").innerHTML = "Нажми сюда чтобы вывести текст в консоль";
//console.log(document.getElementsByTagName("div")[1].innerHTML);
//console.log(document.getElementsByClassName("new_div")[0].innerHTML);
//alert(document.getElementsByName("meat")[0].innerHTML)
console.log(document.querySelector(".new_div span").innerHTML);
//document.querySelector(".new_div span").style.color = "wheat";
document.querySelector(".new_div span").setAttribute("title", "title is working");
document.querySelector(".new_div span").setAttribute("style", "background-color:red;");
function putin(){
	console.log("Текст")
}

document.querySelector(".new_div").setAttribute("style", "background-color:green;");

function dirt(my_obj){
	my_obj.setAttribute("style", "height:100px; background-color:#696969; color:red; font-size:40px")
}

alert(document.querySelector(".new_div span").getAttribute("onclick"));